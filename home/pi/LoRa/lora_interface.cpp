//  Interface to send and receive LoRa messages, exposing a Python wrapper via Swig.
//  We compress JSON messages with MessagePack to reduce transmitted message size.
//  Semtech SX1272 Datasheet: http://www.semtech.com/images/datasheet/sx1272.pdf

#ifdef MESSAGE_PACK
#include <msgpack.h>
#endif  //  MESSAGE_PACK
#include <stdio.h>
#include "arduPiLoRa.h"  //  Include the SX1272 and SPI library.
#include "hope_rfm96.h"
#include "lora_interface.h"
#include "dragino_gps_hat.h"

char *decodeChannel(uint32_t code);
extern int lora_snr; int lora_snr = 0;

int e;
extern char lora_packet[]; char lora_packet[1024];
extern int lora_packet_length; int lora_packet_length = 0;

static int setupDone = 0;
static int sendCount = 0;
static int receiveCount = 0;

//  Which LoRa shield is being used: Libelium or Dragino GPS HAT.
enum Shields { Libelium = 0, Dragino = 1 };
static Shields shield = Dragino;

int getLoRaStatus()
{
    //  Return the status of the last send/receive command.
    return e;
}

int getLoRaSetupDone()
{
    //  Returns non-zero if setup has been called.
    return setupDone;
}

int getLoRaSendCount()
{
    //  Returns the number of send message requests.
    return sendCount;
}

int getLoRaReceiveCount()
{
    //  Returns the number of receive message requests.
    return receiveCount;
}

uint8_t readLoRaRegister(uint8_t reg)
{
    //  Return the value of the register.
    switch (shield) {
        case Dragino:
            return readDraginoRegister(reg);
        case Libelium:
            return sx1272.readRegister(reg);
    }
}

void writeLoRaRegister(uint8_t reg, uint8_t value)
{
    //  Write the value into the register.
    switch (shield) {
        case Dragino:
            return writeDraginoRegister(reg, value);
        case Libelium:
            return sx1272.writeRegister(reg, value);
    }
}

int setupLoRa(int address, int mode, uint32_t channel, char *power)
{
  //  Init the node with the specified LoRa address (1 to 255).
  if (setupDone > 0)
  {
    printf("setupLoRa ERROR: setupLoRa already called");
    return -1;
  }
  printf("setupLoRa: LoRa module and Raspberry Pi: send packets without ACK\n");
  //  Check which shield is used.
  shield = Dragino;
  e = setupDraginoLoRa(address, mode, channel, power);
  //  In case of error, assume shield is Libelium.
  if (e < 0) shield = Libelium;
  switch (shield) {
    case Dragino:
        //  Already initialised earlier.
        //e = setupDraginoLoRa(address, mode, channel, power);
        break;
    case Libelium:
        // Power ON the module
        e = sx1272.ON();
        printf("setupLoRa: Setting power ON: state %d\n", e);

        // Set transmission mode
        e = sx1272.setMode(mode);
        printf("setupLoRa: Setting Mode %d: state %d\n", mode, e);

        // Set header
#ifdef HEADER_OFF
        //  Disable standard header for debugging.
        e = sx1272.setHeaderOFF();
        printf("**** setupLoRa: Setting Header OFF: state %d\n", e);
#else
        e = sx1272.setHeaderON();
        printf("setupLoRa: Setting Header ON: state %d\n", e);
#endif  //  HEADER_OFF

        // Select frequency channel
        e = sx1272.setChannel(channel);
        printf("setupLoRa: Setting Channel %s: state %d\n", decodeChannel(channel), e);

        // Set CRC
#define CRC_OFF ////  Needed for SX1272 to send to RH96 in Mode 1
#ifdef CRC_OFF
        //  Disable CRC for debugging.
        e = sx1272.setCRC_OFF();
        printf("**** setupLoRa: Setting CRC OFF: state %d\n", e);
        #else
        e = sx1272.setCRC_ON();
        printf("setupLoRa: Setting CRC ON: state %d\n", e);
#endif  //  CRC_OFF

        // Select output power (Max, High or Low)
        e = sx1272.setPower(*power);
        printf("setupLoRa: Setting Power %s: state %d\n", power, e);

        // Set the node address
        e = sx1272.setNodeAddress(address);
        printf("setupLoRa: Setting Node address %d: state %d\n", address, e);

#ifdef INVERT_IQ
        // Refer to http://openlora.com/forum/viewtopic.php?t=887
        // Also see example of SX1272-SX1276 interop: http://cpham.perso.univ-pau.fr/LORA/RPIgateway.html
        printf("setupLoRa: Before inverting I/Q REG_NODE_ADRS = 0x%02x\n", readLoRaRegister(REG_NODE_ADRS));
        writeLoRaRegister(REG_NODE_ADRS, readLoRaRegister(REG_NODE_ADRS)|(1<<6));
        printf("setupLoRa: After inverting I/Q REG_NODE_ADRS = 0x%02x\n", readLoRaRegister(REG_NODE_ADRS));
#endif  //  INVERT_IQ
        break;
  }

    // Print a success message
    setupDone++;
    printf("setupLoRa: SX1272 successfully configured %d, %d, %d\n", setupDone, sendCount, receiveCount);
    return e;
}

