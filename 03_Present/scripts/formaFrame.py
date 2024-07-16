"""
Returns a Style class object with adjusted properties.
"""

import pandas as pd

def formaFrame(styler):
    
    # Table caption
    styler.set_caption("Assembly Stats")
    
    # Hide index column headers
    styler.hide(axis = "index", names = True)
    
    # Hide value column headers
    styler.hide(axis = "columns", level = 0)
    
    return styler
