#!/usr/bin/env python3

import os
import shutil
import string

# Set the path to your music directory here
music_directory = '/Volumes/Music/All Music'

# Move files into the respective folders
for filename in os.listdir(music_directory):
    full_path = os.path.join(music_directory, filename)
    
    if os.path.isfile(full_path):  # Check if it's a file
        first_char = filename[0].upper()
        
        # Determine the target folder
        if first_char in string.ascii_uppercase:
            target_folder = first_char
        elif first_char.isdigit():
            target_folder = '0-9'
        else:
            target_folder = '_Other'

        # Move the file to the target folder
        shutil.move(full_path, os.path.join(music_directory, target_folder, filename))

print("Music files have been organized.")
