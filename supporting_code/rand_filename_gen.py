import os
import uuid

def rename_files_to_random(root_folder_path):

# This Python code defines a function, rename_files_to_random, 
# that recursively renames every file within a specified root folder
# and all its subdirectories to a unique, random identifier (UUID)
# while preserving the original file extension.

    # Walk through each subfolder in the root directory
    for dirpath, _, filenames in os.walk(root_folder_path):
        print(f"Processing folder: {dirpath}")
        
        # Shuffle filenames to ensure randomness
        for old_filename in filenames:
            old_file_path = os.path.join(dirpath, old_filename)
            
            # Get the file extension
            file_extension = os.path.splitext(old_filename)[1]
            
            # Generate a unique random filename with the same extension
            new_filename = str(uuid.uuid4()) + file_extension
            new_file_path = os.path.join(dirpath, new_filename)
            
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed {old_filename} to {new_filename} in {dirpath}")

if __name__ == "__main__":
    # Replace with the path to your root folder
    root_folder_path = '/path/to/your/root/folder'
    rename_files_to_random(root_folder_path)