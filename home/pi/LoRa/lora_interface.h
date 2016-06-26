extern int setupLoRa(int address, int mode, uint32_t channel, char *power);
extern int getLoRaStatus(void);
extern int getLoRaSetupDone(void);
extern int getLoRaSendCount(void);
extern int getLoRaReceiveCount(void);
extern int getLoRaSNRValue(void);
extern int getLoRaRSSIValue(void);
extern int getLoRaRSSIpacketValue(void);
extern int getLoRaPreambleLengthValue(void);
extern int sendLoRaMessage(int address, char *msg);
extern char *receiveLoRaMessage(int timeout);
extern int getLoRaSender(void);
extern int getLoRaRecipient(void);
extern int getLoRaPacketNumber(void);
extern char *getLoRaPacket(void);
extern uint8_t readLoRaRegister(uint8_t register);
extern void writeLoRaRegister(uint8_t register, uint8_t value);
extern void dumpLoRaPacket(void);
extern void dumpLoRaRegisters(void);

//FREQUENCY CHANNELS:
extern uint32_t LORA_CH_10_868; // = 0xD84CCC; // channel 10, central freq = 865.20MHz
extern uint32_t LORA_CH_11_868; // = 0xD86000; // channel 11, central freq = 865.50MHz
extern uint32_t LORA_CH_12_868; // = 0xD87333; // channel 12, central freq = 865.80MHz
extern uint32_t LORA_CH_13_868; // = 0xD88666; // channel 13, central freq = 866.10MHz
extern uint32_t LORA_CH_14_868; // = 0xD89999; // channel 14, central freq = 866.40MHz
extern uint32_t LORA_CH_15_868; // = 0xD8ACCC; // channel 15, central freq = 866.70MHz
extern uint32_t LORA_CH_16_868; // = 0xD8C000; // channel 16, central freq = 867.00MHz
extern uint32_t LORA_CH_17_868; // = 0xD90000; // channel 16, central freq = 868.00MHz
extern uint32_t LORA_CH_00_900; // = 0xE1C51E; // channel 00, central freq = 903.08MHz
extern uint32_t LORA_CH_01_900; // = 0xE24F5C; // channel 01, central freq = 905.24MHz
extern uint32_t LORA_CH_02_900; // = 0xE2D999; // channel 02, central freq = 907.40MHz
extern uint32_t LORA_CH_03_900; // = 0xE363D7; // channel 03, central freq = 909.56MHz
extern uint32_t LORA_CH_04_900; // = 0xE3EE14; // channel 04, central freq = 911.72MHz
extern uint32_t LORA_CH_05_900; // = 0xE47851; // channel 05, central freq = 913.88MHz
extern uint32_t LORA_CH_06_900; // = 0xE5028F; // channel 06, central freq = 916.04MHz
extern uint32_t LORA_CH_07_900; // = 0xE58CCC; // channel 07, central freq = 918.20MHz
extern uint32_t LORA_CH_08_900; // = 0xE6170A; // channel 08, central freq = 920.36MHz
extern uint32_t LORA_CH_09_900; // = 0xE6A147; // channel 09, central freq = 922.52MHz
extern uint32_t LORA_CH_10_900; // = 0xE72B85; // channel 10, central freq = 924.68MHz
extern uint32_t LORA_CH_11_900; // = 0xE7B5C2; // channel 11, central freq = 926.84MHz
extern uint32_t LORA_CH_12_900; // = 0xE4C000; // default channel 915MHz, the module is configured with it
