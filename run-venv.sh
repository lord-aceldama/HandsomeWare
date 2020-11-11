#!/bin/bash

if [ ! -d "./venv/" ]; then
  echo "First run: Launching setup..."
  bash ./setup-venv.sh
fi

. ./venv/bin/activate
python handsomeware.py "$@"
deactivate
