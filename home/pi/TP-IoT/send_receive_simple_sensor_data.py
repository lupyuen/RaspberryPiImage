#!/usr/bin/env python

# Send DHT22 sensor data periodically to AWS IoT and process actuation commands received.

import time
import datetime
import ssl
import json
import paho.mqtt.client as mqtt
import dht22
import pigpio
import RPi.GPIO as GPIO

# TODO: Name of our Raspberry Pi, also known as our "Thing Name"
deviceName = "g88_pi"
# TODO: Public certificate of our Raspberry Pi, as provided by AWS IoT.
deviceCertificate = "5c46ea701f-certificate.pem.crt"
# TODO: Private key of our Raspberry Pi, as provided by AWS IoT.
devicePrivateKey = "5c46ea701f-private.pem.key"
# Root certificate to authenticate AWS IoT when we connect to their server.
awsCert = "aws-iot-rootCA.crt"
isConnected = False

# Assume we connected the DHT22 Sensor, YwRobot Light Sensor, L-934ID-5V LED as follows:
# DHT22/AM2302 --> Raspberry Pi:
#   +   --> GPIO 8
#   Out --> GPIO 22
#   -   --> Ground (Pin 14)
power = 8
temp_sensor = 22

# YwRobot Light Sensor --> Raspberry Pi:
#   Ground --> Ground (Pin 9)
#   VCC    --> 3.3V Power (Pin 1)
#   DOUT   --> GPIO 4
light_sensor = 4

# L-934ID-5V LED --> Raspberry Pi
#   +      --> GPIO 25
#   Ground --> Ground (Pin 20)
led = 25


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

    # Prepare the DHT22 sensor. Ensure we don't read from the DHT22 within 2 seconds, else it will eventually hang.
    dht22_sensor = dht22.Sensor(pigpio.pi(), temp_sensor, power=power)
    # Set the pin numbering to the BCM (same as GPIO) numbering format.
    GPIO.setmode(GPIO.BCM)
    # We tell the system that the LED port should be an output port, not input.
    GPIO.setup(led, GPIO.OUT)
    time.sleep(1)

    # Loop forever.
    while True:
        try:
            # If we are not connected yet to AWS IoT, wait 1 second and try again.
            if not isConnected:
                time.sleep(1)
                continue

            # Read DHT22 sensor values.  Skip if we detect an error.
            dht22_sensor.trigger()
            if dht22_sensor.bad_checksum() + dht22_sensor.short_message() + dht22_sensor.missing_message() + \
                    dht22_sensor.sensor_resets() != 0 or dht22_sensor.temperature() < 0 or dht22_sensor.humidity() < 0:
                print(("DHT22 may be connected incorrectly: temperature={:3.1f}, humidity={:3.1f}, bad_checksum={}, " +
                      "short_message={}, missing_message={}, sensor_resets={}")
                      .format(dht22_sensor.temperature(), dht22_sensor.humidity(), dht22_sensor.bad_checksum(),
                              dht22_sensor.short_message(), dht22_sensor.missing_message(),
                              dht22_sensor.sensor_resets()))
                continue

            # Prepare our sensor data in JSON format.
            payload = {
                "state": {
                    "reported": {
                        "temperature": round(dht22_sensor.temperature(), 1),
                        "humidity": round(dht22_sensor.humidity(), 1),
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
# If this is an actuation command, we execute it.
def on_message(client, userdata, msg):
    # Convert the JSON payload to a Python dictionary.
    # The payload is in binary format so we need to decode as UTF-8.
    payload2 = json.loads(msg.payload.decode("utf-8"))
    print("Received message, topic: " + msg.topic + ", payload:\n" +
          json.dumps(payload2, indent=4, separators=(',', ': ')))

    # If there is a desired state in this message, then we actuate, e.g. if we see "led=on", we switch on the LED.
    if payload2.get("state") is not None and payload2["state"].get("desired") is not None:
        # Get the desired state and loop through all attributes inside.
        desired_state = payload2["state"]["desired"]
        for attribute in desired_state:
            # We handle the attribute and desired value by actuating.
            value = desired_state.get(attribute)
            actuate(client, attribute, value)


# Control my actuators based on the specified attribute and value, e.g. "led=on" will switch on my LED.
def actuate(client, attribute, value):
    if attribute == "timestamp":
        # Ignore the timestamp attribute, it's only for info.
        return
    print("Setting " + attribute + " to " + value + "...")
    if attribute == "led":
        # We actuate the LED for "on", "off" or "flash1".
        if value == "on":
            # Switch on LED.
            GPIO.output(led, True)
            send_reported_state(client, "led", "on")
            return
        elif value == "off":
            # Switch off LED.
            GPIO.output(led, False)
            send_reported_state(client, "led", "off")
            return
        elif value == "flash1":
            # Switch on LED, wait 1 second, switch it off.
            GPIO.output(led, True)
            send_reported_state(client, "led", "on")
            time.sleep(1)

            GPIO.output(led, False)
            send_reported_state(client, "led", "off")
            time.sleep(1)
            return
    # Show an error if attribute or value are incorrect.
    print("Error: Don't know how to set " + attribute + " to " + value)


# Send the reported state of our actuator tp AWS IoT after it has been triggered, e.g. "led": "on".
def send_reported_state(client, attribute, value):
    # Prepare our sensor data in JSON format.
    payload = {
        "state": {
            "reported": {
                attribute: value,
                "timestamp": datetime.datetime.now().isoformat()
            }
        }
    }
    print("Sending sensor data to AWS IoT...\n" +
          json.dumps(payload, indent=4, separators=(',', ': ')))

    # Publish our sensor data to AWS IoT via the MQTT topic, also known as updating our "Thing Shadow".
    client.publish("$aws/things/" + deviceName + "/shadow/update", json.dumps(payload))
    print("Sent to AWS IoT")


# Print out log messages for tracing.
def on_log(client, userdata, level, buf):
    print("Log: " + buf)


# Start the main program.
main()
