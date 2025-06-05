#!/bin/bash

# This script stages all changes, commits with the provided message, and pushes the current branch to the remote repository

set -e

if [ $# -ne 1 ]; then
    echo "Usage: $0 <commit-message>"
    exit 1
fi

commit_message="$1"

# Get the current branch name
branch=$(git rev-parse --abbrev-ref HEAD)

# Stage all changes
git add .

# Commit with the provided message
git commit -m "$commit_message"

# Push the current branch to origin
git push origin "$branch"