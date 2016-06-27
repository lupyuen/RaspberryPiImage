#!/bin/bash
# Kill the lora_gateway shell script and Python program

ps aux | grep lora_gateway | grep -v grep
sudo pkill -f lora_gateway
ps aux | grep lora_gateway | grep -v grep

