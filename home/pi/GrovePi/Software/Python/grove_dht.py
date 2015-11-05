#!/usr/bin/env python

# Read the sensor data from the Grove Digital Humidity/Temperature Sensor (DHT) and display the values.
# Based on http://www.seeedstudio.com/wiki/Grove_-_Temperature_and_Humidity_Sensor

import time
import grovepi

# Connect the DHT sensor to port D2.
dht_sensor = 2

# Loop forever.
while True:
    # Get the temperature and humidity from the DHT sensor.
    [temp, hum] = grovepi.dht(dht_sensor, 0)  # 0 means we are using DHT11 as the DHT module.

    # Display the temperature and humidity.
    print("temp =", temp, "C\thumidity =", hum, "%")

    # Wait 10 seconds and repeat.
    time.sleep(10)

# Note: When calling dht(pin, module_type), change module_type to the number below depending on the DHT module used:
# DHT Module --> module_type
#   DHT11   --> 0
#   DHT22   --> 1
#   DHT21   --> 2
#   DHT2301 --> 3

