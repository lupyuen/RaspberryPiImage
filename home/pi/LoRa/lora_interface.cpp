//  Interface to send and receive LoRa messages, exposing a Python wrapper via Swig.
//  We compress JSON messages with MessagePack to reduce transmitted message size.
//  Semtech SX1272 Datasheet: http://www.semtech.com/images/datasheet/sx1272.pdf

#ifdef MESSAGE_PACK
#include <msgpack.h>
#endif  //  MESSAGE_PACK
#include <stdio.h>
#include "arduPiLoRa.h"  //  Include the SX1272 and SPI library.
#include "lora_interface.h"
char *decodeChannel(uint32_t code);

int e;
char my_packet[1024];

static int setupDone = 0;
static int sendCount = 0;
static int receiveCount = 0;

enum Shields { Libelium = 0, Dragino = 1 };
static Shields shield = Dragino;

int getLoRaStatus()
{
  return e;
}

int getLoRaSetupDone()
{
  return setupDone;
}

int getLoRaSendCount()
{
  return sendCount;
}

int getLoRaReceiveCount()
{
  return receiveCount;
}

int setupLoRa(int address, int mode, uint32_t channel, char *power)
{
  //  Init the node with the specified LoRa address (1 to 255).
  if (setupDone > 0)
  {
    printf("setupLoRa ERROR: setupLoRa already called");
    return -1;
  }
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

  // Print a start message
  printf("setupLoRa: SX1272 module and Raspberry Pi: send packets without ACK\n");
  
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
  printf("setupLoRa: Before inverting I/Q REG_NODE_ADRS = 0x%02x\n", sx1272.readRegister(REG_NODE_ADRS));
  sx1272.writeRegister(REG_NODE_ADRS, sx1272.readRegister(REG_NODE_ADRS)|(1<<6));
  printf("setupLoRa: After inverting I/Q REG_NODE_ADRS = 0x%02x\n", sx1272.readRegister(REG_NODE_ADRS));
#endif  //  INVERT_IQ

  // Print a success message
  setupDone++;
  printf("setupLoRa: SX1272 successfully configured %d, %d, %d\n", setupDone, sendCount, receiveCount);
  return e;
}

int getLoRaSNR(void)
{
    //  Gets the SNR value in LoRa mode and stores into _SNR.
    int8_t result = sx1272.getSNR();
    printf("getLoRaSNR: %d\n", result);
    return result;
}

int getLoRaSNRValue(void)
{
    //  Gets the SNR value from _SNR.
    int result = sx1272._SNR;
    printf("getLoRaSNRValue: %d\n", result);
    return result;
}

int getLoRaRSSI(void)
{
    //  Gets the current value of RSSI from the channel and stores into _RSSI.
    uint8_t result = sx1272.getRSSI();
    printf("getLoRaRSSI: %d\n", result);
    return result;
}

int getLoRaRSSIValue(void)
{
    //  Gets the current value of RSSI from _RSSI.
    int result = sx1272._RSSI;
    printf("getLoRaRSSIValue: %d\n", result);
    return result;
}

int getLoRaRSSIpacket(void)
{
    //  Gets the RSSI of the last packet received in LoRa mode and stores into _RSSIpacket.
    int16_t result = sx1272.getRSSIpacket();
    printf("getLoRaRSSIpacket: %d\n", result);
    return result;
}

int getLoRaRSSIpacketValue(void)
{
    //  Gets the RSSI of the last packet from _RSSIpacket.
    int result = sx1272._RSSIpacket;
    printf("getLoRaRSSIpacketValue: %d\n", result);
    return result;
}

int getLoRaPreambleLength(void)
{
    //  Gets the preamble length and stores into _preamblelength.
    uint8_t result = sx1272.getPreambleLength();
    printf("getLoRaPreambleLength: %d\n", result);
    return result;
}

