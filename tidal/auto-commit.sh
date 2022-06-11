#!/usr/bin/env bash

echo "Creating a timestamped commit"

LC_ALL=en_US.UTF-8
timestamp=$(date +"%c")
message="Auto-commit ${timestamp}"

echo $message
git add -A
git commit -m "${message}"
git push origin master
