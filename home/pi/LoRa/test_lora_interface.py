#!/usr/bin/env python3
# This test program sends the send/receive counters and timestamp to the LoRa gateway in a loop.

import time
import datetime
import json
import platform
import lora_interface

gateway = 1
address = 2
mode = 1 # Max range, slow data rate.
#mode = 4 # Mid range, mid data rate.
channel = lora_interface.cvar.LORA_CH_10_868
power = "H"
receive_timeout = 10000
loop_delay = 10

is_gateway = False  # Run as sensor node.
if platform.node() == "g87pi":
    is_gateway = True  # Run as gateway.
    address = gateway
    print(platform.node() + " RUNNING AS GATEWAY")

print("Calling setupLoRa...")
status = lora_interface.setupLoRa(address, mode, channel, power)
print("Status: " + str(status))

# Loop forever.
while True:
    try:
        # Wait a while to receive a message.
        print("Calling receiveLoRaMessage to receive message...")
        msg = lora_interface.receiveLoRaMessage(receive_timeout)
        status = lora_interface.getLoRaStatus()
        print("Msg: " + msg + ", Status: " + str(status))

        # Don't send data if this is gateway.
        if is_gateway: continue

        # Read the LoRa counters.
        status = lora_interface.getLoRaStatus()
        setup_done = lora_interface.getLoRaSetupDone()
        send_count = lora_interface.getLoRaSendCount()
        receive_count = lora_interface.getLoRaReceiveCount()
        snr = lora_interface.getLoRaSNR()
        rssi = lora_interface.getLoRaRSSI()
        rssi_packet = lora_interface.getLoRaRSSIpacket()
        timestamp = datetime.datetime.now().isoformat()

        # If this is the sensor node, send the device state to the LoRa gateway.
        state = {
            "address": address,
            "gateway": gateway,
            "status": status,
            "setup_done": setup_done,
            "send_count": send_count,
            "receive_count": receive_count,
            "snr": snr,
            "rssi": rssi,
            "rssi_packet": rssi_packet,
            "timestamp": datetime.datetime.now().isoformat()
        }
        print("Calling sendLoRaMessage to send device state to LoRa gateway " + str(gateway) + "...\n" +
              json.dumps(state, indent=4, separators=(',', ': ')))
        msg = json.dumps(state)
        '''
        msg = str(address) + "|" + \
              str(gateway) + "|" + \
              str(status) + "|" + \
              str(setup_done) + "|" + \
              str(send_count) + "|" + \
              str(receive_count) + "|" + \
              str(snr) + "|" + \
              str(rssi) + "|" + \
              str(rssi_packet) + "|" + \
              str(timestamp)
        print("Calling sendLoRaMessage to send device state to LoRa gateway " + str(gateway) + "...\n" + msg)
        '''
        status = lora_interface.sendLoRaMessage(gateway, msg)
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
