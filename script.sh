#!/bin/bash

# Change to the specified working directory
working_dir="/Users/valerio/Desktop/Courses/email-crawler"
cd "$working_dir" || exit

# Log the current working directory to ensure the script runs in the correct location
echo "Current working directory: $(pwd)"

# List of commit messages
messages=("Initial commit" "Update README.md" "Fix bug" "Add new feature" "Refactor code")

# Generate a random index to select a commit message
index=$(( RANDOM % 5 ))

# Select the commit message
message=${messages[$index]}

# Add all changes
/usr/bin/git add .

# Check if there are changes to commit
if /usr/bin/git diff --quiet --exit-code; then
    # No changes, so create an empty file with the date stamp
    touch empty.txt
    echo "Date: $(date +"%Y-%m-%d %H:%M:%S")" >> empty.txt
    /usr/bin/git add empty.txt
fi

# Commit changes with the randomly chosen message
commit_message="Random commit - $message"
/usr/bin/git commit -m "$commit_message"

# Pull the latest changes from the remote repository
/usr/bin/git pull

# Push changes
/usr/bin/git push
