#!/usr/bin/env python3

# Blink the LED on and off every second.
# Based on GrovePi LED blink Example for the Grove LED Socket (http://www.seeedstudio.com/wiki/Grove_-_LED_Socket_Kit)

import time
import RPi.GPIO as GPIO

# Set the pin numbering to the BCM (same as GPIO) numbering format.
GPIO.setmode(GPIO.BCM)

# Assumes that we connected LED to GPIO pin 25.
led = 25

# We tell the system that GPIO pin 25 should be an output port, not input.
GPIO.setup(led, GPIO.OUT)
time.sleep(1)

# Loop forever.
while True:
    try:
        # Blink the LED
        GPIO.output(led, True)  # Output True on GPIO pin 25 to switch on LED
        time.sleep(1)  # Wait 1 second.

        GPIO.output(led, False)  # Output False on GPIO pin 25 to switch off LED
        time.sleep(1)  # Wait 1 second and repeat the loop.

    except KeyboardInterrupt:  # Turn LED off before stopping
        GPIO.output(led, False)
        break
    except IOError:  # Print "Error" if communication error encountered
        print("Error")
