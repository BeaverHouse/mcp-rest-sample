# This script enters the virtual environment.
# This is PowerShell script, see enter-venv.sh for the Bash version.
# Written by Austin Lee.

Set-Location -Path "app"
./.venv/Scripts/Activate.ps1
Set-Location -Path ".."
