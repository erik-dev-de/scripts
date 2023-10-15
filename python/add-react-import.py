import os
import glob
import re

directory = r'C:\storage\programming\FGO-Frontend\fgo\src'  # your path here
library_imports = ['from "react"', 'from \'react\'']
added_imports = 0
updated_imports = 0

for filename in glob.iglob(directory + '/**/*.tsx', recursive=True):
    if os.path.isfile(filename):
        with open(filename,'r', encoding='utf-8') as file:
            file_contents = file.read().splitlines()
            matching_lines = list(filter(lambda line: any(term in line for term in library_imports), file_contents))
            if len(matching_lines) == 0:
                print(f"Adding import for {filename}")
                added_imports += 1
                file_contents.insert(0, "import React from 'react';")
                with open(filename, 'w', encoding='utf-8') as updated_file:
                    updated_file.write('\n'.join(file_contents))
            else:
                result_strings = [re.split(r'\s+from\s+', s)[0] for s in matching_lines]
                has_react_import = [s for s in result_strings if re.search(r'[Rr]eact', s)]
                if len(has_react_import) > 0:
                    print(f"Skipping, react import exists for {filename}")
                else:
                    print(f"Updated existing import for {filename}")
                    updated_imports += 1
                    if result_strings:
                        modified_import = result_strings[0].replace('import', 'import React,') + ' from \'react\';'
                        index_to_replace = file_contents.index(matching_lines[0])
                        file_contents[index_to_replace] = modified_import
                    with open(filename, 'w', encoding='utf-8') as updated_file:
                        updated_file.write('\n'.join(file_contents))

print(f"Added imports for {added_imports}")
print(f"Updated imports for {updated_imports}")