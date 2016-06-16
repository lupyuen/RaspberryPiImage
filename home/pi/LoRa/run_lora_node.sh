#!/bin/bash

cd /home/pi/LoRa
for (( ; ; ))
do
   sudo python3 test_lora_interface.py
   sleep 1
done
