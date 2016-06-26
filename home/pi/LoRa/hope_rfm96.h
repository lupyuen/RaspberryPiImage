//  Derived from Hope RF sample code at http://www.hoperf.com/design_guides/785.html

//RFM96 Internal registers Address
const int REG_RegFifo                                  = 0x00;
// Common settings
const int REG_RegOpMode                                = 0x01;
const int REG_RegFrMsb                                 = 0x06;
const int REG_RegFrMid                                 = 0x07;
const int REG_RegFrLsb                                 = 0x08;
// Tx settings
const int REG_RegPaConfig                              = 0x09;
const int REG_RegPaRamp                                = 0x0A;
const int REG_RegOcp                                   = 0x0B;
// Rx settings
const int REG_RegLna                                   = 0x0C;
// LoRa registers
const int REG_RegFifoAddrPtr                           = 0x0D;
const int REG_RegFifoTxBaseAddr                        = 0x0E;
const int REG_RegFifoRxBaseAddr                        = 0x0F;
const int REG_RegFifoRxCurrentaddr                     = 0x10;
const int REG_RegIrqFlagsMask                          = 0x11;
const int REG_RegIrqFlags                              = 0x12;
const int REG_RegRxNbBytes                             = 0x13;
const int REG_RegRxHeaderCntValueMsb                   = 0x14;
const int REG_RegRxHeaderCntValueLsb                   = 0x15;
const int REG_RegRxPacketCntValueMsb                   = 0x16;
const int REG_RegRxPacketCntValueLsb                   = 0x17;
const int REG_RegModemStat                             = 0x18;
const int REG_RegPktSnrValue                           = 0x19;
const int REG_RegPktRssiValue                          = 0x1A;
const int REG_RegRssiValue                             = 0x1B;
const int REG_RegHopChannel                            = 0x1C;
const int REG_RegModemConfig1                          = 0x1D;
const int REG_RegModemConfig2                          = 0x1E;
const int REG_RegSymbTimeoutLsb                        = 0x1F;
const int REG_RegPreambleMsb                           = 0x20;
const int REG_RegPreambleLsb                           = 0x21;
const int REG_RegPayloadLength                         = 0x22;
const int REG_RegMaxPayloadLength                      = 0x23;
const int REG_RegHopPeriod                             = 0x24;
const int REG_RegFifoRxByteAddr                        = 0x25;
const int REG_RegModemConfig3                          = 0x26;

// I/O settings
const int REG_DIOMAPPING1                          = 0x40;
const int REG_DIOMAPPING2                          = 0x41;
// Version
const int REG_VERSION0                              = 0x42;
// Additional settings
const int REG_PLLHOP                               = 0x44;
const int REG_TCXO0                                 = 0x4B;
const int REG_PADAC                                = 0x4D;
const int REG_FORMERTEMP                           = 0x5B;

const int REG_AGCREF                               = 0x61;
const int REG_AGCTHRESH1                           = 0x62;
const int REG_AGCTHRESH2                           = 0x63;
const int REG_AGCTHRESH3                           = 0x64;
