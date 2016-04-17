#!/bin/bash
##  This script is run during Pi startup.  Don't use ~ because the script runs in the root context.
##  Change to the directory containing our scripts.
cd /home/pi/GrovePi/Software/Python/

##  Start the Python web server and wait a while for the web server to start up before starting the HTTP tunnel.
##sudo python server.py &
##sleep 10

##  Start the TCP tunnel for SSH and HTTP tunnel for remote web access to our web server.
##./ngrok http --log "stdout" -config=/home/pi/.ngrok2/ngrok.yml --subdomain=luppypi 80 &
##./ngrok tcp --log "stdout" -config=/home/pi/.ngrok2/ngrok.yml --remote-addr=1.tcp.ngrok.io:20400 22 &

##  Send sensor data in a loop.  Put it in the background so the script can continue.
##python send_sensor_data.py &

##  Loop forever.
for (( ; ; ))
do
    ##  Fix the filesystem permissions when files are copied via network file share.
	/home/pi/fixpermissions.sh
	##  Wait 1 minute and redo the loop.
	sleep 60
done
