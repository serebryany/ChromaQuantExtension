import pytest
import pandas as pd
import io
from csv_man_loader import load_manual_csv #this is the function to be tested from the csv_loader.py file

def test_upload():
    # Simulate a CSV file with correct columns
    csv_data = io.StringIO("ret,name,formula,Area,Mass of liq (mg)\n1,Sample1,H2O,50,10.5\n2,Sample2,C6H12O6,30,5.2") #this is the csv data to be tested (not a real csv)

    # Test successful load
    df = load_manual_csv(csv_data)
    
    # Assert DataFrame is not empty
    assert not df.empty  
    
    # Assert correct column names
    expected_columns = ["ret", "name", "formula", "Area", "Mass of liq (mg)"]
    assert list(df.columns) == expected_columns  

    # Test failure when no file is provided
    with pytest.raises(ValueError, match="No file provided"):
        load_manual_csv(None)