import os
import glob
from tkinter import Tk
from tkinter.filedialog import askdirectory

directory = askdirectory(title='Select Folder')
string_to_replace = input("Insert the text you want to replace:")
new_string = input("Insert new text:")

for filename in glob.iglob(directory + '/*.*'):
    base_name, extension = os.path.splitext(filename)
    new_file_name = base_name.replace(string_to_replace, new_string)
    new_file_name_with_original_extension = new_file_name + extension
    new_filename = os.path.join(directory, new_file_name_with_original_extension)
    os.rename(filename, new_filename)

print("Files replaced")
