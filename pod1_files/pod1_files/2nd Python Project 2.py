import os
import glob

# Set the working directory to the correct path
working_directory = r'C:\Users\Lesli\OneDrive\Desktop\luit-2024-cohort\pod1_files\pod1_files' 

# List to store information about files
files_info = []

# Use glob to find all files in the directory
for item in glob.glob(os.path.join(working_directory, '*')):
    # Check if the item is a file (not a directory)
    if os.path.isfile(item):
        # Get the size of the file
        file_size = os.path.getsize(item)
        
        # Get the file name from the full path
        file_name = os.path.basename(item)
        
        # Create a dictionary with the file name and its size
        file_info = {
            'file_name': file_name,
            'size_bytes': file_size  # size in bytes
        }
        
        # Add the file info to the list
        files_info.append(file_info)

# Print the list of files with their information
for file_info in files_info:
    print(f"File: {file_info['file_name']}, Size: {file_info['size_bytes']} bytes")