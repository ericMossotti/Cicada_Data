# ---- Import data from the web with wget

import os
import sys
import wget

def importer (fileMap):
    
    # Check for directory, then skip, or create dir and import files
    #if not os.path.exists(directory):
    #    os.makedirs(directory)
    #    print(f"Directory {directory} created successfully.")
        
    # Otherwise, notify if exists
    #else:
    #    print(f"Directory {directory} already exists.")
        
    # Download from URL to path and notify when complete
    for url, file_path in fileMap.items():
        # Check if file exists before downloading
        if not os.path.exists(file_path):
            wget.download(url, file_path)
            print(f"{file_path} written")
        else:
            print(f"{file_path} already exists.")
