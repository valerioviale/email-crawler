#!/bin/bash

# Change to the specified working directory
working_dir="/Users/valerio/Desktop/Courses/GitAuto"
cd "$working_dir" || exit

# Log the current working directory to ensure the script runs in the correct location
echo "Current working directory: $(pwd)"

# Add all changes
git add .

# Check if there are changes to commit
if git diff --quiet --exit-code; then
    # No changes, so create an empty file with the date stamp
    touch empty.txt
    echo "Date: $(date +"%Y-%m-%d %H:%M:%S")" >> empty.txt
    git add empty.txt
fi

# Commit changes with a timestamp
commit_message="Daily commit - $(date +"%Y-%m-%d %H:%M:%S")"
git commit -m "$commit_message"

# Push changes
git push
