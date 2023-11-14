import os
import shutil
import string

# Set the path to your music directory here
music_directory = '/path/to/your/music/folder'

# Move files into the respective folders
for filename in os.listdir(music_directory):
    full_path = os.path.join(music_directory, filename)
    
    if os.path.isfile(full_path):  # Check if it's a file
        first_char = filename[0].upper()
        if first_char in string.ascii_uppercase:
            shutil.move(full_path, os.path.join(music_directory, first_char, filename))
        elif first_char.isdigit():
            shutil.move(full_path, os.path.join(music_directory, '0-9', filename))

print("Music files have been organized.")
