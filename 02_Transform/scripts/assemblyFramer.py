"""
assemblyFramer.py

This script processes a JSON-structured file containing assembly statistics 
(e.g., contig and scaffold stats) and converts it into a multi-indexed Pandas 
DataFrame for easier analysis and manipulation.

The script is designed to handle file outputs similar to the 
`summary_stats.json` or `summary_stats.txt` in this project, as long as the 
content is valid JSON. It extracts key-value pairs from the JSON structure and 
organizes them into a DataFrame with a hierarchical index (Category and Label).

Author: Eric Mossotti
Date: 2025-03-12
Version: 1.0
CC-BY SA
"""

import pandas as pd
import json

def assemblyFramer(statsPath = None):
    """
    Reads a JSON-structured assembly stats file and returns a multi-index DataFrame.

    Parameters:
    -----------
    statsPath : str, optional
        The file path to the JSON-structured assembly stats file. Default is None.
        The file can have any extension (e.g., `.json`, `.txt`), but the content must be valid JSON.

    Returns:
    --------
    pd.DataFrame
        A Pandas DataFrame with a multi-index (Category, Label) and a single column "Value".
        The DataFrame contains all key-value pairs extracted from the input JSON file.

    Example:
    --------
    >>> df = assemblyFramer("summary_stats.json")
    >>> print(df)
                             Value
    Category Label                
    Contigs  L10                41
             L20                99
             L30               174
             L40               267
             L50               385
             N10          12643769
             N20           9681846
             N30           7895799
             N40           6288966
             N50           4902968
             gc_content  35.248104
             longest     43529772
             mean       1552486.99
             median        331935.0
             sequence_count   4200
             shortest         1000
             total_bps   6520445364
    Scaffolds L10                 0
             L20                 0
             L30                 1
             L40                 2
             L50                 3
             N10          1438277616
             N20          1438277616
             N30           915491830
             N40           607508155
             N50           518932092
             gc_content  35.248104
             longest     1438277616
             mean       3212576.534
             median        62362.5
             sequence_count   2030
             shortest         1000
             total_bps   6521530364
    """
    # Read the JSON file
    with open(statsPath, 'r') as file:
        data = json.load(file)
    
    # Prepare rows for the DataFrame
    rows = []
    for category_key, stats in data.items():
        # Convert "Contig Stats" to "Contigs", "Scaffold Stats" to "Scaffolds"
        category = category_key.split()[0] + 's'
        for label, value in stats.items():
            rows.append({
                'Category': category,
                'Label': label,
                'Value': value
            })
    
    # Create a DataFrame and set multi-index
    df = pd.DataFrame(rows)
    df.set_index(['Category', 'Label'], inplace=True)
    
    return df
