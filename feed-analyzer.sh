#!/bin/bash
# feed-analyzer.sh
# Usage: ./feed-analyzer.sh twitter_dataset.csv
#
# Extracts the Username column, counts how many tweets each user has,
# and prints the Top 5 Most Active Users.

FILE="$1"

if [ -z "$FILE" ]; then
    echo "Usage: ./feed-analyzer.sh <csv_file>"
    exit 1
fi

if [ ! -f "$FILE" ]; then
    echo "Error: File '$FILE' not found."
    exit 1
fi

echo "Top 5 Most Active Users:"
echo "-------------------------"

tail -n +2 "$FILE" | cut -d',' -f2 | sort | uniq -c | sort -rn | head -n 5
