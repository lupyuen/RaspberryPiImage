#!/usr/bin/env python
# grovepi_lcd_dht.py
# From http://www.seeedstudio.com/wiki/Grove_-_Temperature_and_Humidity_Sensor

# dht(pin,module_type), change module_type number to use other kind of dht
# module_type:
#             DHT11 0
#             DHT22 1
#             DHT21 2
#             DHT2301 3

from grovepi import *
import time

dht_sensor_port = 2  # Connect the DHt sensor to port D2

while True:
    [temp, hum] = dht(dht_sensor_port, 0)  # Get the temperature and Humidity from the DHT sensor
    print("temp =", temp, "C\thumidity =", hum, "%")
    t = str(temp)
    h = str(hum)
    time.sleep(10)

