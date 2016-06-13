 %module lora_interface
 %{
extern int setupLoRa(int address, int mode, unsigned int channel, string power);
extern int getLoRaStatus(void);
extern int getLoRaSetupDone(void);
extern int getLoRaSendCount(void);
extern int getLoRaReceiveCount(void);
extern int sendLoRaMessage(int address, char *msg);
extern char *receiveLoRaMessage(int timeout);
 %}

extern int setupLoRa(int address, int mode, unsigned int channel, string power);
extern int getLoRaStatus(void);
extern int getLoRaSetupDone(void);
extern int getLoRaSendCount(void);
extern int getLoRaReceiveCount(void);
extern int sendLoRaMessage(int address, char *msg);
extern char *receiveLoRaMessage(int timeout);

//FREQUENCY CHANNELS:
const uint32_t CH_10_868 = 0xD84CCC; // channel 10, central freq = 865.20MHz
const uint32_t CH_11_868 = 0xD86000; // channel 11, central freq = 865.50MHz
const uint32_t CH_12_868 = 0xD87333; // channel 12, central freq = 865.80MHz
const uint32_t CH_13_868 = 0xD88666; // channel 13, central freq = 866.10MHz
const uint32_t CH_14_868 = 0xD89999; // channel 14, central freq = 866.40MHz
const uint32_t CH_15_868 = 0xD8ACCC; // channel 15, central freq = 866.70MHz
const uint32_t CH_16_868 = 0xD8C000; // channel 16, central freq = 867.00MHz
const uint32_t CH_17_868 = 0xD90000; // channel 16, central freq = 868.00MHz
const uint32_t CH_00_900 = 0xE1C51E; // channel 00, central freq = 903.08MHz
const uint32_t CH_01_900 = 0xE24F5C; // channel 01, central freq = 905.24MHz
const uint32_t CH_02_900 = 0xE2D999; // channel 02, central freq = 907.40MHz
const uint32_t CH_03_900 = 0xE363D7; // channel 03, central freq = 909.56MHz
const uint32_t CH_04_900 = 0xE3EE14; // channel 04, central freq = 911.72MHz
const uint32_t CH_05_900 = 0xE47851; // channel 05, central freq = 913.88MHz
const uint32_t CH_06_900 = 0xE5028F; // channel 06, central freq = 916.04MHz
const uint32_t CH_07_900 = 0xE58CCC; // channel 07, central freq = 918.20MHz
const uint32_t CH_08_900 = 0xE6170A; // channel 08, central freq = 920.36MHz
const uint32_t CH_09_900 = 0xE6A147; // channel 09, central freq = 922.52MHz
const uint32_t CH_10_900 = 0xE72B85; // channel 10, central freq = 924.68MHz
const uint32_t CH_11_900 = 0xE7B5C2; // channel 11, central freq = 926.84MHz
const uint32_t CH_12_900 = 0xE4C000; // default channel 915MHz, the module is configured with it
