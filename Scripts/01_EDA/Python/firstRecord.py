import gzip
import Bio
from Bio import SeqIO
from Bio.Seq import Seq

def firstRecord (file_path = file_path):
    
    with gzip.open(file_path, "rt") as handle:
        first_record = next(SeqIO.parse(handle, "fasta"))
        
    return first_record
