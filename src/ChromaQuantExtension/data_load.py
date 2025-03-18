import pandas as pd
import argparse

def print_sheet_names(file_path):
    """Loads an Excel file and prints the names of all sheets."""
    xls = pd.ExcelFile(file_path)
    print(f"Sheet names in {file_path}: {xls.sheet_names}")

def extract_tables_from_sheet(file_path, sheet_name, is_manual=False):
    """Extracts multiple tables from a given Excel sheet and returns them as separate DataFrames."""
    
    # Load the entire sheet into a DataFrame
    xls = pd.ExcelFile(file_path)
    sheet_df = pd.read_excel(xls, sheet_name, header=None)  # Load without headers
    
    # Define table ranges for different sheets based on whether it's manual or QC
    if is_manual:
        table_ranges = {
            "Liquid": {
                "LiquidFID": sheet_df.iloc[2:47983, 1:3],
                "LiquidMS": sheet_df.iloc[2:47983, 3:5],
                "FIDPeaks": sheet_df.iloc[6:232, 6:21],
                "CompoundType": sheet_df.iloc[7:39, 22:29],
            },
            "Gas FID": {
                "LiquidFID": sheet_df.iloc[2:47983, 1:3],
                "LiquidMS": sheet_df.iloc[2:47983, 3:5],
                "FIDPeaks": sheet_df.iloc[7:81, 6:22],
                "CompoundType": sheet_df.iloc[26:47, 28:34],
                "GasFIDRF": sheet_df.iloc[2:22, 24:27],
            },
            "Gas TCD": {
                "GasTCD": sheet_df.iloc[4:17, 1:15]
            }
        }
    else:
        table_ranges = {
            "Liquid FID": {
                "main": sheet_df.iloc[4:295, 1:15],
                "summary": sheet_df.iloc[7:14, 16:19],
                "rxn_info": sheet_df.iloc[1:3, 1:21],
                "breakdown": sheet_df.iloc[1:6, 22:24],
                "postprocessed": sheet_df.iloc[7:42, 20:27],
                "CnMass": sheet_df.iloc[15:50, 16:18],
            },
            "Gas FID": {
                "main": sheet_df.iloc[4:295, 1:15],
                "summary": sheet_df.iloc[7:14, 16:19],
                "rxn_info": sheet_df.iloc[1:3, 1:21],
                "breakdown": sheet_df.iloc[1:6, 22:24],
                "postprocessed": sheet_df.iloc[7:42, 20:27],
                "CnMass": sheet_df.iloc[15:50, 16:18],
            },
            "Gas TCD": {
                "main": sheet_df.iloc[4:295, 1:15],
                "injection_data": sheet_df.iloc[4:17, 1:14],
            },
            "Total": {
                "total_table": sheet_df.iloc[1:36, 1:8],
            }
        }
    
    if sheet_name not in table_ranges:
        raise ValueError(f"Sheet '{sheet_name}' not found in predefined tables.")
    
    tables = table_ranges[sheet_name]
    
    # Assign column names from the first row of each table
    for key in tables:
        tables[key].columns = tables[key].iloc[0]  # Set first row as header
        tables[key] = tables[key][1:].reset_index(drop=True)  # Drop original header row
    
    return tables

def main():
    parser = argparse.ArgumentParser(description="Load and process QC and manually calculated Excel files.")
    parser.add_argument("--manual", type=str, required=True, help="Path to the manually calculated Excel file.")
    parser.add_argument("--cq", type=str, required=True, help="Path to the QC Excel file.")
    args = parser.parse_args()
    
    manual_file_path = args.manual
    cq_file_path = args.cq
    
    # Print sheet names
    print_sheet_names(manual_file_path)
    print_sheet_names(cq_file_path)
    
    # Define sheets to extract for both files
    sheets = ["Liquid", "Gas FID", "Gas TCD"]
    qc_sheets = ["Liquid FID", "Gas FID", "Gas TCD", "Total"]
    
    # Extract tables from manual file
    for sheet in sheets:
        print(f"\nExtracting tables from manual file: {sheet}...")
        tables = extract_tables_from_sheet(manual_file_path, sheet, is_manual=True)
        for name, df in tables.items():
            print(f"\n{name} table from {sheet}:")
            print(df.head())
    
    # Extract tables from QC file
    for sheet in qc_sheets:
        print(f"\nExtracting tables from QC file: {sheet}...")
        tables = extract_tables_from_sheet(cq_file_path, sheet, is_manual=False)
        for name, df in tables.items():
            print(f"\n{name} table from {sheet}:")
            print(df.head())
    
if __name__ == "__main__":
    main()

