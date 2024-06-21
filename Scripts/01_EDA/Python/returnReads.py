import gzip
import Bio
from Bio import SeqIO
from Bio.Seq import Seq

def returnReads (file_path = file_path, wantLen = False):
    
    with gzip.open(file_path, "rt") as handle:
        reads = list(SeqIO.parse(handle, "fasta"))  
        
    if wantLen:
        readsLen = len(reads)
        return readsLen
    else:
        return reads
