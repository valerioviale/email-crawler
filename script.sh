#!/bin/bash

# Change to the specified working directory
working_dir="/Users/valerio/Desktop/Courses/email-crawler"
cd "$working_dir" || exit

# Log the current working directory to ensure the script runs in the correct location
echo "Current working directory: $(pwd)"

# List of commit messages
messages=("New feature" "Documentation" "Bug Fix" "Test" "Some stuff")

# Specify the name of the remote branch
remote_branch="main"

# Pull the latest changes from the remote branch
/usr/bin/git pull origin "$remote_branch"

# Loop to perform five commits
for ((i=0; i<5; i++))
do
    # Add all changes
    /usr/bin/git add .

    # Check if there are changes to commit
    if /usr/bin/git diff --quiet --exit-code; then
        # No changes, so create an empty file with the date stamp
        touch empty.txt
        echo "Date: $(date +"%Y-%m-%d %H:%M:%S")" >> empty.txt
        /usr/bin/git add empty.txt
    fi

    # Generate a random index to select a commit message
    index=$(( RANDOM % 5 ))

    # Select the commit message
    commit_message="${messages[$index]} - $(date +"%Y-%m-%d %H:%M:%S")"
    
    # Commit changes with the randomly chosen message
    /usr/bin/git commit -m "$commit_message"
done

# Push changes to the remote branch
/usr/bin/git push origin "$remote_branch"
