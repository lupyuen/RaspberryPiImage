extern uint8_t readDraginoRegister(uint8_t addr);
extern void writeDraginoRegister(uint8_t addr, uint8_t value);
extern int setupDraginoLoRa(int address, int mode, uint32_t channel, char *power);
extern int receiveDraginoPacket();
