import os

def delete_files_in_directory(directory_path):

# This Python code defines a function, delete_files_in_directory, 
# whose purpose is to recursively delete all individual files within a 
# specified directory path and all its subdirectories. 
# Crucially, it leaves the directories and subdirectories themselves intact.

    # Walk through the directory tree
    for root, dirs, files in os.walk(directory_path):
        # Loop through each file in the current directory
        for file_name in files:
            # Construct the full path to the file
            file_path = os.path.join(root, file_name)
            try:
                # Delete the file
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")

# Replace 'your_directory_path' with the path of your directory
directory_path = '/path/to/your/directory'
delete_files_in_directory(directory_path)