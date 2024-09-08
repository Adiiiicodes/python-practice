import os

def clear_clutter(folder_path):
    # Change the directory to the given folder path
    os.chdir('C:\Users\HP\Documents\OOPM')

    # Get a list of all files in the directory
    files = os.listdir()

    # Create dictionaries to store files by their extensions
    file_types = {}

    # Categorize files by their extension
    for file in files:
        if os.path.isfile(file):  # Ignore directories
            ext = file.split('.')[-1]
            if ext in file_types:
                file_types[ext].append(file)
            else:
                file_types[ext] = [file]

    # Rename files for each file type
    for ext, file_list in file_types.items():
        file_list.sort()  # Optional: Sort files alphabetically before renaming
        for i, file in enumerate(file_list, start=1):
            new_name = f"{i}.{ext}"
            os.rename(file, new_name)
            print(f"Renamed {file} to {new_name}")

# Provide the path to the folder you want to clear clutter from
folder_path = "C:/path/to/your/folder"
clear_clutter(folder_path)
