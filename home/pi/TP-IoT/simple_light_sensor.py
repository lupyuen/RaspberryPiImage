#!/usr/bin/env python3

# Read the light sensor values.
# Based on GrovePi Example for using the Grove Button (http://www.seeedstudio.com/wiki/Grove_-_Button)
# Refer to https://www.raspberrypi.org/forums/viewtopic.php?f=28&t=107058&p=739228

import time
import RPi.GPIO as GPIO

# Set the pin numbering to the BCM (same as GPIO) numbering format.
GPIO.setmode(GPIO.BCM)

# Assumes that we connected the light sensor to GPIO pin 3.
lightSensor = 3

# We tell the system that the GPIO pin for the light sensor should
# be an input port, not output.
GPIO.setup(lightSensor, GPIO.IN)
time.sleep(1)

# Loop forever.
while True:
    try:
        # Read the light level and display it.
        lightLevel = GPIO.input(lightSensor)
        print("light level = {}".format(lightLevel))

        # Wait 1 second and repeat the loop.
        time.sleep(1)

    except IOError:  # Print "Error" if communication error encountered
        print("Error")
