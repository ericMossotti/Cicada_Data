import pandas as pd

def formaFrame(styler):
    styler.set_caption("Assembly Stats")
    styler.hide(axis = "index", names = True)
    styler.hide(axis = "columns", level = 0)
    return styler
