#!/bin/bash

# Imports react for tsx files, if it's not already imported

directory="" # your directory here

for file in "$directory"/*.tsx; do
    has_library_import=$(grep -r 'from "react"\|from '\''react'\''' "$file")
    
    if [ "$has_library_import" ]; then
        has_react_imported=$(grep -w "React" "$file")
        if [ "$has_react_imported" ]; then
            echo "Skipping, React import exists for $file"
        else
            sed -i -e "s/$has_library_import/import React, $has_library_import/" "$file"
            echo "Updated the import in $file"
        fi
    else
        gawk -i inplace 'BEGINFILE{print "import React from '\''react'\'';"} 1' "$file"
        echo "Added React import to $file"
    fi
done
