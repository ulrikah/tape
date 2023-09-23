#!/usr/bin/env bash


LC_ALL=no_NO.UTF-8
timestamp=$(date -u +%Y%m%d_%H%M%S)


filename="untitled_${timestamp}.tidal"
output_file="scores/$filename"
echo "Creating a new Tidal file called $output_file"
touch $output_file

echo "setcps (140/60/4)" >> $output_file
