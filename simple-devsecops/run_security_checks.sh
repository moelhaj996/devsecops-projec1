#!/bin/bash

echo "Running SAST with Bandit..."
bandit -r app/

echo "\nChecking dependencies with Safety..."
safety check -r requirements.txt

echo "\nRunning tests with coverage..."
pytest --cov=app tests/