# Lab 2: The Social Media Data Detective

## Overview
This project analyzes a messy Twitter dataset (`twitter_dataset.csv`) using
only custom-built Python logic (no `.sort()`, `sorted()`, or `max()`), plus a
Bash one-liner pipeline for quick command-line analysis.

## Files
- `data-detective. Python script with all 4 quests implementedpy` 
- `feed-analyzer. Bash script that prints the Top 5 most active userssh` 
- `twitter_dataset. dataset used for testingcsv` 

## Requirements
- Python 3
- Bash (Linux/macOS terminal, or WSL/Git Bash on Windows)

## How to Run the Python Script

1. Make sure `twitter_dataset.csv` is in the same directory as
   `data-detective.py`.
2. Run:
```bash
   python3 data-detective.py
```
3. The script will:
   - Load the raw dataset
   - Clean missing `Text`, `Likes`, and `Retweets` fields (Quest 1)
   - Print the most viral tweet by `Likes` (Quest 2)
   - Print the Top 10 most liked tweets using a custom sort (Quest 3)
   - Prompt you to enter a keyword and print all matching tweets (Quest 4)

## How to Run the Shell Script

1. Make the script executable (only needs to be done once):
```bash
   chmod +x feed-analyzer.sh
```
2. Run it, passing the CSV file as an argument:
```bash
   ./feed-analyzer.sh twitter_dataset.csv
```
3. It will print the Top 5 Most Active Users and how many tweets each posted.

> **Note:** `feed-analyzer.sh` assumes `Username` is the 2nd column in the
> CSV. If your actual `twitter_dataset.csv` has a different column order,
> update the `-f2` flag in the `cut` command to match the correct column
> number.

## How the Custom Sorting Algorithm Works

`custom_sort_by_likes()` uses **Selection Sort**: for each position in the
list, it scans the remaining unsorted tweets to find the one with the
highest `Likes` count, then swaps it into place. This repeats until the
entire list is sorted from highest to lowest likes, all without using
Python's built-in `.sort()` or `sorted()` functions.
