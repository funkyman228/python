import os
import shutil

print("Enter dir")
folder_path = input()  # Replace this with the actual path to your folder
folder_path = folder_path.replace(os.sep, '/')

# Set the source and destination directories
src_dir = folder_path
dst_dir = folder_path
singles_dir = f"{folder_path}/Singles"

# Create the "singles" directory if it doesn't exist
os.makedirs(singles_dir, exist_ok=True)

# Get a list of all the files and subdirectories in the source directory
items = os.listdir(src_dir)

# Iterate over the items in the list
for item in items:

    print(item)
    # Skip directories that contain the string "singles"
    if 'Singles' in item:
        real_sing_dir = item
        continue

    # Skip directories that start and end with square brackets
    if item.startswith('['):
        continue

    # Check if the item is a directory
    if os.path.isdir(os.path.join(src_dir, item)):
        # Count the number of files in the directory
        num_files = len([f for f in os.listdir(os.path.join(src_dir, item)) if os.path.isfile(os.path.join(src_dir, item, f))])
        
        # Check if the directory contains only one file
        if num_files == 1:
            # Get the name of the file
            file_name = os.listdir(os.path.join(src_dir, item))[0]
            
            # Add the name of the directory to the beginning of the file name
            new_name = f'{item}_{file_name}'

            # Rename the file with the name of the directory
            os.rename(os.path.join(src_dir, item, file_name), os.path.join(src_dir, item, new_name))
            
            # Move the file to the "singles" directory
            shutil.move(os.path.join(src_dir, item, new_name), os.path.join(singles_dir, new_name))
            
            # Delete the empty directory
            os.rmdir(os.path.join(src_dir, item))
        else:
            # Modify the name of the directory by adding the number of files to it
            new_name = f'[{num_files}] {item}'

            # Rename the directory
            os.rename(os.path.join(src_dir, item), os.path.join(dst_dir, new_name))

# Set the source and destination directories
src_dir = os.path.join(src_dir, 'Singles')
dst_dir = os.path.join(folder_path, real_sing_dir)

# Get a list of all the files in the source directory
items = os.listdir(src_dir)

if real_sing_dir == None:
    real_sing_dir == 'Singles'


# Iterate over the items in the list
if real_sing_dir != 'Singles':
    for item in items:
        # Check if the item is a file
        if os.path.isfile(os.path.join(src_dir, item)):
            # Move the file to the destination directory
            shutil.move(os.path.join(src_dir, item), os.path.join(dst_dir, item))

    # Delete the empty directory
    os.rmdir(os.path.join(folder_path, 'Singles'))


item = real_sing_dir
# Count the number of files in the directory
num_files = len([f for f in os.listdir(os.path.join(folder_path, item)) if os.path.isfile(os.path.join(folder_path, item, f))])
# Modify the name of the directory by adding the number of files to it
new_name = f'[{num_files}] Singles'
# Rename the directory
os.rename(os.path.join(folder_path, item), os.path.join(folder_path, new_name))