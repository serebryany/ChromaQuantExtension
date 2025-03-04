import pandas as pd

def load_manual_csv(file):
    if file is None:
        raise ValueError("No file provided")
    return pd.read_csv(file)