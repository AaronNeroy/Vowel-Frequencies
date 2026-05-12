#!/bin/bash

echo "Starting Frequency Analyzer..."

# Check if data.txt exists
echo "Checking for data.txt..."
ls /app/data.txt

# Running the Python frequency analyzer
echo "Running frequency.py..."
FREQ_RESULT=$(python3 /app/.github/scripts/frequency.py /app/data.txt)

# Debug: print the result
echo "FREQ_RESULT is: $FREQ_RESULT"
echo "GITHUB_USER is: $GITHUB_USER"

# Running update_readme.sh
bash /app/.github/scripts/update_readme.sh "$FREQ_RESULT" "$GITHUB_USER"

echo "Process Completed!"