int getLoRaPreambleLengthValue(void)
{
    //  Gets the preamble length from _preamblelength.
    int result = sx1272._preamblelength;
    printf("getLoRaPreambleLengthValue: %d\n", result);
    return result;
}

int sendLoRaMessage(int address, char *msg)
{
	  // Send message and print the result
    printf("sendLoRaMessage: address=%d, msg=%s\n", address, msg);
    if (setupDone == 0)
    {
      printf("sendLoRaMessage ERROR: setupLoRa not called");
      return -1;
    }
    //  TODO: If message starts with "{", assume it's in JSON format and compress with MessagePack.
    e = sx1272.sendPacketTimeout(address, msg);
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
    sx1272.writeRegister(REG_FIFO_ADDR_PTR, 0x00);  // Setting address pointer in FIFO data buffer
    packet_buffer[0] = 0;
    int len = 0;
    for(unsigned int i = 0; i < sx1272.readRegister(REG_RX_NB_BYTES); i++) {
        int b = sx1272.readRegister(REG_FIFO);
        packet_buffer[len++] = hex_digits[b / 16];
        packet_buffer[len++] = hex_digits[b % 16];
        packet_buffer[len++] = ' ';
    }
    packet_buffer[len] = 0;
    printf("getLoRaPacket: done %s\n", packet_buffer);
    return (char *) packet_buffer;
}

void dumpPacket()
{
    //  Dump the last received packet.
    printf("dumpPacket:\n");
    printf("REG_FIFO_RX_BASE_ADDR = 0x%02x\n", sx1272.readRegister(REG_FIFO_RX_BASE_ADDR));
    printf("REG_FIFO_RX_CURRENT_ADDR = 0x%02x\n", sx1272.readRegister(REG_FIFO_RX_CURRENT_ADDR));
    printf("REG_RX_NB_BYTES = 0x%02x\n", sx1272.readRegister(REG_RX_NB_BYTES));
    printf("REG_RX_HEADER_CNT_VALUE_LSB = 0x%02x\n", sx1272.readRegister(REG_RX_HEADER_CNT_VALUE_LSB));
    printf("REG_RX_HEADER_CNT_VALUE_MSB = 0x%02x\n", sx1272.readRegister(REG_RX_HEADER_CNT_VALUE_MSB));
    printf("REG_RX_PACKET_CNT_VALUE_LSB = 0x%02x\n", sx1272.readRegister(REG_RX_PACKET_CNT_VALUE_LSB));
    printf("REG_RX_PACKET_CNT_VALUE_MSB = 0x%02x\n", sx1272.readRegister(REG_RX_PACKET_CNT_VALUE_MSB));

    sx1272.writeRegister(REG_FIFO_ADDR_PTR, 0x00);  // Setting address pointer in FIFO data buffer
    for(unsigned int i = 0; i < sx1272.readRegister(REG_RX_NB_BYTES); i++)
        printf("[0x%02x] = 0x%02x\n", i, sx1272.readRegister(REG_FIFO));

    /*
    sx1272.writeRegister(REG_FIFO_ADDR_PTR, 0x00);  		// Setting address pointer in FIFO data buffer
    for(unsigned int i = 0; i < 20; i++)
        sx1272.writeRegister(REG_FIFO, 0);

    int dst = readRegister(REG_FIFO);	// Storing first byte of the received packet
    int src = readRegister(REG_FIFO);		// Reading second byte of the received packet
    int packnum = readRegister(REG_FIFO);	// Reading third byte of the received packet
    int length = readRegister(REG_FIFO);	// Reading fourth byte of the received packet
    int payloadlength = length - OFFSET_PAYLOADLENGTH;
    {
        packet_received.retry = readRegister(REG_FIFO);
        // Print the packet if debug_mode
        #if (SX1272_debug_mode > 0)
            printf("## Packet received:\n");
            printf("Destination: ");
            printf("0x%02x\n", packet_received.dst);			 	// Printing destination
            printf("Source: ");
            printf("0x%02x\n", packet_received.src);			 	// Printing source
            printf("Packet number: ");
            printf("0x%02x\n", packet_received.packnum);			// Printing packet number
            printf("Packet length: ");
            printf("0x%02x\n", packet_received.length);			// Printing packet length
            printf("Data: ");
            for(unsigned int i = 0; i < _payloadlength; i++)
            {
                printf("%c", packet_received.data[i]);		// Printing payload
            }
            printf("\n");
            printf("Retry number: ");
            printf("0x%02x\n", packet_received.retry);			// Printing number retry
            printf(" ##\n");
            printf("\n");
        #endif
        state = 0;
    }
    */
}

