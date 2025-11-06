
import os
import shutil
import random

ratio_to_move = 0.2  # Ratio of images to move to the first destination folder

def split_images(original_dir, dest_dir, ratio = ratio_to_move):

# This Python code defines a function, split_images, designed to randomly 
# move a specified percentage of files from subfolders within an 
# original_dir to corresponding subfolders within a single dest_dir.

    # Ensure destination directories exist
    os.makedirs(dest_dir, exist_ok=True)

    for subfolder in os.listdir(original_dir):
        subfolder_path = os.path.join(original_dir, subfolder)
        if os.path.isdir(subfolder_path):
            # Create corresponding subfolders in both destination directories
            dest_subfolder1 = os.path.join(dest_dir, subfolder)
            os.makedirs(dest_subfolder1, exist_ok=True)

            # List all files in the current subfolder
            files = [f for f in os.listdir(subfolder_path) if os.path.isfile(os.path.join(subfolder_path, f))]
            random.shuffle(files)  # Shuffle the list to ensure random splitting

            # Calculate split points
            split_index1 = int(len(files) * ratio)

            # Move the files to the first destination subfolder
            for file in files[:split_index1]:
                src_path = os.path.join(subfolder_path, file)
                dest_path = os.path.join(dest_subfolder1, file)
                shutil.move(src_path, dest_path)
                print(f"Moved {src_path} to {dest_path}")

    print("Image splitting complete.")

# Define paths to the directories
original_dir = '/path/to/your/original/images'
destination_dir = '/path/to/your/destination/images'

split_images(original_dir, destination_dir, ratio = ratio_to_move)
