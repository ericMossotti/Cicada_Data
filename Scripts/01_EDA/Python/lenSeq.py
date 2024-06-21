import gzip
import Bio
from Bio import SeqIO
from Bio.Seq import Seq

def lenSeq (file_path = file_path):
    
    with gzip.open(file_path, "rt") as handle:
        seqLen = sum(len(record.seq) for record in SeqIO.parse(handle, "fasta"))
        print(f"Sequence length: '{seqLen}'")
        
    return seqLen
