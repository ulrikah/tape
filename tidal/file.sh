#!/usr/bin/env bash


LC_ALL=no_NO.UTF-8
timestamp=$(date -u +%Y%m%d_%H%M%S)


filename="yes_${timestamp}.tidal"
echo "Creating a new Tidal file called $filename"
touch $filename 

echo "setcps (140/60/4)" >> $filename
