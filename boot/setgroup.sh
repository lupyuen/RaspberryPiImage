#!/bin/bash
# setgroup.sh groupname
# Set the group name in /etc/hosts and /etc/hostname

#test="/Users/Luppy/Raspberry Pi"
test=""

groupname="${1:?Specify a group name e.g. g88}"
file1="${test}/etc/hosts"
file2="${test}/etc/hostname"

echo sudo sed -i.bak s/g89/${groupname}/g "${file1}"
echo sudo sed -i.bak s/g89/${groupname}/g "${file2}"

sudo sed -i.bak s/g89/${groupname}/g "${file1}"
sudo sed -i.bak s/g89/${groupname}/g "${file2}"

echo Updated group ${groupname} in ${file1}, ${file2}
