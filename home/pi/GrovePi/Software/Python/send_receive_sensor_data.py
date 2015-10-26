#!/usr/bin/env python

# Send sensor data continually to AWS IoT and process commands received.
# Based on GrovePi Example for using the Grove Temperature Sensor
# (http://www.seeedstudio.com/wiki/Grove_-_Temperature_Sensor)

import time
import grovepi
import datetime
import ssl
import json
import paho.mqtt.client as mqtt

# TODO: Name of our Raspberry Pi, also known as our "Thing Name"
deviceName = "g88_pi"
# TODO: Public certificate of our Raspberry Pi, as provided by AWS IoT.
deviceCertificate = "5c46ea701f-certificate.pem.crt"
# TODO: Private key of our Raspberry Pi, as provided by AWS IoT.
devicePrivateKey = "5c46ea701f-private.pem.key"
# Root certificate to authenticate AWS IoT when we connect to their server.
awsCert = "aws-iot-rootCA.crt"

# Assume we connected the Grove Light Sensor to analog port A0,
# Temperature Sensor to A1, Sound Sensor to A2.
light_sensor = 0
temp_sensor = 1
sound_sensor = 2
isConnected = False

# Connect the Grove LED to digital port D4
led = 4
grovepi.pinMode(led, "OUTPUT")
time.sleep(1)


# Control my actuators based on the specified attribute and value, e.g. "led=on" will switch on my LED.
def actuate(attribute, value):
    if attribute == "timestamp":
        # Ignore the timestamp attribute, it's only for info.
        return
    print("Setting " + attribute + " to " + value + "...")
    if attribute == "led":
        # We actuate the LED for "on", "off" or "flash1".
        if value == "on":
            # Switch on LED.
            grovepi.digitalWrite(led, 1)
        elif value == "off":
            # Switch off LED.
            grovepi.digitalWrite(led, 0)
        elif value == "flash1":
            # Switch on LED, wait 1 second, switch it off.
            grovepi.digitalWrite(led, 1)
            time.sleep(1)
            grovepi.digitalWrite(led, 0)
            time.sleep(1)


# This is called when we are connected to AWS IoT via MQTT.
def on_connect(client2, userdata, flags, rc):
    print("Connected to AWS IoT")
    global isConnected
    isConnected = True
    # Subscribe to our MQTT topic so that we will receive notifications of updates.
    topic = "$aws/things/" + deviceName + "/shadow/update/accepted"
    print("Subscribing to MQTT topic " + topic)
    client2.subscribe(topic)


# This is called when we receive a subscription notification from AWS IoT.
def on_message(client2, userdata, msg):
    # Convert the JSON payload to a Python dictionary.
    # The payload is in binary format so we need to decode as UTF-8.
    payload2 = json.loads(msg.payload.decode("utf-8"))
    print("Received message, topic: " + msg.topic + ", payload:\n" +
          json.dumps(payload2, indent=4, separators=(',', ': ')))
    # If there is a desired state in this message, then we actuate, e.g. if we see "led=on", we switch on the LED.
    if payload2.get("state") is not None and payload2["state"].get("desired") is not None:
        # Get the desired state and loop through all attributes inside.
        desiredState = payload2["state"]["desired"]
        for attribute in desiredState:
            # We handle the attribute and desired value by actuating.
            value = desiredState.get(attribute)
            actuate(attribute, value)


# Print out log messages for tracing.
def on_log(client2, userdata, level, buf):
    print("Log: " + buf)


# Create an MQTT client for connecting to AWS IoT via MQTT.
client = mqtt.Client("awsiot")
client.on_connect = on_connect
client.on_message = on_message
client.on_log = on_log

# Set the certificates and private key for connecting to AWS IoT.  TLS 1.2 is mandatory for AWS IoT and is supported
# only in Python 3.4 and later, compiled with OpenSSL 1.0.1 and later.
client.tls_set(awsCert, deviceCertificate, devicePrivateKey, ssl.CERT_REQUIRED, ssl.PROTOCOL_TLSv1_2)

# Connect to AWS IoT server.  Use AWS command line "aws iot describe-endpoint" to get the address.
print("Connecting to AWS IoT...")
client.connect("A1P01IYM2DOZA0.iot.us-west-2.amazonaws.com", 8883, 60)

# Start a background thread to process the MQTT network commands concurrently, including auto-reconnection.
client.loop_start()

# Loop forever.
while True:
    try:
        # If we are not connected yet to AWS IoT, wait 1 second and try again.
        if not isConnected:
            time.sleep(1)
            continue

        # Read sensor values. Prepare our sensor data in JSON format.
        payload = {
            "state": {
                "reported": {
                    # "temperature": round(29.1, 1),
                    "temperature": round(grovepi.temp(temp_sensor, '1.1'), 1),
                    "light_level": grovepi.analogRead(light_sensor),
                    "sound_level": grovepi.analogRead(sound_sensor),
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
        break
    except IOError:
        print("Error")
