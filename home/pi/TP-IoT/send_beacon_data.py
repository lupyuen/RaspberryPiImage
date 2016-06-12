#!/usr/bin/env python3

# Send beacons detected periodically to AWS IoT.  Based on bluez library.
# Must be run with "sudo python3"

import time
import datetime
import ssl
import json
import paho.mqtt.client as mqtt
import bluetooth.ble as ble

# TODO: Change this to the name of our Raspberry Pi, also known as our "Thing Name"
deviceName = "g88pi"

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
    client = mqtt.Client(deviceName + "_sr")  # Client ID must be unique because AWS will disconnect any duplicates.
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

    # Create the beacon service for scanning beacons.
    beacon_service = ble.BeaconService()

    # Loop forever.
    while True:
        try:
            # If we are not connected yet to AWS IoT, wait 1 second and try again.
            if not isConnected:
                time.sleep(1)
                continue

            # Scan for beacons and add to the sensor data payload.
            beacons = {}
            beacons_detected = beacon_service.scan(2)
            for beacon_address, beacon_info in list(beacons_detected.items()):
                # For each beacon found, add to the payload. Need to flip the bytes.
                beacon = {
                    "uuid": beacon_info[0].replace('-', ''),
                    "major": (beacon_info[1] % 256) * 256 + beacon_info[1] // 256,
                    "minor": (beacon_info[2] % 256) * 256 + beacon_info[2] // 256,
                    "power": beacon_info[3],
                    "rssi": beacon_info[4],
                    "address": beacon_address
                }
                # Beacon ID is B_(uuid)_(major)_(minor). This format allows us
                # to match beacon IDs within IoT rules. Prepad major and minor
                # with 0s to max length, so that we can slice beacons by fixed
                # length in IoT rules. Sample beacon ID:
                # "B_b9407f30f5f8466eaff925556b57fe6d_00602_29434"
                beacon_id = "B_" + beacon["uuid"] + "_" + \
                            str(beacon["major"]).rjust(5, '0') + "_" + \
                            str(beacon["minor"]).rjust(5, '0')
                beacon["id"] = beacon_id
                beacons[beacon_id] = beacon

            # Prepare our sensor data in JSON format.
            payload = {
                "state": {
                    "reported": {
                        "beacons": beacons,
                        "timestamp": datetime.datetime.now().isoformat()
                    }
                }
            }

            print("Sending sensor data to AWS IoT...\n" +
                  json.dumps(payload, indent=4, separators=(',', ': ')))

            # Publish our sensor data to AWS IoT via the MQTT topic, also known as updating our "Thing Shadow".
            client.publish("$aws/things/" + deviceName + "/shadow/update", json.dumps(payload))
            print("Sent to AWS IoT")

            # Wait 30 seconds before sending the next set of sensor data.
            time.sleep(30)

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
    isConnected = True
    print("Connected to AWS IoT")
    # Subscribe to our MQTT topic so that we will receive notifications of updates.
    topic = "$aws/things/" + deviceName + "/shadow/update/accepted"
    print("Subscribing to MQTT topic " + topic)
    client.subscribe(topic)


# This is called when we receive a subscription notification from AWS IoT.
def on_message(client, userdata, msg):
    # Convert the JSON payload to a Python dictionary.
    # The payload is in binary format so we need to decode as UTF-8.
    payload2 = json.loads(msg.payload.decode("utf-8"))
    print("Received message, topic: " + msg.topic + ", payload:\n" +
          json.dumps(payload2, indent=4, separators=(',', ': ')))


# Print out log messages for tracing.
def on_log(client, userdata, level, buf):
    print("Log: " + buf)


# Start the main program.
main()