int getLoRaSNRValue(void)
{
    //  Gets the SNR of the last received packet.
    int result;
    uint8_t value = readLoRaRegister(REG_RegPktSnrValue);
    if( value & 0x80 ) // The SNR sign bit is 1
    {
        // Invert and divide by 4
        value = ( ( ~value + 1 ) & 0xFF ) >> 2;
        result = -value;
    }
    else
    {
        // Divide by 4
        result = ( value & 0xFF ) >> 2;
    }
    printf("getLoRaSNRValue: %d\n", result);
    return result;
}

int getRSSICorrection(void)
{
    //  Get the correction value for RSSI, which differs for each chip.
    switch (shield) {
        case Dragino:
            //  Assume Dragino only uses RFM96.
            return 137;
        case Libelium:
            //  Assume Libelium only uses sx1272.
            const int sx1272 = 1;
            if (sx1272) {
                return 139;
            } else {
                return 157;
            }
    }
}

int getLoRaRSSIValue(void)
{
    //  Gets the current value of RSSI.
    int result = readLoRaRegister(REG_RegRssiValue) - getRSSICorrection();
    printf("getLoRaRSSIValue: %d\n", result);
    return result;
}

int getLoRaRSSIpacketValue(void)
{
    //  Gets the RSSI of the last packet.
    int result = readLoRaRegister(REG_RegPktRssiValue) - getRSSICorrection();
    printf("getLoRaRSSIpacketValue: %d\n", result);
    return result;
}

int getLoRaPreambleLengthValue(void)
{
    //  Gets the preamble length.
    uint8_t msb = readLoRaRegister(REG_RegPreambleMsb);
    uint8_t lsb = readLoRaRegister(REG_RegPreambleLsb);
    int result = ((msb << 8) & 0xFFFF) + (lsb & 0xFFFF);
    printf("getLoRaPreambleLengthValue: %d\n", result);
    return result;
}

int sendLoRaMessage(int address, char *msg)
{
	  // Send message and print the result
    printf("sendLoRaMessage: address=%d, msg=%s\n", address, msg);
    if (setupDone == 0) {
        printf("sendLoRaMessage ERROR: setupLoRa not called");
        return -1;
    }
    switch(shield) {
        case Dragino:
            e = 0;
            puts("*** ERROR: sendLoRaMessage not implemented for Dragino");
            break;
        case Libelium:
            e = sx1272.sendPacketTimeout(address, msg);
            break;
    }
    printf("sendLoRaMessage: state=%d\n",e);
    sendCount++;
    printf("sendLoRaMessage: done %d, %d, %d\n", setupDone, sendCount, receiveCount);
    return e;
}

char packet_buffer[4096];
char *hex_digits = (char *) "0123456789abcdef";

char *getLoRaPacket()
{
    //  Return the last packet received.
    printf("getLoRaPacket:\n");
    writeLoRaRegister(REG_FIFO_ADDR_PTR, 0x00);  // Setting address pointer in FIFO data buffer
    packet_buffer[0] = 0;
    int len = 0;
    for(unsigned int i = 0; i < readLoRaRegister(REG_RX_NB_BYTES); i++) {
        int b = readLoRaRegister(REG_FIFO);
        packet_buffer[len++] = hex_digits[b / 16];
        packet_buffer[len++] = hex_digits[b % 16];
        packet_buffer[len++] = ' ';
    }
    packet_buffer[len] = 0;
    printf("getLoRaPacket: done %s\n", packet_buffer);
    return (char *) packet_buffer;
}

