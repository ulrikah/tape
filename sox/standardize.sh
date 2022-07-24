#!/bin/bash

# input

ARG=$1

if   [[ -d "${ARG}" ]]; then 
    echo "${ARG} is a directory"
    # TODO: validate that all files in the dir are of a given extension
    FILES=(${ARG}/*)
elif [[ -f "${ARG}" ]]; then 
    echo "${ARG} is a file"
    FILES=($ARG)
elif [[ -ne "${ARG}" ]]; then 
    echo "$ARG is not a valid audio file"
else 
    echo "Input argument has to be a valid audio file or a directory containing only audio files"
    exit 1
fi

for FILE in ${FILES[@]}; do
    EXT="${FILE##*.}"
    BASENAME=$(basename "${FILE}" ."${EXT}")
    OUTPUT="${BASENAME}_std.${EXT}"
    
    sox $FILE \
        -r 44100 \
        -b 16 \
        $OUTPUT \
        silence 1 0.1 1% 1 0.1 1% # trim silence from start and end

    echo "${OUTPUT} 🌻"
done