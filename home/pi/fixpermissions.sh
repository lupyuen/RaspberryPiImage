#!/bin/bash

##  Recursively change permissions of all files in home folder and below.
##  Called every minute by /home/pi/GrovePi/Software/Python/send_loop.sh to fix any problems caused by copying files to shared folders
echo `date` Fixing file permissions...

sudo chown pi -R /home/pi
sudo chgrp pi -R /home/pi 
echo `date` Done
