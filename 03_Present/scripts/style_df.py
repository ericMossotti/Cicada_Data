#---- style_df(df, cap)

import pandas as pd

# Format a dataframe and add a caption to output
def style_df (df, cap):
    # Caption
    styled = df.style.set_caption(cap)
    # Separator string
    styled = styled.format(thousands=",")
    # Output styled dataframe
    return styled
