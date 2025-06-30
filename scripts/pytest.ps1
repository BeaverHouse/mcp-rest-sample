# This script runs the tests using pytest.
# This is PowerShell script, see pytest.sh for the Bash version.
# Written by Austin Lee.

Set-Location -Path "app"
& ".venv\Scripts\python.exe" -m pytest
Set-Location -Path ".."