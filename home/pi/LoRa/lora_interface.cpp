//  Interface to send and receive LoRa messages, exposing a Python wrapper via Swig.
//  We compress JSON messages with MessagePack to reduce transmitted message size.
//  Semtech SX1272 Datasheet: http://www.semtech.com/images/datasheet/sx1272.pdf

#include <msgpack.h>
#include <stdio.h>
#include "arduPiLoRa.h"  //  Include the SX1272 and SPI library.
#include "lora_interface.h"
char *decodeChannel(uint32_t code);

int e;
char my_packet[1024];
char message1 [] = "Packet 1, wanting to see if received packet is the same as sent packet";
char message2 [] = "Packet 2, broadcast test";

////
static int setupDone = 0;
static int sendCount = 0;
static int receiveCount = 0;

//  MessagePack buffer and serializer instance.
msgpack_sbuffer* buffer = NULL;
msgpack_packer* pk = NULL;

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
  //  Test MessagePack. Create MessagePack buffer and serializer instance.
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

  // Print a start message
  printf("setupLoRa: SX1272 module and Raspberry Pi: send packets without ACK\n");
  
  // Power ON the module
  e = sx1272.ON();
  printf("setupLoRa: Setting power ON: state %d\n", e);
  
  // Set transmission mode
  e = sx1272.setMode(mode);
  printf("setupLoRa: Setting Mode %d: state %d\n", mode, e);
  
  // Set header
  e = sx1272.setHeaderON();
  printf("setupLoRa: Setting Header ON: state %d\n", e);
  //e = sx1272.setHeaderOFF();  ////  TODO
  //printf("****setupLoRa: Setting Header OFF: state %d\n", e);

  // Select frequency channel
  e = sx1272.setChannel(channel);
  printf("setupLoRa: Setting Channel %s: state %d\n", decodeChannel(channel), e);
  
  // Set CRC
  ////e = sx1272.setCRC_ON();
  ////printf("setupLoRa: Setting CRC ON: state %d\n", e);
  e = sx1272.setCRC_OFF();  ////  TODO
  printf("setupLoRa: Setting CRC OFF: state %d\n", e);

  // Select output power (Max, High or Low)
  e = sx1272.setPower(*power);
  printf("setupLoRa: Setting Power %s: state %d\n", power, e);
  
  // Set the node address
  e = sx1272.setNodeAddress(address);
  printf("setupLoRa: Setting Node address %d: state %d\n", address, e);
  
  // Print a success message
  printf("setupLoRa: SX1272 successfully configured\n\n");

  ////
  setupDone++;
  printf("setupLoRa: done %d, %d, %d\n", setupDone, sendCount, receiveCount);
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

    ////
    sendCount++;
    printf("sendLoRaMessage: done %d, %d, %d\n", setupDone, sendCount, receiveCount);
    return e;
}

char *receiveLoRaMessage(int timeout)
{
  // Receive message. Wait till timeout, in milliseconds.
  printf("receiveLoRaMessage: start\n");
  if (setupDone == 0)
  {
    printf("receiveLoRaMessage ERROR: setupLoRa not called");
    return (char *) "ERROR";
  }
  printf("receiveLoRaMessage REG_HOP_CHANNEL = 0x%02x\n", sx1272.readRegister(REG_HOP_CHANNEL));
  printf("receiveLoRaMessage REG_MODEM_CONFIG1 = 0x%02x\n", sx1272.readRegister(REG_MODEM_CONFIG1));
  printf("receiveLoRaMessage REG_MODEM_CONFIG2 = 0x%02x\n", sx1272.readRegister(REG_MODEM_CONFIG2));
  //for (int r = 0; r <= 0x3f; r++) printf("Reg[0x%X] = 0x%X\n", r, sx1272.readRegister(r));

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
    if (length > 10) {
        printf("***truncated to 10 bytes\n");
        length = 10;
    }

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

  ////
  //  TODO: If message does not start with "{", assume it's in MessagePack format and uncompress to JSON format.
  receiveCount++;
  printf("receiveLoRaMessage: done %d, %d, %d\n", setupDone, sendCount, receiveCount);
  return my_packet;
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

int main() {
    const int address = 2;
    const int mode = 4;
    unsigned int channel = LORA_CH_10_868;
    char *power = (char *) "H";
    int setupStatus = setupLoRa(address, mode, channel, power);
    printf("Setup status %d\n",setupStatus);
    delay(1000);
	while(1) {
        // Send message1 to address 8 and print the result
        e = sendLoRaMessage(8, message1);
        printf("Packet sent, state %d\n",e);
        delay(4000);

        // Send message2 broadcast and print the result
        e = sendLoRaMessage(0, message2);
        printf("Packet sent, state %d\n",e);

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