void dumpLoRaPacket(void)
{
    //  Dump the last received packet.
    printf("dumpLoRaPacket:\n");
    printf("REG_FIFO_RX_BASE_ADDR = 0x%02x\n", readLoRaRegister(REG_FIFO_RX_BASE_ADDR));
    printf("REG_FIFO_RX_CURRENT_ADDR = 0x%02x\n", readLoRaRegister(REG_FIFO_RX_CURRENT_ADDR));
    printf("REG_RX_NB_BYTES = 0x%02x\n", readLoRaRegister(REG_RX_NB_BYTES));
    printf("REG_RX_HEADER_CNT_VALUE_LSB = 0x%02x\n", readLoRaRegister(REG_RX_HEADER_CNT_VALUE_LSB));
    printf("REG_RX_HEADER_CNT_VALUE_MSB = 0x%02x\n", readLoRaRegister(REG_RX_HEADER_CNT_VALUE_MSB));
    printf("REG_RX_PACKET_CNT_VALUE_LSB = 0x%02x\n", readLoRaRegister(REG_RX_PACKET_CNT_VALUE_LSB));
    printf("REG_RX_PACKET_CNT_VALUE_MSB = 0x%02x\n", readLoRaRegister(REG_RX_PACKET_CNT_VALUE_MSB));

    writeLoRaRegister(REG_FIFO_ADDR_PTR, 0x00);  // Setting address pointer in FIFO data buffer
    for(unsigned int i = 0; i < readLoRaRegister(REG_RX_NB_BYTES); i++)
        printf("[0x%02x] = 0x%02x\n", i, readLoRaRegister(REG_FIFO));
}

void dumpLoRaRegisters(void)
{
    //  Dump out all registers.
    printf("dumpLoRaRegisters:\n");
    for (int r = 0; r <= 0x64; r++)
        printf("Reg[0x%X] = 0x%X\n", r, readLoRaRegister(r));
}

char *receiveLoRaMessage(int timeout)
{
    //  Receive message. Wait till timeout, in milliseconds.
    printf("receiveLoRaMessage: start\n");
    if (setupDone == 0)
    {
        printf("receiveLoRaMessage ERROR: setupLoRa not called");
        return (char *) "ERROR";
    }
    printf("receiveLoRaMessage REG_HOP_CHANNEL = 0x%02x\n", readLoRaRegister(REG_HOP_CHANNEL));
    printf("receiveLoRaMessage REG_MODEM_CONFIG1 = 0x%02x\n", readLoRaRegister(REG_MODEM_CONFIG1));
    printf("receiveLoRaMessage REG_MODEM_CONFIG2 = 0x%02x\n", readLoRaRegister(REG_MODEM_CONFIG2));
    lora_packet_length = 0;
    lora_packet[0] = 0;  //  Empty the string.
    switch(shield) {
        case Dragino: {
            unsigned long start_time = millis();
            while(millis() - start_time < (unsigned long) timeout) {
                e = receiveDraginoPacket();
                if (e == 0) break;
                //  Condition to avoid an overflow (DO NOT REMOVE)
                if (millis() < start_time)
                    start_time = millis();
    		}
            break;
        }
        case Libelium: {
                #ifdef CRC_OFF
                sx1272.setCRC_OFF();
                printf("receiveLoRaMessage REG_MODEM_CONFIG1 = 0x%02x\n", readLoRaRegister(REG_MODEM_CONFIG1));
                //dumpRegisters();
            #endif  //  CRC_OFF
            e = sx1272.receivePacketTimeout(timeout);
            if (e == 0)
            {
                printf("receiveLoRaMessage: state=%d, dst=0x%02x, src=0x%02x, packnum=0x%02x, length=0x%02x\n",
                    e, sx1272.packet_received.dst, sx1272.packet_received.src, sx1272.packet_received.packnum,
                    sx1272.packet_received.length);
                int length = sx1272.packet_received.length;
                if (sizeof(lora_packet) > 0 && length > sizeof(lora_packet) - 1)
                    length = sizeof(lora_packet) - 1;
    #ifdef TRUNCATE_MESSAGES
                if (length > 10) {
                    printf("**** receiveLoRaMessage: truncated to 10 bytes\n");
                    length = 10;
                }
    #endif  //  TRUNCATE_MESSAGES
                unsigned int i;
                for (i = 0; i < sizeof(lora_packet); i++)
                    lora_packet[i] = 0;
                for (i = 0; i < length; i++) {
                    lora_packet[i] = (char)sx1272.packet_received.data[i];
                    printf("%02x ", lora_packet[i]);
                }
                lora_packet[i] = 0;  //  Terminate the string.
                lora_packet_length = length;
            }
            break;
        }
    }
    printf("\nreceiveLoRaMessage: message=%s\n", lora_packet);
    for (int j = 0; j < lora_packet_length; j++) {
      //  TODO: Remove non-ASCII characters.
      if (lora_packet[j] == 0) break;
      if (lora_packet[j] < 0x20 || lora_packet[j] > 0x7f)
        lora_packet[j] = '?';
    }
    receiveCount++;
    printf("receiveLoRaMessage: done %d, %d, %d\n", setupDone, sendCount, receiveCount);
    dumpLoRaPacket(); ////
    return (char *) lora_packet;
}

