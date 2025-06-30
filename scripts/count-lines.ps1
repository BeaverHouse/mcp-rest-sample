# Script for counting lines of all .py files in the current directory and subdirectories
# This is PowerShell script, see count-lines.sh for the Bash version.
# Written by Austin Lee.

$totalLines = 0
$fileCount = 0

Write-Host "Calculating Python file line count..." -ForegroundColor Green

# Find all .py files recursively and process them
# Exclude the file in .venv
Get-ChildItem -Path . -Filter *.py -Recurse | ForEach-Object {
    if ($_.FullName -notlike "*.venv*") {
        $lines = (Get-Content $_.FullName -Encoding UTF8).Count
        $totalLines += $lines
        $fileCount++
        
        # Print information about each file
        Write-Host "$($_.FullName): $lines lines" -ForegroundColor Yellow
    }
}

# Print final result
Write-Host "`nFinal result" -ForegroundColor Green
Write-Host "Total file count: $fileCount" -ForegroundColor Cyan
Write-Host "Total line count: $totalLines" -ForegroundColor Cyan 