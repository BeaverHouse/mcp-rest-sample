#!/bin/bash

# This script initializes a virtual environment and syncs the dependencies, using uv.
# This is Bash script, see init-venv.ps1 for the PowerShell version.
# Written by Austin Lee.

echo "Initializing venv"

cd app
uv sync
cd ..

echo "Venv initialized"