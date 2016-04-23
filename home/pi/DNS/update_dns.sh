#!/bin/bash
##  This script updates the AWS DNS with the local IP address of this machine.
##  Useful for locating the Pi in a large network like TP.

cd ~/DNS
ipaddress=`ip addr | grep 'state UP' -A2 | tail -n1 | awk '{print $2}' | cut -f1  -d'/'`
hostname=`cat /etc/hostname`

cat update.template | sed s/HOSTNAME/$hostname/ | sed s/IPADDRESS/$ipaddress/ >update.json

aws route53 change-resource-record-sets --hosted-zone-id Z2ZUGCEJOR6L9D --change-batch file://update.json
