"""
Parsing genomic data in a memory-efficent way by not loading the entire
file into memory at once. The file is processed one line at a time, grouping
related lines together. 

Statistics such as N50 are crucial in assessing the contiguity 
of a genome assembly, with higher N50 values generally indicating 
a more contiguous assembly.

The distinction between contigs and scaffolds is important in genome assembly, 
as it provides information about the continuity and completeness of 
the assembly.


#----
read_genome()
____________

Differentiates between scaffolds (which may contain gaps) and contigs 
(continuous sequences). 
  
Calculate the GC content, which is an important genomic characteristic.
Prepare lists of contig and scaffold lengths.


#----
fasta_iter()
____________

Groups the .fasta file data into alternating groups of headers and sequences.
It is a generator function that will pause until the next item is requested 
after yielding a tuple.

The iterator groups two aspects:
  a. Single header lines starting with '>'
  b. Subsequent lines until the next '>'


#----
calculate_stats()
_________________

Where the stats dictionary values are calculated and keys assigned.


#----
def assemblyDictionary()
________________________

Maps the previously created dictionaries of contig and scaffold stats to the 
category they belong, thereby distinguishing the contigs and scaffold stats. 
Returning the desired values is quite intuitive as a result.


"""

import numpy as np
from itertools import groupby

#---- fasta_iter()
def fasta_iter(fasta_file):
    
    fh = open(fasta_file)
    
    # Only need the second part, or code sequences part, of the grouped by items
    fa_iter = (x[1] for x in groupby(fh, lambda line: line[0] == ">"))
    
    for header in fa_iter:
        
        # Get first line of group; drop the ">" and starting/trailing whitespace
        header = next(header)[1:].strip()
        
        # Join all sequence lines to one string; conv to uppercase; remv whitespace
        seq = "".join(s.upper().strip() for s in next(fa_iter))
        
        yield header, seq


#---- read_genome
def read_genome(fasta_file):
    
    gc = 0
    total_len = 0
    
    contig_lens = []
    scaffold_lens = []
    
    # Ignore header information (the '_' part) and process sequence data
    for _, seq in fasta_iter(fasta_file):
        
        # Add sequence (scaffold) length
        scaffold_lens.append(len(seq))
        # NN reprs gaps in scaffold, which are contigs
        if "NN" in seq:
            # Add split sequences to contig list if gap
            contig_list = seq.split("NN")
            
        else:
            # Add sequence to contig list
            contig_list = [seq]
            
        for contig in contig_list:
            # An initial check for 0-length contigs
            if len(contig):
              gc += contig.count('G') + contig.count('C')
              # Update the total length
              total_len += len(contig)
              # Add  length to list of contig lengths
              contig_lens.append(len(contig))
    # GC content as the percentage of total genome
    gc_cont = (gc / total_len) * 100

    return contig_lens, scaffold_lens, gc_cont


#---- calculate_stats()
def calculate_stats(seq_lens, gc_cont):
    
    # Empty dictionary
    stats = {}
    # The set of sequence lengths are converted to a NumPy array
    seq_array = np.array(seq_lens)
    
    # Count the individual sequences
    stats['sequence_count'] = seq_array.size
    
    # GC proportion
    stats['gc_content'] = gc_cont

    # Sort lengths by descending order
    sorted_lens = seq_array[np.argsort(-seq_array)]
    
    # The first length is the longest due to sorting
    stats['longest'] = int(sorted_lens[0])
    
    # Likewise, shortest length is at the end
    stats['shortest'] = int(sorted_lens[-1])
    
    stats['median'] = np.median(sorted_lens)
    
    stats['mean'] = np.mean(sorted_lens)
    
    # Sums the total length of all sequences
    stats['total_bps'] = int(np.sum(sorted_lens))
    
    # An array of cumulative sums to calculate N50 efficiently
    csum = np.cumsum(sorted_lens)
    
    for level in [10, 20, 30, 40, 50]:
        
        # Calculate target base pair count for the level
        nx = int(stats['total_bps'] * (level / 100))
        
        # Find smallest bp value in array, >= to the target %
        csumn = min(csum[csum >= nx])
        
        """
        
        --- The original code in the next line:
  
          l_level = int(np.where(csum == csumn)[0])
          
        --- Has been changed to:
            
          l_level = int(np.where(csum == csumn)[0][0])

        This finds the index where the cumulative sum equals csumn, which 
        represents the number of sequences needed to reach the target 
        percentage of base pairs. 
        
        I've added an extra [0] to fix the NumPy deprecation warning. This 
        ensures return of a scalar value from the array, as the extra '[0]' 
        ensures the first element of the first array is being accessed.
        
        The console warning (in Rstudio) that's now been resolved: 
        
          'Conversion of an array with ndim > 0 to a scalar is deprecated, and 
          will error in future. Ensure you extract a single element from your 
          array before performing this operation. (Deprecated NumPy 1.25.)'
          
        """
        
        # Determine the index where the sequences required to reach target % of bps is met
        l_level = int(np.where(csum == csumn)[0][0])
        
        # Get bp length of seq at index, l_level, for the N-statistic value
        n_level = int(sorted_lens[l_level])
        
        stats['L' + str(level)] = l_level

        # Store the statistic in a dictionary, mapped to its new name key
        stats['N' + str(level)] = n_level
        
    return stats


#---- assemblyDictionary
def assemblyDictionary(infilename):
    
    # Return two np arrays of lengths
    contig_lens, scaffold_lens, gc_cont = read_genome(infilename)
    
    # Return contig stats from contig lengths
    contig_stats = calculate_stats(contig_lens, gc_cont)
    
    # Return scaffold stats from scaffold lengths
    scaffold_stats = calculate_stats(scaffold_lens, gc_cont)
    
    # A dictionary of outputs is easily queried
    stat_output = {'Contig Stats': contig_stats,
                   'Scaffold Stats': scaffold_stats}
    
    return stat_output

