""" Formats the string representation of an 
integer value as a comma separated string. """

import pandas as pd
import re


# Format output with comma seperator for thousands place
def strint (dataframe, category, label):
    
    # Find the desired value
    stat = dataframe.loc[(category, label), "Value"]
    
    # Set boolean match value
    isFloat = re.search(r"\.", stat)
    
    # Convert to float if there is a decimal
    if isFloat:
        stat = pd.to_numeric(stat, downcast = "float")
    else:
        # Else convert to an integer 
        stat = pd.to_numeric(stat, downcast = "integer")
        
    # Add a thousands seperator and convert back to a string
    stat = f'{stat:,}'
    
    return stat 
