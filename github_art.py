#!/usr/bin/env python3
import os
import datetime
import subprocess
from pathlib import Path

def create_commit(date, message, times=1):
    """Create a commit for a specific date."""
    for _ in range(times):
        subprocess.run(['git', 'commit', '-m', message, '--date', date.strftime('%Y-%m-%d'), '--allow-empty'])

def create_background_commits(start_date):
    """Create commits for every day in a year to form a background."""
    for day in range(365):
        date = start_date + datetime.timedelta(days=day)
        create_commit(date, 'Background commit for GitHub art')

def main():
    # Initialize git repository if not already initialized
    if not Path('.git').exists():
        subprocess.run(['git', 'init'])
    
    # Define the pattern for "clau"
    # Each letter is represented by a 5x7 grid where 1 means commit, 0 means no commit
    pattern = {
        'c': [
            [0, 1, 1, 1, 0],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 1],
            [0, 1, 1, 1, 0]
        ],
        'l': [
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1]
        ],
        'a': [
            [0, 1, 1, 1, 0],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1]
        ],
        'u': [
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [0, 1, 1, 1, 0]
        ],
        'smile': [
            [0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0]
        ]
    }
    
    # Start date set to 2018
    start_date = datetime.datetime(2017, 2, 19)
    
    # Create commits for each letter with spacing between them
    letter_spacing = 42  # Number of days between each letter
    current_date = start_date
    
    # First create the text
    for letter in 'clau':
        for row in range(7):
            for col in range(5):
                if pattern[letter][row][col]:
                    date = current_date + datetime.timedelta(days=row + (col * 7))
                    create_commit(date, f'Working on {letter} in GitHub art', 1)
        
        # Add spacing between letters
        current_date += datetime.timedelta(days=letter_spacing)
    
  
    current_date += datetime.timedelta(days=letter_spacing)
  
    Add a smile
    for row in range(7):
        for col in range(5):
            if pattern['smile'][row][col]:
                date = current_date + datetime.timedelta(days=row + (col * 7))
                create_commit(date, 'working on the smile to GitHub art', 3)
                
                
                
    # add background
    # Create background commits starting from 2017
    background_start = datetime.datetime(2017, 1, 1)
    create_background_commits(background_start)
    
    print("Commits created successfully!")

if __name__ == '__main__':
    main() 