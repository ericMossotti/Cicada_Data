from Bio import SeqIO
from collections import Counter
import gzip

def calc_n50(file_path = None):
    
    with gzip.open(file_path, "rt") as handle:

        # Parse the FASTA file and extract the sequence lengths as an array
        sequence_lengths = [len(record.seq) for record in SeqIO.parse(handle, "fasta")]

    tmp = []
    
    for tmp_number in set(sequence_lengths):
            tmp += [tmp_number] * sequence_lengths.count(tmp_number) * tmp_number
            
    tmp.sort()
 
    if (len(tmp) % 2) == 0:
        median = (tmp[int(len(tmp) / 2) - 1] + tmp[int(len(tmp) / 2)]) / 2
        
    else:
        median = tmp[int(len(tmp) / 2)]
 
    return median

    # Sort the sequence lengths in descending order
#    sorted_lengths = sorted(sequence_lengths, reverse = True)

    # Calculate the total sum of all sequence lengths
#    total_sum = sum(sequence_lengths)

    # Calculate the cumulative sum of the sorted sequence lengths
#    cumulative_sum = 0
#    for length in sorted_lengths:
#        cumulative_sum += length
#        if cumulative_sum >= total_sum / 2:
#            return length

    # If no sequence satisfies the N50 condition, return 0
#    return 0
