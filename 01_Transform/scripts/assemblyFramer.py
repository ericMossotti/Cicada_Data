
import pandas as pd
import re

""" Utilize Python string methods and multi-indexing 
to process assembly_stats' output text file """

def assemblyFramer(statsPath = None):

    
    # Read the file
    with open(statsPath, 'r') as file:
        content = file.read()
    
    pairs = re.findall(r"\"\w+\"\:\s\d*\.?\d*", content)
    
    cleaned_list = [pair.replace('"', '').replace(':', '').strip() for pair in pairs]
    
    labeled_list = [item.split() for item in cleaned_list]
    
    df = pd.DataFrame(labeled_list, columns=['Label', 'Value'])
    
    df['Category'] = ['Contigs'] * 17 + ['Scaffolds'] * 17
    
    category_array = pd.Series.to_list(df['Category'])
    label_array = pd.Series.to_list(df['Label'])
    value_array = pd.Series.to_list(df['Value'])
    
    arrayList = [category_array, label_array]
    indices = pd.MultiIndex.from_arrays(arrays = arrayList, names = ('Category', 'Label'))
    
    df_indexed = pd.DataFrame(data = value_array, index = indices)
    
    df_indexed = df_indexed.rename(columns={0:"Value"})
    
    return df_indexed
