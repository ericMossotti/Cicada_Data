# ---- Import data from the web with wget
import os
import sys
import wget

def importer (fileMap):
    # Download from URL to path and notify when complete
    for url, file_path in fileMap.items():
        # Check if file exists before downloading
        if not os.path.exists(file_path):
            wget.download(url, file_path)
            print(f"{file_path} written")
        else:
            print(f"{file_path} already exists.")
