#!/bin/bash

PASSED=$1

if   [[ -d "${PASSED}" ]]; then 
    echo "${PASSED} is a directory"
    # TODO: validate that all files in the dir are of a given extension
    FILES=(${PASSED}/*)
elif [[ -f "${PASSED}" ]]; then 
    echo "${PASSED} is a file"
    FILES=($PASSED)
elif [[ -ne "${PASSED}" ]]; then 
    echo "$PASSED is not a valid audio file"
else 
    echo "Input argument has to be a valid audio file or a directory containing only audio files"
    exit 1
fi


echo "Processing files:"
printf '%s\n' "${FILES[@]}"