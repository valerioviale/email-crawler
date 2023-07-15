#!/bin/bash

# Change to the specified working directory
working_dir="/Users/valerio/Desktop/Courses/email-crawler"
cd "$working_dir" || exit

# Log the current working directory to ensure the script runs in the correct location
echo "Current working directory: $(pwd)"

# Add all changes
git add .

# Commit changes with a timestamp
commit_message="Daily commit - $(date +"%Y-%m-%d %H:%M:%S")"
git commit -m "$commit_message"

# Push changes
git push

