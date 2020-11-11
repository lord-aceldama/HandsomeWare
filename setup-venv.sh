#!/bin/bash

echo "Creating virtual environment..."
python3 -m venv venv

echo "Installing pip(s)..."
. ./venv/bin/activate
pip3 install -r requirements.txt
deactivate

echo "Making scripts executable..."
chmod +x *.py
chmod +x *.sh

echo "All done :)"
