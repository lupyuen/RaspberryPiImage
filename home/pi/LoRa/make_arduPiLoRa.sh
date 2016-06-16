#/bin/bash

cp -f arduPiLoRa.* ../cooking/libraries/arduPiLoRa
cd /home/pi/cooking/examples/LoRa/
rm -f /home/pi/cooking/libraries/arduPiLoRa/arduPiLoRa.o
./cook.sh


cd /home/pi/LoRa
swig -python lora_interface.i

g++ -c lora_interface.cpp lora_interface_wrap.c -I/home/pi/cooking/arduPi -I/home/pi/cooking/arduPi-api -I/home/pi/cooking/libraries/arduPiLoRa -I /usr/include/python3.4 

ld -shared -lrt -lpthread -lstdc++ -L /usr/lib/gcc/arm-linux-gnueabihf/4.9 lora_interface.o lora_interface_wrap.o /home/pi/cooking/libraries/arduPiLoRa/arduPiLoRa.o /home/pi/cooking/arduPi-api/arduPiUART.o /home/pi/cooking/arduPi-api/arduPiUtils.o /home/pi/cooking/arduPi-api/arduPiMultiprotocol.o /home/pi/cooking/arduPi/arduPi.o /usr/local/lib/libmsgpackc.a -o _lora_interface.so

sudo python3 test_lora_interface.py
