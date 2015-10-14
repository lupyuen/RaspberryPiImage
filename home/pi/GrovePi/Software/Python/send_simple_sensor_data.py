#!/usr/bin/env python

# Send sensor data from simple sensors continually to AWS IoT.
# Based on DHT22 AM2302 Python code from http://abyz.co.uk/rpi/pigpio/examples.html
# (2014-07-11 DHT22.py)

import time
import atexit
import pigpio


class sensor:
    """
    A class to read relative humidity and temperature from the
    DHT22 sensor.  The sensor is also known as the AM2302.
    The sensor can be powered from the Pi 3V3 or the Pi 5V rail.
    Powering from the 3V3 rail is simpler and safer.  You may need
    to power from 5V if the sensor is connected via a long cable.
    For 3V3 operation connect pin 1 to 3V3 and pin 4 to ground.
    Connect pin 2 to a gpio.
    For 5V operation connect pin 1 to 5V and pin 4 to ground.
    The following pin 2 connection works for me.  Use at YOUR OWN RISK.
    5V--5K_resistor--+--10K_resistor--Ground
                     |
    DHT22 pin 2 -----+
                     |
    gpio ------------+
    """

    def __init__(self, pi, gpio, LED=None, power=None):
        """
        Instantiate with the Pi and gpio to which the DHT22 output
        pin is connected.

        Optionally a LED may be specified.  This will be blinked for
        each successful reading.

        Optionally a gpio used to power the sensor may be specified.
        This gpio will be set high to power the sensor.  If the sensor
        locks it will be power cycled to restart the readings.

        Taking readings more often than about once every two seconds will
        eventually cause the DHT22 to hang.  A 3 second interval seems OK.
        """

        self.pi = pi
        self.gpio = gpio
        self.LED = LED
        self.power = power

        if power is not None:
            pi.write(power, 1)  # Switch sensor on.
            time.sleep(2)

        self.powered = True
        self.cb = None
        atexit.register(self.cancel)

        self.bad_CS = 0  # Bad checksum count.
        self.bad_SM = 0  # Short message count.
        self.bad_MM = 0  # Missing message count.
        self.bad_SR = 0  # Sensor reset count.

        # Power cycle if timeout > MAX_TIMEOUTS.
        self.no_response = 0
        self.MAX_NO_RESPONSE = 2
        self.rhum = -999
        self.temp = -999
        self.tov = None
        self.high_tick = 0
        self.bit = 40

        pi.set_pull_up_down(gpio, pigpio.PUD_OFF)
        pi.set_watchdog(gpio, 0)  # Kill any watchdogs.
        self.cb = pi.callback(gpio, pigpio.EITHER_EDGE, self._cb)

    def _cb(self, gpio, level, tick):
        """
        Accumulate the 40 data bits.  Format into 5 bytes, humidity high,
        humidity low, temperature high, temperature low, checksum.
        """
        diff = pigpio.tickDiff(self.high_tick, tick)

        if level == 0:
            # Edge length determines if bit is 1 or 0.
            if diff >= 50:
                val = 1
                if diff >= 200:  # Bad bit?
                    self.CS = 256  # Force bad checksum.
            else:
                val = 0

            if self.bit >= 40:  # Message complete.
                self.bit = 40

            elif self.bit >= 32:  # In checksum byte.
                self.CS = (self.CS << 1) + val
                if self.bit == 39:
                    # 40th bit received.
                    self.pi.set_watchdog(self.gpio, 0)
                    self.no_response = 0
                    total = self.hH + self.hL + self.tH + self.tL

                    if (total & 255) == self.CS:  # Is checksum ok?
                        self.rhum = ((self.hH << 8) + self.hL) * 0.1
                        if self.tH & 128:  # Negative temperature.
                            mult = -0.1
                            self.tH = self.tH & 127
                        else:
                            mult = 0.1

                        self.temp = ((self.tH << 8) + self.tL) * mult
                        self.tov = time.time()
                        if self.LED is not None:
                            self.pi.write(self.LED, 0)

                    else:

                        self.bad_CS += 1

            elif self.bit >= 24:  # in temp low byte
                self.tL = (self.tL << 1) + val

            elif self.bit >= 16:  # in temp high byte
                self.tH = (self.tH << 1) + val

            elif self.bit >= 8:  # in humidity low byte
                self.hL = (self.hL << 1) + val

            elif self.bit >= 0:  # in humidity high byte
                self.hH = (self.hH << 1) + val

            else:  # header bits
                pass

            self.bit += 1

        elif level == 1:
            self.high_tick = tick
            if diff > 250000:
                self.bit = -2
                self.hH = 0
                self.hL = 0
                self.tH = 0
                self.tL = 0
                self.CS = 0

        else:  # level == pigpio.TIMEOUT:
            self.pi.set_watchdog(self.gpio, 0)
            if self.bit < 8:  # Too few data bits received.
                self.bad_MM += 1  # Bump missing message count.
                self.no_response += 1
                if self.no_response > self.MAX_NO_RESPONSE:
                    self.no_response = 0
                    self.bad_SR += 1  # Bump sensor reset count.
                    if self.power is not None:
                        self.powered = False
                        self.pi.write(self.power, 0)
                        time.sleep(2)
                        self.pi.write(self.power, 1)
                        time.sleep(2)
                        self.powered = True
            elif self.bit < 39:  # Short message receieved.
                self.bad_SM += 1  # Bump short message count.
                self.no_response = 0

            else:  # Full message received.
                self.no_response = 0

    def temperature(self):
        """Return current temperature."""
        return self.temp

    def humidity(self):
        """Return current relative humidity."""
        return self.rhum

    def staleness(self):
        """Return time since measurement made."""
        if self.tov is not None:
            return time.time() - self.tov
        else:
            return -999

    def bad_checksum(self):
        """Return count of messages received with bad checksums."""
        return self.bad_CS

    def short_message(self):
        """Return count of short messages."""
        return self.bad_SM

    def missing_message(self):
        """Return count of missing messages."""
        return self.bad_MM

    def sensor_resets(self):
        """Return count of power cycles because of sensor hangs."""
        return self.bad_SR

    def trigger(self):
        """Trigger a new relative humidity and temperature reading."""
        if self.powered:
            if self.LED is not None:
                self.pi.write(self.LED, 1)

            self.pi.write(self.gpio, pigpio.LOW)
            time.sleep(0.017)  # 17 ms
            self.pi.set_mode(self.gpio, pigpio.INPUT)
            self.pi.set_watchdog(self.gpio, 200)

    def cancel(self):
        """Cancel the DHT22 sensor."""
        self.pi.set_watchdog(self.gpio, 0)
        if self.cb != None:
            self.cb.cancel()
            self.cb = None


