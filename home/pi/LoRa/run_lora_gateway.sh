#!/bin/bash

cd /home/pi/LoRa
for (( ; ; ))
do
   sudo python3 lora_gateway.py
   sleep 1
done
