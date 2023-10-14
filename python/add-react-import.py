import os
import re

directory = '' # your path here

updated_imports_count = 0
added_imports_count = 0

def consolidate_imports(file_contents, file_path):

    global updated_imports_count
    global added_imports_count

    existing_imports = re.findall(r'import (.+?) from ["\']react["\']\s*;', file_contents)
    if existing_imports:
        existing_imports = [imp for imp in existing_imports if 'React' not in imp]
        if existing_imports:
            updated_imports_count += 1
            print(f"Updated import for {file_path}")
            consolidated_import = f"import React, {', '.join(existing_imports)} from 'react';"
            return re.sub(r'import (.+?) from ["\']react["\']\s*;', consolidated_import, file_contents)
        else:
            print(f"Skipping, import found for {file_path}")
            return file_contents
    else:
        added_imports_count += 1
        print(f"Added import for {file_path}")
        return f"import React from 'react';\n{file_contents}"

def read_file(file_path):
    full_file_path = os.path.join(directory, file_path)
    with open(full_file_path, 'r') as f:
        file_contents = f.read()
        modified_contents = consolidate_imports(file_contents, file_path)
        return modified_contents

for filename in os.listdir(directory):
    if filename.endswith('.tsx'):
        modified_contents = read_file(filename)
        with open(os.path.join(directory, filename), 'w') as f:
            f.write(modified_contents)

print(f"Total imports updated: {updated_imports_count}")
print(f"Total imports added: {added_imports_count}")