#  This is a Python web server that handles requests to switch the Grove LED on/off, buzz the buzzer and show a message on the LCD screen.
#  Based on code from http://mattrichardson.com/Raspberry-Pi-Flask/
from flask import Flask, render_template
from grovepi import *
from grove_rgb_lcd import *
import datetime
import time

app = Flask(__name__)

# Connect the Grove LED to digital port D4
led = 4
pinMode(led, "OUTPUT")

# Connect the Grove Buzzer to digital port D8
# SIG,NC,VCC,GND
buzzer = 8
pinMode(buzzer, "OUTPUT")

# http://.../led_on will switch on the LED
@app.route("/led_on")
def led_on():
    try:
        digitalWrite(led, 1)     # Send HIGH to switch on LED
        response = "LED is now on"
    except:
        response = "There was an error switching on the LED"

    return response

# http://.../led_off will switch off the LED
@app.route("/led_off")
def led_off():
    try:
        digitalWrite(led, 0)     # Send LOW to switch off LED
        response = "LED is now off"
    except:
        response = "There was an error switching off the LED"

    return response

# http://.../buzz will buzz the buzzer
@app.route("/buzz")
def buzz():
    try:
        # Buzz for 1 second
        digitalWrite(buzzer, 1)
        time.sleep(1)

        # Stop buzzing after 1 second
        digitalWrite(buzzer, 0)
        response = "Luppy has been buzzed"
    except:
        response = "There was an error buzzing Luppy"

    return response

# http://.../lcd/msg will show msg on the LCD screen
@app.route("/lcd/<msg>")
def lcd(msg):
    try:
        # Show the message
        setText(msg)
        # Set the background to yellow
        setRGB(128, 128, 0)
        response = "'" + msg + "' is now shown on the LCD screen"
    except:
        response = "There was an error showing the message on the LCD screen"

    return response

# If no URL specified, show the date and time
@app.route("/")
def hello():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    return timeString

# Force the web browser not to cache our requests. Sometimes with caching on, the web browser may show the previous result instead of calling our server.
@app.after_request
def add_header(response):
    response.cache_control.max_age = 0
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
