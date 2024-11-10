#!/bin/bash

# Create a virtual environment in the 'venv' directory
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

echo "Dependencies installed successfully."
