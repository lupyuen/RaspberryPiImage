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

# Sensor data message from sensor nodes must follow this sequence of sensor data, delimited by "|".
# e.g. "28.1|72||OK".  We may skip fields by sending "||".
# TODO: Manage this list of fields.
fields = [
    "temperature",
    "humidity",
    "light_level",
    "message"
]

# AWS IoT Device l001 to l255 <--> LoRa address 1 to 255
# AWS IoT Device l000 <--> LoRa broadcast (address 0)
# Address 1 is the LoRa Gateway
gateway_address = 1
min_device_address = 2
max_device_address = 255
last_heartbeat = datetime.datetime.min  # Last time we sent a heartbeat message to AWS.

# Public certificate of our Raspberry Pi, as provided by AWS IoT.
deviceCertificate = "tp-iot-certificate.pem.crt"
# Private key of our Raspberry Pi, as provided by AWS IoT.
devicePrivateKey = "tp-iot-private.pem.key"
# Root certificate to authenticate AWS IoT when we connect to their server.
awsCert = "aws-iot-rootCA.crt"

# Set to true when we are connected to AWS MQTT.
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
    preamble_length = lora_interface.getLoRaPreambleLengthValue()
    print("Preamble Length: " + str(preamble_length))
    time.sleep(1)

    # Loop forever.
    while True:
        try:
            # If we are not connected yet to AWS IoT, wait 1 second and try again.
            if not isConnected:
                time.sleep(1)
                continue
            # Attempt to read 1 message from LoRa.
            device_state = read_lora_message()
            # If no message available, try again.
            if device_state is None:
                continue

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
            device_topic = convert_lora_address_to_mqtt_topic(device_state["address"])
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

# Read a LoRa message, parse into device state and return the device state.  TODO: Check status.
def read_lora_message():
    global last_heartbeat
    print("Calling receiveLoRaMessage to receive message...")
    msg0 = lora_interface.receiveLoRaMessage(receive_timeout)
    msg = msg0  # Copy the message safely.
    status = lora_interface.getLoRaStatus()
    print("Msg: " + msg + ", Status: " + str(status))
    write_packet()
    gateway_snr = lora_interface.getLoRaSNRValue()
    gateway_rssi = lora_interface.getLoRaRSSIValue()
    gateway_rssi_packet = lora_interface.getLoRaRSSIpacketValue()

    # If no message available, try again.
    if len(msg) == 0:
        # Send a heartbeat message if it was last sent 10 mins ago.
        if (datetime.datetime.now() - last_heartbeat).total_seconds() < 10 * 60:
            return None
        last_heartbeat = datetime.datetime.now()
        device_state = {
            "message": "heartbeat",
            "address": gateway_address,
            "gateway": gateway_address,
            "gateway_snr": gateway_snr,
            "gateway_rssi": gateway_rssi,
            "gateway_rssi_packet": gateway_rssi_packet
        }
        return device_state

    device_address = lora_interface.getLoRaSender()
    recipient_address = lora_interface.getLoRaRecipient()
    packet_number = lora_interface.getLoRaPacketNumber()
    device_state = {
        "address": device_address,
        "gateway": recipient_address,
        "packet_number": packet_number,
        "gateway_snr": gateway_snr,
        "gateway_rssi": gateway_rssi,
        "gateway_rssi_packet": gateway_rssi_packet
    }
    try:
        # Msg contains an array of sensor data. Convert to dictionary.
        msg_split = msg.split("|")
        col = 0
        for value in msg_split:
            key = fields[col]
            col = col + 1
            value = value.strip()
            if value == "": continue  # Allow "||" to denote skipping of fields.

            # If field is integer or decimal, convert accordingly.
            if key != "timestamp" and value.isdecimal():
                if '.' in value: value = float(value)
                else: value = int(value)
            device_state[key] = value
    except Exception as e:
        # In case of parse errors e.g. due to Low Data Rate Optimization, record the error and continue.
        device_state["error"] = str(e)
    return device_state

# Write the received packet to a local file.
def write_packet():
    with open('lora_gateway.log', 'a') as out:
        packet = lora_interface.getLoRaPacket()
        out.write(datetime.datetime.now().isoformat() + '|' + packet + '\n')

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
