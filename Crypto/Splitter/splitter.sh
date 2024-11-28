#!/bin/bash

file_to_copy=$1
splits=$2

if [ -z "$file_to_copy" ] || [ -z "$splits" ]; then
    echo "Usage: $0 <file_to_copy> <nº of splits>"
    exit 1
fi

mkdir -p splitted

for (( i=1; i<=splits; i++ ))
do
    filename=$(basename -- "$file_to_copy")
    extension="${filename##*.}"
    filename="${filename%.*}"
    new_file="${filename}_${i}.${extension}"
    echo "Copying $file_to_copy to splitted/$new_file"
    cp "$file_to_copy" "splitted/$new_file"
done