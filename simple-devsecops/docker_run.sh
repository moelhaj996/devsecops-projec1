#!/bin/bash

echo "Building Docker image..."
docker build -t secure-app .

echo "\nRunning container..."
docker run -p 5000:5000 secure-app