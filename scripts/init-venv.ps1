# This script initializes a virtual environment and syncs the dependencies, using uv.
# This is PowerShell script, see init-venv.sh for the Bash version.
# Written by Austin Lee.

Write-Host "Initializing venv"

Set-Location -Path "app"
uv sync
Set-Location -Path ".."

Write-Host "Venv initialized" 