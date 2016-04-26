#!/bin/bash
# setgroup.sh groupname
# Set the group name in /etc/hosts, /etc/hostname and /home/pi/TP-IoT/*.py

#test="/Users/Luppy/Raspberry Pi"
test=""

# Update hosts and hostname files.
groupname="${1:?Specify a group name e.g. g88}"
file1="${test}/etc/hosts"
file2="${test}/etc/hostname"

echo sudo sed -i.bak s/g88/${groupname}/g "${file1}"
echo sudo sed -i.bak s/g88/${groupname}/g "${file2}"

sudo sed -i.bak s/g88/${groupname}/g "${file1}"
sudo sed -i.bak s/g88/${groupname}/g "${file2}"

echo Updated group ${groupname} in ${file1}, ${file2}

# Update all files in /home/pi/TP-IoT.
shopt -s nullglob
FILES=/home/pi/TP-IoT/*.py
for f in $FILES
do
  echo sed -i s/g88/${groupname}/g "${f}"
  sed -i s/g88/${groupname}/g "${f}"
done
