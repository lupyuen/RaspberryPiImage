#!/usr/bin/env bash

# This script looks for SSID config files written by set_wifi_password and updates the wifi config.

shopt -s nullglob
FILES=/boot/pending_wifi_config_*
for f in $FILES
do
  echo "Processing $f..."
  python3 update_wifi_config.py $f
done
