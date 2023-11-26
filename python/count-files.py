import os

def is_hidden(filepath):
    if os.name == 'nt':
        try:
            attrs = os.stat(filepath).st_file_attributes
            return attrs & getattr(os, 'FILE_ATTRIBUTE_HIDDEN', 2) != 0
        except OSError:
            return False
    else:  # For Unix-like systems (including Linux)
        return os.path.basename(filepath).startswith('.')

def count_files_in_subdirectories(root_directory):
    subdirectory_info = []

    for dirpath, dirnames, filenames in os.walk(root_directory):
        filenames = [file for file in filenames if not is_hidden(os.path.join(dirpath, file))]
        
        if filenames:
            file_count = len(filenames)
            folder_name = os.path.basename(dirpath)
            subdirectory_info.append((folder_name, file_count))

    subdirectory_info.sort(key=lambda x: x[1], reverse=True)

    for folder_name, file_count in subdirectory_info:
        print(f"{folder_name}: {file_count}")

root_directory = ''
count_files_in_subdirectories(root_directory)
