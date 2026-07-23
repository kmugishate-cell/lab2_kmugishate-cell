#!/bin/bash
#
# feed-analyzer.sh
# Usage: ./feed-analyzer.sh twitter_dataset.csv
#
# Extracts the Username column, counts how many tweets each user posted,
# and displays the Top 5 Most Active Users.
#
# NOTE: twitter_dataset.csv contains "Text" fields with embedded newlines
# inside quoted values (valid CSV, but it breaks naive line-based tools
# like `cut` on raw lines). We use a small embedded Python snippet with
# the `csv` module to correctly parse quoted, multi-line fields, then hand
# off to the classic sort | uniq -c | sort -rn | head -n 5 pipeline.

FILE="$1"

if [ -z "$FILE" ]; then
    echo "Usage: ./feed-analyzer.sh <csv_file>"
    exit 1
fi

if [ ! -f "$FILE" ]; then
    echo "Error: File '$FILE' not found."
    exit 1
fi

if ! command -v python3 &> /dev/null; then
    echo "Error: python3 is required but was not found in PATH."
    exit 1
fi

echo "Top 5 Most Active Users:"
echo "-------------------------"

python3 -c "
import csv, sys

with open('$FILE', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader, None)  # skip header row

    if header is None:
        sys.exit(0)  # empty file, nothing to do

    for row in reader:
        if len(row) > 1:
            print(row[1])
" | sort | uniq -c | sort -rn | head -n 5
