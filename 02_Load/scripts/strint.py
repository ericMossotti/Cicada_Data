"""
Format string representation of an integer value
as a comma separated string
"""

import pandas as pd

# Format output with comma seperator for thousands place
def strint (df, category, label):
    stat = df.loc[(category, label), "Value"]
    stat = pd.to_numeric(stat, downcast = "integer")
    stat = f'{stat:,}'
    
    return stat 
