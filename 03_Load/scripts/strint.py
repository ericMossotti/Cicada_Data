
""" 
Formats the string representation of an 
integer value as a comma separated string 
"""

import pandas as pd
import re

def strint(data, category, label):
    if isinstance(data, pd.DataFrame):
        # Existing DataFrame handling code
        stat = data.loc[(category, label), "Value"]
        
        # Set boolean match value
        isFloat = re.search(r"\.", str(stat))
        
        # Convert to float if there is a decimal
        if isFloat:
            stat = pd.to_numeric(stat, downcast="float")
        else:
            # Else convert to an integer 
            stat = pd.to_numeric(stat, downcast="integer")
    
    elif isinstance(data, dict):
        # New dictionary handling code
        #stat = data.get(f"{category} {label}")
        stat = data[category][label]
        
        if stat is None:
            raise KeyError(f"Key '{category} {label}' not found in the dictionary")
        
        # No need to convert to numeric as values are already integers or floats
    
    else:
        raise TypeError("Input must be a pandas DataFrame or a dictionary")

    # Add a thousands separator and convert back to a string
    stat = f'{stat:,}'
    
    return stat