int getLoRaSender()
{
    //  Return the sender address of the last packet.
    int result = 2;  //  Default sender to address 2.
    switch (shield) {
        case Dragino:
            puts("*** getLoRaSender not implemented for Dragino");
            break;
        case Libelium:
            result = sx1272.packet_received.src;
            break;
    }
    printf("getLoRaSender: %d\n", result);
    return result;
}

int getLoRaRecipient()
{
    //  Return the recipient address of the last packet.
    int result = 1;  //  Default recipient to gateway.
    switch (shield) {
        case Dragino:
            puts("*** getLoRaRecipient not implemented for Dragino");
            break;
        case Libelium:
            result = sx1272.packet_received.dst;
            break;
    }
    printf("getLoRaRecipient: %d\n", result);
    return result;
}

/*
char message1 [] = { 0x1 , 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xa, 0xb, 0xc, 0xd, 0xe, 0xf,
0x1 , 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xa, 0xb, 0xc, 0xd, 0xe, 0xf,
0x00
 };
char message1 [] = { 0x1, 0x1, 0x1, 0x1, 0x1, 0x1, 0x1, 0x1, 0x1, 0x1, 0x1, 0x1, 0x1, 0x1, 0x1, 0x1,
0x00
 };
char message1 [] = { 0x1, 0x1, 0x1, 0x1, 0x1, 0x1, 0x1, 0x1, 0x1, 0x1, 0x1, 0x1, 0x1, 0x1, 0x1, 0x1, 0x1,
0x00
 };
 */
char message1 [] = { 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2,
0x00
 };

//char message2 [] = "Packet 2, broadcast test";

int main() {
    const int address = 2;
    const int mode = 1;
    unsigned int channel = LORA_CH_10_868;
    char *power = (char *) "H";
    int setupStatus = setupLoRa(address, mode, channel, power);
    printf("Setup status %d\n",setupStatus);
    delay(1000);
	while(1) {
        //  Send message1 and print the result
        e = sendLoRaMessage(1, message1);
        printf("Packet sent, state %d\n",e);
        delay(4000);

        // Send message2 broadcast and print the result
        //e = sendLoRaMessage(0, message2);
        //printf("Packet sent, state %d\n",e);

        /*
        //  Receive a message.
        const int timeout = 10000;
        char *msg = receiveLoRaMessage(timeout);
        printf("Received message: %s\n", msg);

        //  Show the receive status.
        int status = getLoRaStatus();
        int setup_done = getLoRaSetupDone();
        int send_count = getLoRaSendCount();
        int receive_count = getLoRaReceiveCount();
        printf("Receive status: %d, %d, %d, %d\n", status, setup_done, send_count, receive_count);

        //  Show the SNR and RSSI.
        int snr = getLoRaSNR();
        int rssi = getLoRaRSSI();
        int rssi_packet = getLoRaRSSIpacket();
        printf("SNR, RSSI, RSSI packet: %d, %d, %d\n", snr, rssi, rssi_packet);
        */
	}
	return (0);
}

char *decodeChannel(uint32_t code) {
    //  Given the channel code, return the name of the channel.
    switch(code) {
        case CH_10_868: return (char *) "LORA_CH_10_868";
        case CH_11_868: return (char *) "LORA_CH_11_868";
        case CH_12_868: return (char *) "LORA_CH_12_868";
        case CH_13_868: return (char *) "LORA_CH_13_868";
        case CH_14_868: return (char *) "LORA_CH_14_868";
        case CH_15_868: return (char *) "LORA_CH_15_868";
        case CH_16_868: return (char *) "LORA_CH_16_868";
        case CH_17_868: return (char *) "LORA_CH_17_868";
        case CH_00_900: return (char *) "LORA_CH_00_900";
        case CH_01_900: return (char *) "LORA_CH_01_900";
        case CH_02_900: return (char *) "LORA_CH_02_900";
        case CH_03_900: return (char *) "LORA_CH_03_900";
        case CH_04_900: return (char *) "LORA_CH_04_900";
        case CH_05_900: return (char *) "LORA_CH_05_900";
        case CH_06_900: return (char *) "LORA_CH_06_900";
        case CH_07_900: return (char *) "LORA_CH_07_900";
        case CH_08_900: return (char *) "LORA_CH_08_900";
        case CH_09_900: return (char *) "LORA_CH_09_900";
        case CH_10_900: return (char *) "LORA_CH_10_900";
        case CH_11_900: return (char *) "LORA_CH_11_900";
        case CH_12_900: return (char *) "LORA_CH_12_900";
    }
    return (char *) "Unknown";
}

