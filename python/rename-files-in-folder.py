import os
import glob
from tkinter import Tk
from tkinter.filedialog import askdirectory

directory = askdirectory(title='Select Folder')
starting_file_number = 1
new_file_name = input("Insert your file name: ")

for filename in glob.iglob(directory + '/*.*'):
    base_name, extension = os.path.splitext(filename)
    new_file_name_with_original_extension = new_file_name + f"-{starting_file_number}" + extension
    new_filename = os.path.join(directory, new_file_name_with_original_extension)
    os.rename(filename, new_filename)
    starting_file_number += 1

print(f"Files renamed to {new_file_name}-1, {new_file_name}-2, etc.")
