#!/bin/bash

# Change to the specified working directory
working_dir="/Users/valerio/Desktop/Courses/email-crawler"
cd "$working_dir" || exit

# Log the current working directory to ensure the script runs in the correct location
echo "Current working directory: $(pwd)"

# List of commit messages
messages=("Initial commit" "Update README.md" "Fix bug" "Add new feature" "Refactor code")

# Specify the name of the remote branch
remote_branch="main"

# Create a new branch with a random name
branch_name="autocommit-$(date +"%Y%m%d%H%M%S")"
/usr/bin/git checkout -b "$branch_name"

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

# Pull the latest changes from the remote branch
/usr/bin/git pull origin "$remote_branch"

# Push changes to the specified remote branch
/usr/bin/git push origin "$branch_name":"$remote_branch"

# Switch back to the main branch
/usr/bin/git switch main