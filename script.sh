#!/bin/bash

# Change to the specified working directory
working_dir="/Users/valerio/Desktop/Courses/email-crawler"
cd "$working_dir" || exit

# Log the current working directory to ensure the script runs in the correct location
echo "Current working directory: $(pwd)"

# Add all changes
/usr/bin/git add .

# Check if there are changes to commit
if /usr/bin/git diff --quiet --exit-code; then
    # No changes, so create an empty file with the date stamp
    touch empty.txt
    echo "Date: $(date +"%Y-%m-%d %H:%M:%S")" >> empty.txt
    /usr/bin/git add empty.txt
fi

# Commit changes with a timestamp
commit_message="Daily commit - $(date +"%Y-%m-%d %H:%M:%S")"
/usr/bin/git commit -m "$commit_message"

# Push changes
/usr/bin/git push