//FREQUENCY CHANNELS:
uint32_t LORA_CH_10_868 = CH_10_868; //  0xD84CCC; // channel 10, central freq = 865.20MHz
uint32_t LORA_CH_11_868 = CH_11_868; //  0xD86000; // channel 11, central freq = 865.50MHz
uint32_t LORA_CH_12_868 = CH_12_868; //  0xD87333; // channel 12, central freq = 865.80MHz
uint32_t LORA_CH_13_868 = CH_13_868; //  0xD88666; // channel 13, central freq = 866.10MHz
uint32_t LORA_CH_14_868 = CH_14_868; //  0xD89999; // channel 14, central freq = 866.40MHz
uint32_t LORA_CH_15_868 = CH_15_868; //  0xD8ACCC; // channel 15, central freq = 866.70MHz
uint32_t LORA_CH_16_868 = CH_16_868; //  0xD8C000; // channel 16, central freq = 867.00MHz
uint32_t LORA_CH_17_868 = CH_17_868; //  0xD90000; // channel 16, central freq = 868.00MHz
uint32_t LORA_CH_00_900 = CH_00_900; //  0xE1C51E; // channel 00, central freq = 903.08MHz
uint32_t LORA_CH_01_900 = CH_01_900; //  0xE24F5C; // channel 01, central freq = 905.24MHz
uint32_t LORA_CH_02_900 = CH_02_900; //  0xE2D999; // channel 02, central freq = 907.40MHz
uint32_t LORA_CH_03_900 = CH_03_900; //  0xE363D7; // channel 03, central freq = 909.56MHz
uint32_t LORA_CH_04_900 = CH_04_900; //  0xE3EE14; // channel 04, central freq = 911.72MHz
uint32_t LORA_CH_05_900 = CH_05_900; //  0xE47851; // channel 05, central freq = 913.88MHz
uint32_t LORA_CH_06_900 = CH_06_900; //  0xE5028F; // channel 06, central freq = 916.04MHz
uint32_t LORA_CH_07_900 = CH_07_900; //  0xE58CCC; // channel 07, central freq = 918.20MHz
uint32_t LORA_CH_08_900 = CH_08_900; //  0xE6170A; // channel 08, central freq = 920.36MHz
uint32_t LORA_CH_09_900 = CH_09_900; //  0xE6A147; // channel 09, central freq = 922.52MHz
uint32_t LORA_CH_10_900 = CH_10_900; //  0xE72B85; // channel 10, central freq = 924.68MHz
uint32_t LORA_CH_11_900 = CH_11_900; //  0xE7B5C2; // channel 11, central freq = 926.84MHz
uint32_t LORA_CH_12_900 = CH_12_900; //  0xE4C000; // default channel 915MHz, the module is configured with it

#ifdef MESSAGE_PACK
  //  Test MessagePack. Create MessagePack buffer and serializer instance.
  //  MessagePack buffer and serializer instance.
  msgpack_sbuffer* buffer = NULL;
  msgpack_packer* pk = NULL;

  buffer = msgpack_sbuffer_new();
  pk = msgpack_packer_new(buffer, msgpack_sbuffer_write);
  for (int j = 0; j < 5; j++)
  {
     //  NB: the buffer needs to be cleared on each iteration.
     msgpack_sbuffer_clear(buffer);

     //  Serializes ["Hello", "MessagePack"].
     msgpack_pack_array(pk, 3);
     msgpack_pack_bin(pk, 5);
     msgpack_pack_bin_body(pk, "Hello", 5);
     msgpack_pack_bin(pk, 11);
     msgpack_pack_bin_body(pk, "MessagePack", 11);
     msgpack_pack_int(pk, j);

     //  Deserializes it.
     msgpack_unpacked msg;
     msgpack_unpacked_init(&msg);
     bool success = msgpack_unpack_next(&msg, buffer->data, buffer->size, NULL);

     //  Prints the deserialized object.
     msgpack_object obj = msg.data;
     msgpack_object_print(stdout, obj);  // => ["Hello", "MessagePack"]
     puts("");
  }
  //  Cleaning.
  //msgpack_sbuffer_free(buffer);
  //msgpack_packer_free(pk);
#endif  //  MESSAGE_PACK
