#!/usr/bin/env python3

import os
import string

# Set the path to your music directory here
music_directory = '/Volumes/Music/All Music'

# Create alphabetical subfolders and a folder for numeric filenames
for letter in string.ascii_uppercase:
    os.makedirs(os.path.join(music_directory, letter), exist_ok=True)

os.makedirs(os.path.join(music_directory, '0-9'), exist_ok=True)

# Create an 'Other' folder for files that don't fit the other categories
os.makedirs(os.path.join(music_directory, '_Other'), exist_ok=True)

print("Subdirectories have been created.")
