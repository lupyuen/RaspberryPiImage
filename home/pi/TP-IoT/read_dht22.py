#!/usr/bin/env python3

# Read sensor data from DHT22 sensor and display the data.  Remember to start pigpiod:
# sudo pigpiod

import time
import dht22
import pigpio


# Assume we connected the DHT22 Sensor as follows:
# DHT22/AM2302 --> Raspberry Pi:
#   +   --> GPIO 8
#   Out --> GPIO 22
#   -   --> Ground (Pin 14)
power = 8
temp_sensor = 22

# Prepare the DHT22 sensor. Ensure we don't read from the DHT22 within 2 seconds, else it will eventually hang.
dht22_sensor = dht22.Sensor(pigpio.pi(), temp_sensor, power=power)

# Loop forever.
while True:
    # Read DHT22 sensor values.
    dht22_sensor.trigger()
    # Display the sensor values.
    print(("{:3.1f} {:3.1f}".format(dht22_sensor.temperature(), dht22_sensor.humidity())))
    # Wait 5 seconds before reading sensor values again.
    time.sleep(5)
