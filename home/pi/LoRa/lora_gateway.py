#!/usr/bin/env python3
# LoRa gateway for AWS IoT.  Forward messages from LoRa devices to AWS IoT, and forward AWS IoT messages to LoRa devices.
# Based on https://www.cooking-hacks.com/documentation/tutorials/extreme-range-lora-sx1272-module-shield-arduino-raspberry-pi-intel-galileo/

import time
import datetime
import ssl
import json
import paho.mqtt.client as mqtt
import lora_interface

transmission_mode = 1 # Max range, slow data rate.
transmission_channel = lora_interface.cvar.LORA_CH_10_868
transmission_power = "H"
receive_timeout = 10000

# TODO: Manage list of fields.
fields = [
    "address",
    "gateway",
    "status",
    "setup_done",
    "send_count",
    "receive_count",
    "node_snr",
    "node_rssi"
    # "node_rssi_packet"
]

# AWS IoT Device l001 to l255 <--> LoRa address 1 to 255
# AWS IoT Device l000 <--> LoRa broadcast (address 0)
# Address 1 is the LoRa Gateway
gateway_address = 1
min_device_address = 2
max_device_address = 255

# Public certificate of our Raspberry Pi, as provided by AWS IoT.
deviceCertificate = "tp-iot-certificate.pem.crt"
# Private key of our Raspberry Pi, as provided by AWS IoT.
devicePrivateKey = "tp-iot-private.pem.key"
# Root certificate to authenticate AWS IoT when we connect to their server.
awsCert = "aws-iot-rootCA.crt"

isConnected = False


# This is the main logic of the program.  We connect to AWS IoT via MQTT, send sensor data periodically to AWS IoT,
# and handle any actuation commands received from AWS IoT.
def main():
    global isConnected
    # Create an MQTT client for connecting to AWS IoT via MQTT.
    client = mqtt.Client("lora_gateway")  # Client ID must be unique because AWS will disconnect any duplicates.
    client.on_connect = on_connect  # When connected, call on_connect.
    client.on_message = on_message  # When message received, call on_message.
    client.on_log = on_log  # When logging debug messages, call on_log.

    # Set the certificates and private key for connecting to AWS IoT.  TLS 1.2 is mandatory for AWS IoT and is supported
    # only in Python 3.4 and later, compiled with OpenSSL 1.0.1 and later.
    client.tls_set(awsCert, deviceCertificate, devicePrivateKey, ssl.CERT_REQUIRED, ssl.PROTOCOL_TLSv1_2)
    # Connect to AWS IoT server.  Use AWS command line "aws iot describe-endpoint" to get the address.
    print("Connecting to AWS IoT...")
    client.connect("A1P01IYM2DOZA0.iot.us-west-2.amazonaws.com", 8883, 60)
    # Start a background thread to process the MQTT network commands concurrently, including auto-reconnection.
    client.loop_start()

    # Setup the LoRa connection.  TODO: Check status
    print("Calling setupLoRa...")
    status = lora_interface.setupLoRa(gateway_address, transmission_mode, transmission_channel, transmission_power)
    print("Status: " + str(status))
    if lora_interface.getLoRaPreambleLength() == 0:
        preamble_length = lora_interface.getLoRaPreambleLengthValue()
    else:
        preamble_length = -1
    print("Preamble Length: " + str(preamble_length))
    time.sleep(1)

    # Loop forever.
    while True:
        try:
            # If we are not connected yet to AWS IoT, wait 1 second and try again.
            if not isConnected:
                time.sleep(1)
                continue
            # Read a LoRa message, which contains the device state.  TODO: Check status.
            print("Calling receiveLoRaMessage to receive message...")
            msg0 = lora_interface.receiveLoRaMessage(receive_timeout)
            msg = msg0 # Copy the message safely.
            print("Msg: " + msg + ", Status: " + str(status))
            status = lora_interface.getLoRaStatus()
            if lora_interface.getLoRaSNR() == 0:
                gateway_snr = lora_interface.getLoRaSNRValue()
            else:
                gateway_snr = -1
            if lora_interface.getLoRaRSSI() == 0:
                gateway_rssi = lora_interface.getLoRaRSSIValue()
            else:
                gateway_rssi = -1
            if lora_interface.getLoRaRSSIpacket() == 0:
                gateway_rssi_packet = lora_interface.getLoRaRSSIpacketValue()
            else:
                gateway_rssi_packet = -1

            # TODO: Comment this section.
            #if len(msg) == 0:
                #msg = '''{
                    #"temperature": 27.3,
                    #"humidity": 88
                #}'''

            # If no message available, try again.
            if len(msg) == 0:
                continue
            device_address = lora_interface.getLoRaSender()
            recipient_address = lora_interface.getLoRaRecipient()
            device_state = {
                "gateway_snr": gateway_snr,
                "gateway_rssi": gateway_rssi,
                "gateway_rssi_packet": gateway_rssi_packet
            }
            if device_address == 3:
                # TODO: Temp logging for Arduino: Log the RSSI only
                print('Ignoring Arduino packet')
            else:
                # Msg contains an array of sensor data. Convert to dictionary.
                msg_split = msg.split("|")
                col = 0
                for value in msg_split:
                    key = fields[col]
                    col = col + 1
                    if key != "timestamp":
                        value = int(value)
                    device_state[key] = value

            # Set the timestamp if not present.
            if device_state.get("timestamp") is None:
                device_state["timestamp"] = datetime.datetime.now().isoformat()
            # Send the reported device state to AWS IoT.
            payload = {
                "state": {
                    "reported": device_state
                }
            }
            print("Sending sensor data to AWS IoT...\n" +
                  json.dumps(payload, indent=4, separators=(',', ': ')))
            # Publish our sensor data to AWS IoT via the gateway topic and the LoRa topic.
            device_topic = convert_lora_address_to_mqtt_topic(device_address)
            gateway_topic = convert_lora_address_to_mqtt_topic(gateway_address)
            client.publish(device_topic + "/shadow/update", json.dumps(payload))
            client.publish(gateway_topic + "/shadow/update", json.dumps(payload))
            print("Sent to AWS IoT")

        except KeyboardInterrupt:
            # Stop the program when we press Ctrl-C.
            break
        except Exception as e:
            # For all other errors, we wait a while and resume.
            print("Exception: " + str(e))
            time.sleep(10)
            continue

