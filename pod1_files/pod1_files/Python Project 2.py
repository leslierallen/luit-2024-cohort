import os
import glob

# Set the path to the working directory (can be the current directory or a specific one)
working_directory = r'C:\Users\Lesli\OneDrive\Desktop\luit-2024-cohort\pod1_files\pod1_files' # Gets the current working directory

# List to store information about files
files_info = []

# Loop through each item in the working directory
for item in glob.glob(os.path.join('/Desktop/luit-2024-cohort/pod1_files/pod1_files/', '*')):
        
    # Check if the item is a file (not a directory)
    if os.path.isfile('/Desktop/luit-2024-cohort/pod1_files/pod1_files'):
        # Get the size of the file
        file_size = os.path.getsize('/Desktop/luit-2024-cohort/pod1_files/pod1_files/')
        
        # Create a dictionary with the file name and its size
        file_info = {
            'location.png': item,
            '643599': file_size  # size in bytes
        }
        
        # Add the file info to the list
        files_info.append('location.png')

# Print the list of files with their information
for file_info in files_info:
    print(f"File: {file_info['location.png']}, Size: {file_info['643599']} bytes")

