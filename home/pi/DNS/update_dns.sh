#!/bin/bash

# This script updates the AWS DNS with the local IP address of this machine.
# Useful for locating the Pi in a large network like TP.  This script is
# called by cron every minute.

# Get the IP address and hostname.
ipaddress=`ip addr | grep 'state UP' -A2 | tail -n1 | awk '{print $2}' | cut -f1  -d'/'`
hostname=`cat /etc/hostname`
request={"hostname":"$hostname","ip":"$ipaddress"}

# Invoke AWS API Gateway to call Lambda function UpdateDNS.
echo curl -H "Content-Type: application/json" -X POST -d ${request} \
https://vldi2nta91.execute-api.us-west-2.amazonaws.com/prod/UpdateDNS

curl -H "Content-Type: application/json" -X POST -d ${request} \
https://vldi2nta91.execute-api.us-west-2.amazonaws.com/prod/UpdateDNS
