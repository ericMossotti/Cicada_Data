""" Utilizes Python string methods and multi-indexing 
to process assembly_stats' output text file """

import pandas as pd
import re

def assemblyFramer(statsPath = None):
    
    #---- Read Text File
    with open(statsPath, 'r') as file:
        content = file.read()
        
    #---- Regex Matching
    pairs = re.findall(r"\"\w+\"\:\s\d*\.?\d*", content)
    
    #---- Clean Strings
    cleaned_list = [pair.replace('"', '').replace(':', '').strip() for pair in pairs]
    
    #---- Split Strings
    labeled_list = [item.split() for item in cleaned_list]
    
    #---- Create DataFrame
    df = pd.DataFrame(labeled_list, columns = ['Label', 'Value'])
    
    #---- Add Category Column
    df['Category'] = ['Contigs'] * 17 + ['Scaffolds'] * 17
    
    #---- Create Arrays
    category_array = pd.Series.to_list(df['Category'])
    label_array = pd.Series.to_list(df['Label'])
    value_array = pd.Series.to_list(df['Value'])
    
    #---- Combine Arrays to List
    arrayList = [category_array, label_array]
    
    #---- Define Multi-Level Indices
    indices = pd.MultiIndex.from_arrays(arrays = arrayList, names = ('Category', 'Label'))
    
    #---- Index a DataFrame 
    df_indexed = pd.DataFrame(data = value_array, index = indices)
    
    #---- Rename Non-Indexed Column
    df_indexed = df_indexed.rename(columns = {0:"Value"})
    
    return df_indexed
