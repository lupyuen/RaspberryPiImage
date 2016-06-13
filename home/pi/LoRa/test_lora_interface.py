#!/usr/bin/env python3
# This test program sends the send/receive counters and timestamp to the LoRa gateway in a loop.

import time
import datetime
import json
import lora_interface

gateway = 1
receive_timeout = 10000

print("Calling setupLoRa...")
address = 2
mode = 4
channel = lora_interface.cvar.LORA_CH_10_868
power = "H"
status = lora_interface.setupLoRa(address, mode, channel, power)
print("Status: " + str(status))

# Loop forever.
while True:
    try:
        # Read the LoRa counters.
        status = lora_interface.getLoRaStatus()
        setup_done = lora_interface.getLoRaSetupDone()
        send_count = lora_interface.getLoRaSendCount()
        receive_count = lora_interface.getLoRaReceiveCount()

        # Send the device state to the LoRa gateway.
        state = {
            "status": status,
            "setup_done": setup_done,
            "send_count": send_count,
            "receive_count": receive_count,
            "timestamp": datetime.datetime.now().isoformat()
        }
        print("Calling sendLoRaMessage to send device state to LoRa gateway " + str(gateway) + "...\n" +
              json.dumps(state, indent=4, separators=(',', ': ')))
        msg = json.dumps(state)
        status = lora_interface.sendLoRaMessage(gateway, msg)
        print("Status: " + str(status))

        # Wait a while to receive a message.
        print("Calling receiveLoRaMessage to receive message...")
        msg = lora_interface.receiveLoRaMessage(receive_timeout)
        status = lora_interface.getLoRaStatus()
        print("Msg: " + msg + ", Status: " + str(status))

        # Wait 30 seconds before sending the next message.
        time.sleep(20)

    except KeyboardInterrupt:
        # Stop the program when we press Ctrl-C.
        break
    except Exception as e:
        # For all other errors, we wait a while and resume.
        print("Exception: " + str(e))
        time.sleep(10)
        continue
