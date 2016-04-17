#!/usr/bin/env python
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

import time
import grovepi
import datetime
from temboo.Library.Google.Spreadsheets import AddListRows
from temboo.core.session import TembooSession

# Connect the Grove Button to digital port D3
# SIG,NC,VCC,GND
button = 3

lastState = 0

while True:
    try:
        # Get the current timestamp.
        now = datetime.datetime.now()
        timestamp = str(now)

        # Get button state, which should be either 0 (released) or 1 (pressed).
        state = grovepi.digitalRead(button)

        # Ignore state 255, which may be a read conflict with send_sensor_data.py.
        if state == 255:
            continue

        # Show the state for debugging.
        #print ("state=", state)

        # If state has changed, send the state to Google Spreadsheet through Temboo.
        if state != lastState:
            lastState = state
            if state == 0:
                stateText = "Released"
            else:
                stateText = "Pressed"
            print ("Sending stateText=", stateText)

            # Send the state to the Google Spreadsheet through Temboo.
            # Create a session with your Temboo account details
            session = TembooSession("lupyuen", "myFirstApp", "2e0421546ea248d4a5cd2029f2979e23")

            # Instantiate the Choreo
            addListRowsChoreo = AddListRows(session)

            # Get an InputSet object for the Choreo
            addListRowsInputs = addListRowsChoreo.new_input_set()

            # Set credential to use for execution
            addListRowsInputs.set_credential('SensorData')

            # Set the data to be added
            addListRowsInputs.set_RowsetXML("""
            <rowset>
            <row>
            <Timestamp>{0}</Timestamp>
            <Button>{1}</Button>
            </row>
            </rowset>
            """.format(timestamp, stateText))

            # Execute the Choreo
            addListRowsResults = addListRowsChoreo.execute_with_results(addListRowsInputs)

            # Print the Choreo outputs
            print("Response: " + addListRowsResults.get_Response())
            print("NewAccessToken: " + addListRowsResults.get_NewAccessToken())
        else:
            time.sleep(.5)

    except KeyboardInterrupt:
        break
    except IOError:
        print ("Error")


