import os

# Specify the directory path
directory_path = '/python'  # Current directory

# Get the list of files and directories
contents = os.listdir(directory_path)

# Print the contents
for item in contents:
    print(item)
