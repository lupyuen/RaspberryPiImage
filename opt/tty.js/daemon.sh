#!/bin/bash

su -c "node /opt/tty.js/node_modules/tty.js/bin/tty.js --port 3000 --daemonize" pi
echo Started tty.js as daemon
