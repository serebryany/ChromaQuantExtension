import pytest
import pandas as pd
import os
import re
import sys


def get_file_patterns():
    return {
        r".+_.+_(LQ\d+|GS\d+)_(MS|TCD|FID)_SPEC\.csv": 2,  # FID, MS, and TCD SPEC files
        r".+_.+_(GS\d+|LQ\d+)_UA_UPP\.csv": {"Component RT", "Compound Name", "Formula", "Match Factor"},  # UA_UPP files
        r".+_.+_(LQ\d+|GS\d+)_TCD_CSO\.csv": {"Signal Name", "RT", "Area", "Height"}  # CSO files
    }

def get_matching_files():
    files = os.listdir()
    file_patterns = get_file_patterns()
    return [(file, pattern, expected) for file in files for pattern, expected in file_patterns.items() if re.match(pattern, file)]

@pytest.mark.parametrize("file, pattern, expected", get_matching_files())
def test_file_formats(file, pattern, expected):
    df = pd.read_csv(file)
    if isinstance(expected, int):  # Files that should have exactly two columns
        assert df.shape[1] == expected, f"File {file} does not have exactly {expected} columns"
    else:  # Files that should contain specific column names
        assert expected.issubset(set(df.columns)), f"File {file} is missing expected columns"