void dumpRegisters()
{
  //  Dump out all registers.
  for (int r = 0; r <= 0x3f; r++)
    printf("Reg[0x%X] = 0x%X\n", r, sx1272.readRegister(r));
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
  printf("receiveLoRaMessage REG_HOP_CHANNEL = 0x%02x\n", sx1272.readRegister(REG_HOP_CHANNEL));
  printf("receiveLoRaMessage REG_MODEM_CONFIG1 = 0x%02x\n", sx1272.readRegister(REG_MODEM_CONFIG1));
  printf("receiveLoRaMessage REG_MODEM_CONFIG2 = 0x%02x\n", sx1272.readRegister(REG_MODEM_CONFIG2));
#ifdef CRC_OFF
  sx1272.setCRC_OFF();
  printf("receiveLoRaMessage REG_MODEM_CONFIG1 = 0x%02x\n", sx1272.readRegister(REG_MODEM_CONFIG1));
  //dumpRegisters();
#endif  //  CRC_OFF

  my_packet[0] = 0;  //  Empty the string.
  e = sx1272.receivePacketTimeout(timeout);
  if ( e == 0 )
  {
    printf("receiveLoRaMessage: state=%d, dst=0x%02x, src=0x%02x, packnum=0x%02x, length=0x%02x\n",
        e, sx1272.packet_received.dst, sx1272.packet_received.src, sx1272.packet_received.packnum,
        sx1272.packet_received.length);
    unsigned int length = sx1272.packet_received.length;
    if (sizeof(my_packet) > 0 && length > sizeof(my_packet) - 1)
        length = sizeof(my_packet) - 1;
#ifdef TRUNCATE_MESSAGES
    if (length > 10) {
        printf("**** receiveLoRaMessage: truncated to 10 bytes\n");
        length = 10;
    }
#endif  //  TRUNCATE_MESSAGES
    unsigned int i;
    for (i = 0; i < sizeof(my_packet); i++)
      my_packet[i] = 0;
    for (i = 0; i < length; i++) {
      my_packet[i] = (char)sx1272.packet_received.data[i];
      printf("%02x ", my_packet[i]);
    }
    my_packet[i] = 0;  //  Terminate the string.
    printf("\nreceiveLoRaMessage: message=%s\n", my_packet);

    for (int j = 0; j < i; j++) {
      //  TODO: Remove non-ASCII characters.
      if (my_packet[j] == 0) break;
      if (my_packet[j] < 0x20 || my_packet[j] > 0x7f)
        my_packet[j] = '?';
    }
  }
  else {
    printf("receiveLoRaMessage: state=%d\n",e);
  }

  //  TODO: If message does not start with "{", assume it's in MessagePack format and uncompress to JSON format.
  receiveCount++;
  printf("receiveLoRaMessage: done %d, %d, %d\n", setupDone, sendCount, receiveCount);
  dumpPacket(); ////
  return (char *) my_packet;
}

int getLoRaSender()
{
  //  Return the sender address of the last packet.
  int result = sx1272.packet_received.src;
  printf("getLoRaSender: %d\n", result);
  return result;
}

int getLoRaRecipient()
{
  //  Return the recipient address of the last packet.
  int result = sx1272.packet_received.dst;
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
        //  Send message1 broadcast and print the result
        e = sendLoRaMessage(0, message1);
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
