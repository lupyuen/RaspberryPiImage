#!/usr/bin/env python
#
# GrovePi Example for using the Grove Encoder(http://www.seeedstudio.com/depot/Grove-Encoder-p-1352.html) with the GrovePi
#
# The GrovePi connects the Raspberry Pi and Grove sensors.  You can learn more about GrovePi here:  http://www.dexterindustries.com/GrovePi
#
# Have a question about this example?  Ask on the forums here:  http://www.dexterindustries.com/forum/?forum=grovepi
#
'''
## License

The MIT License (MIT)

GrovePi for the Raspberry Pi: an open source platform for connecting Grove Sensors to the Raspberry Pi.
Copyright (C) 2015  Dexter Industries

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''

# USAGE
#
# Connect the grove encoder to D2 on the GrovePi.
# You can send'run_in_bk=1' as a parameter, e.g. grovepi.encoderRead(run_in_bk=1) to run the encoder code in the background on the GrovePi. This allows you to use other functions such as digitalRead to run with the encoder read running in the background
#
# the fist byte is 1 for a new value and 0 for old values
# second byte is encoder positon from 1 to 24

import time
import grovepi

print "Reading from the encoder"
while True:
    try:
		[new_val,encoder_val] = grovepi.encoderRead(run_in_bk=1)
		if new_val:
			print encoder_val
		time.sleep(.5) 

    except IOError:
        print ("Error")
