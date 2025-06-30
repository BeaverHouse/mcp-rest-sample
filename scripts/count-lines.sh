#!/bin/bash

# Script for counting lines of all .py files in the current directory and subdirectories
# This is Bash script, see count-lines.ps1 for the PowerShell version.
# Written by Austin Lee.

total_lines=0
file_count=0

echo -e "\033[32mCalculating Python file line count...\033[0m"

# Find all .py files recursively and process them
while IFS= read -r -d '' file; do
    if [[ "$file" != *.venv* ]]; then
        lines=$(wc -l < "$file")
        total_lines=$((total_lines + lines))
        file_count=$((file_count + 1))
        
        # Print information about each file
        echo -e "\033[33m$file: $lines lines\033[0m"
    fi
done < <(find . -name "*.py" -print0)

# Print final result
echo -e "\n\033[32mFinal result\033[0m"
echo -e "\033[36mTotal file count: $file_count\033[0m"
echo -e "\033[36mTotal line count: $total_lines\033[0m" 