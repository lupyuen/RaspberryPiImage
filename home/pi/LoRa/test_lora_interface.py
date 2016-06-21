#!/usr/bin/env python3
# This test program sends the send/receive counters and timestamp to the LoRa gateway in a loop.

import time
import datetime
import json
import platform
import lora_interface

#transmission_mode = 1 # Max range, slow data rate.
transmission_mode = 5 # Better reach, medium time on air. Test this mode because it doesn't mandate Low Data Rate Optimisation, which is not supported on Hope RF95.
transmission_channel = lora_interface.cvar.LORA_CH_10_868
transmission_power = "H"
receive_timeout = 10000
loop_delay = 10

device_address = 2  # My own address.
gateway_address = 1  # Address of gateway.

print("Calling setupLoRa...")
status = lora_interface.setupLoRa(device_address, transmission_mode, transmission_channel, transmission_power)
print("Status: " + str(status))

# Loop forever.
while True:
    try:
        # Wait a while to receive a message.
        print("Calling receiveLoRaMessage to receive message...")
        msg = lora_interface.receiveLoRaMessage(receive_timeout)
        status = lora_interface.getLoRaStatus()
        print("Msg: " + msg + ", Status: " + str(status))

        # Read the LoRa counters.
        status = lora_interface.getLoRaStatus()
        setup_done = lora_interface.getLoRaSetupDone()
        send_count = lora_interface.getLoRaSendCount()
        receive_count = lora_interface.getLoRaReceiveCount()
        snr = lora_interface.getLoRaSNR()
        rssi = lora_interface.getLoRaRSSI()
        rssi_packet = lora_interface.getLoRaRSSIpacket()
        timestamp = datetime.datetime.now().isoformat()

        msg = str(device_address) + "|" + \
              str(gateway_address) + "|" + \
              str(status) + "|" + \
              str(setup_done) + "|" + \
              str(send_count) + "|" + \
              str(receive_count) + "|" + \
              str(snr) + "|" + \
              str(rssi) + "|" + \
              str(rssi_packet) + "|" + \
              str(timestamp)
        print("Calling sendLoRaMessage to send device state to LoRa gateway " + str(gateway_address) + "...\n" + msg)
        status = lora_interface.sendLoRaMessage(gateway_address, msg)
        print("Status: " + str(status))

        # Wait 10 seconds before sending the next message.
        time.sleep(loop_delay)

    except KeyboardInterrupt:
        # Stop the program when we press Ctrl-C.
        break
    except Exception as e:
        # For all other errors, we wait a while and resume.
        print("Exception: " + str(e))
        time.sleep(10)
        continue
