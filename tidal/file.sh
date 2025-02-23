#!/usr/bin/env bash


if [[ $1 ]]; then
    score_name=$1
else
    score_name="untitled"
fi

LC_ALL=no_NO.UTF-8
timestamp=$(date -u +%Y%m%d_%H%M%S)
filename="${timestamp}_${score_name}.tidal"
output_file="scores/$filename"
echo "Creating a new Tidal score: $output_file"
touch $output_file

echo "setcps (140/60/4)" >> $output_file
