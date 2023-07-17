#!/bin/bash

# List of commit messages
messages=("Initial commit" "Update README.md" "Fix bug" "Add new feature" "Refactor code")

# Generate a random index to select a commit message
index=$(( RANDOM % 5 ))

# Select the commit message
message=${messages[$index]}

# Add all files to the staging area
git add -A

# Commit with the randomly chosen message
git commit -m "$message"

# Push to the remote repository (assuming the remote is named 'origin' and the branch is 'master')
git push origin master
