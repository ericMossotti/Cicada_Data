# ---- Decompress the gz file with gzip

import os
import gzip
import shutil

def decompress(gzFasta, fasta):
    
    # If not decompressed, then decompress and redirect to a new file path
    if not os.path.exists(fasta):
        # File doesn't exist, then decompress
        with gzip.open(gzFasta, 'rb') as f_in:
            with open(fasta, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        print(f"{fasta} has been decompressed and written.")
    else:
        print(f"The file {fasta} already exists. Skipping unzip.")
