#!/bin/bash

for file in *.png; do
  if [ -e "$file" ]; then
    rm "$file"
    echo "Deleted $file"
  fi
done