if __name__ == "__main__":

    import time
    import pigpio
    import datetime
    import ssl
    import json
    import paho.mqtt.client as mqtt
    import send_simple_sensor_data as DHT22

    # TODO: Name of our Raspberry Pi, also known as our "Thing Name"
    deviceName = "g0_temperature_sensor"
    # TODO: Public certificate of our Raspberry Pi, as provided by AWS IoT.
    deviceCertificate = "5c46ea701f-certificate.pem.crt"
    # TODO: Private key of our Raspberry Pi, as provided by AWS IoT.
    devicePrivateKey = "5c46ea701f-private.pem.key"
    # Root certificate to authenticate AWS IoT when we connect to their server.
    awsCert = "aws-iot-rootCA.crt"
    isConnected = False

    # This is called when we are connected to AWS IoT via MQTT.
    def on_connect(client2, userdata, flags, rc):
        print("Connected to AWS IoT...")
        # Subscribe to our MQTT topic so that we will receive notifications of updates.
        client2.subscribe("$aws/things/" + deviceName + "/shadow/update")
        global isConnected
        isConnected = True


    # This is called when we receive a subscription notification from AWS IoT.
    def on_message(client2, userdata, msg):
        print(msg.topic + " " + str(msg.payload))


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

    # Intervals of about 2 seconds or less will eventually hang the DHT22.
    INTERVAL = 3
    pi = pigpio.pi()
    s = DHT22.sensor(pi, 22, LED=25, power=8)
    r = 0
    next_reading = time.time()
    # Loop forever.
    while True:
        # If we are not connected yet to AWS IoT, wait 1 second and try again.
        if not isConnected:
            time.sleep(1)
            continue

        r += 1
        s.trigger()
        time.sleep(0.2)

        # Read sensor values. Prepare our sensor data in JSON format.
        print("{} temperature={:3.1f} {:3.1f} {:3.2f} {} {} {} {}".format(
            r, s.temperature(), s.humidity(), s.staleness(),
            s.bad_checksum(), s.short_message(), s.missing_message(),
            s.sensor_resets()))
        payload = json.dumps({
            "state": {
                "reported": {
                    # "temperature": round(28.12345678, 1),
                    "temperature": round(s.temperature(), 1),
                    "timestamp": datetime.datetime.now().isoformat()
                }
            }
        })
        print("Sending sensor data to AWS IoT: ", payload)

        # Publish our sensor data to AWS IoT via the MQTT topic, also known as updating our "Thing Shadow".
        client.publish("$aws/things/" + deviceName + "/shadow/update", payload)
        print("Sent to AWS IoT")

        # Wait a while for interval before sending the next set of sensor data.
        next_reading += INTERVAL
        time.sleep(next_reading - time.time())

    s.cancel()
    pi.stop()
