#---- 

"""
This gives a color scheme that visually distinguishes the first level 
of the index while grouping rows by their second-level index across all columns. 
The column headers will also have colors from the same palette 
as the second-level index. 

One can adjust the color palettes and alpha values 
to fine-tune the appearance as needed.
"""

import pandas as pd
import seaborn as sns
import numpy as np


def formaFrame(df, color_dict1, color_dict2):
    
    # Apply the styling to indices
    styled_df = df.style.map_index(color_index, axis = 0)
    # Apply styling to the value column
    styled_df = styled_df.apply(color_values, axis = 0)
    
    # Return the styled df
    return styled_df

# To color the Value column the same as the Label index 
def color_values(s):
    
    return [color_to_rgba(color_dict2[idx[1]]) for idx in s.index]


# Create the rgb values
def color_to_rgba(color, alpha = 0.5):
    
    return f'background-color: rgba({", ".join(f"{int(c*255)}" for c in color)}, {alpha})'


def color_index(index):
    
    # For full multi-index, use color from first level
    if isinstance(index, tuple):
        # For full multi-index, use color from the first level
        return color_to_rgba(color_dict1[index[0]])
    
    elif index in color_dict1:
        return color_to_rgba(color_dict1[index])

    # For single-level indices, use the appropriate color dictionaries
    elif index in color_dict2:
        return color_to_rgba(color_dict2[index])
    
    else:
        return ''

