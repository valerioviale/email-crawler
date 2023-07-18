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

# Commit changes with four random messages and a timestamp
for ((i=0; i<4; i++))
do
    # Generate a random index to select a commit message
    index=$(( RANDOM % 5 ))

    # List of commit messages
    messages=("New feature" "Documentation" "Bug Fix" "Test" "Some stuff")

    # Select the commit message
    commit_message="${messages[$index]} - $(date +"%Y-%m-%d %H:%M:%S")"
    
    # Commit changes with the randomly chosen message
    /usr/bin/git commit -m "$commit_message"
done

# Push changes
/usr/bin/git push