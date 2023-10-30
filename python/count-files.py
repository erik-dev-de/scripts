import os

def count_files_in_subdirectories(root_directory):
    subdirectory_info = []

    for dirpath, dirnames, filenames in os.walk(root_directory):
        if filenames:

            file_count = len(filenames)

            folder_name = os.path.basename(dirpath)
            subdirectory_info.append((folder_name, file_count))

    subdirectory_info.sort(key=lambda x: x[1], reverse=True)

    for folder_name, file_count in subdirectory_info:
        print(f"{folder_name}: {file_count}")

root_directory = ''

count_files_in_subdirectories(root_directory)