# This is called when we are connected to AWS IoT via MQTT.
# We subscribe for notifications of desired state updates.
def on_connect(client, userdata, flags, rc):
    global isConnected
    if isConnected == True:
        # Subscribe to updates only once.
        return
    isConnected = True
    print("Connected to AWS IoT")
    # Subscribe to MQTT topics for the gateway and all devices so that we will receive notifications of updates.
    gateway_topic = convert_lora_address_to_mqtt_topic(gateway_address)
    topic = gateway_topic + "/shadow/update/accepted"
    print("Subscribing to MQTT topic " + topic)
    client.subscribe(topic)
    for device_address in range(min_device_address, max_device_address + 1 ):
        device_topic = convert_lora_address_to_mqtt_topic(device_address)
        topic = device_topic + "/shadow/update/accepted"
        print("Subscribing to MQTT topic " + topic)
        client.subscribe(topic)

# This is called when we receive a subscription notification from AWS IoT.
# If this is an actuation command, we execute it.
def on_message(client, userdata, msg):
    # Convert the JSON payload to a Python dictionary.
    # The payload is in binary format so we need to decode as UTF-8.
    payload2 = json.loads(msg.payload.decode("utf-8"))
    print("Received message, topic: " + msg.topic + ", payload:\n" +
          json.dumps(payload2, indent=4, separators=(',', ': ')))
    # If there is a desired state in this message, then we send to the LoRa device.
    if payload2.get("state") is not None and payload2["state"].get("desired") is not None:
        # Get the desired state and convert to JSON.
        desired_state = payload2["state"]["desired"]
        msg = json.dumps(desired_state)
        # Send to LoRa device.
        lora_address = convert_mqtt_topic_to_lora_address(msg.topic)
        status = lora_interface.sendLoRaMessage(lora_address, msg)  # TODO: Check status.

def convert_lora_address_to_mqtt_topic(address):
    # Address contains a number like 888.  Return topic $aws/things/l888.
    topic = "$aws/things/l{:0>3}".format(address)
    return topic

def convert_mqtt_topic_to_lora_address(topic):
    # Topic is of the format $aws/things/l888/... Return 888.
    topic_split = topic.split("/")
    address2 = topic_split[2]  # "l888"
    address3 = address2[1:]  # "888"
    address4 = int(address3)  # 888
    return address4

# Print out log messages for tracing.
def on_log(client, userdata, level, buf):
    print("Log: " + buf)


# Start the main program.
main()
