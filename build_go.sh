#!/bin/bash
echo "Building sleep-sound..."
go build -o sleep-sound
if [ $? -eq 0 ]; then
    echo "Build successful!"
    echo "Run with: ./sleep-sound [options]"
else
    echo "Build failed!"
fi
