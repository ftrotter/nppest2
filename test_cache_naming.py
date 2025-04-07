#!/usr/bin/env python3
import os
import sys
import glob
from CSVRawImport import CSVRawImport

def test_cache_naming():
    """
    Test the cache naming functionality of CSVRawImport.
    
    This script verifies that the CSVRawImport class can find and load
    cache files with human-readable names.
    """
    # Create a simple CSV file for testing
    test_csv_path = "test_cache_naming.csv"
    
    # Create a simple CSV file with a consistent header
    with open(test_csv_path, 'w') as f:
        # Write header
        f.write("Column1,Column2,Column3\n")
        # Write a sample data row
        f.write("data1,data2,data3\n")
    
    print(f"Created test CSV file: {test_csv_path}")
    
    # Check if a cache file already exists for this CSV
    cache_dir = "create_table_sql_cache"
    
    # First run: Generate the cache file
    print("\nFirst run: Generating cache file...")
    try:
        sql_statements = CSVRawImport.fromFileToLoadDataSQL(test_csv_path)
        print("Cache file generated successfully.")
        
        # Find the generated cache file
        cache_files = glob.glob(os.path.join(cache_dir, "*.sql"))
        
        # Find the most recently created cache file
        latest_cache_file = max(cache_files, key=os.path.getctime)
        
        # Get the MD5 hash from the filename
        md5_hash = os.path.basename(latest_cache_file).split('.')[0]
        
        print(f"Generated cache file: {latest_cache_file}")
        print(f"MD5 hash: {md5_hash}")
        
        # Rename the cache file to add a human-readable part
        human_readable_name = "test_human_readable"
        new_cache_file = os.path.join(cache_dir, f"{md5_hash}.{human_readable_name}.sql")
        
        # Rename the file
        os.rename(latest_cache_file, new_cache_file)
        print(f"Renamed cache file to: {new_cache_file}")
        
        # Second run: Verify that the renamed cache file is found and loaded
        print("\nSecond run: Verifying cache file loading...")
        sql_statements = CSVRawImport.fromFileToLoadDataSQL(test_csv_path)
        
        # Check if the CREATE TABLE SQL was loaded from cache
        create_table_found = False
        for sql in sql_statements:
            if sql.startswith("CREATE TABLE"):
                create_table_found = True
                break
        
        if create_table_found:
            print("\nSUCCESS: CSVRawImport successfully loaded the CREATE TABLE SQL from the renamed cache file.")
        else:
            print("\nERROR: CSVRawImport did not load the CREATE TABLE SQL from cache.")
        
        # Clean up
        if os.path.exists(new_cache_file):
            os.remove(new_cache_file)
            print(f"Cleaned up test cache file: {new_cache_file}")
        
    except Exception as e:
        print(f"\nERROR: An exception occurred: {e}")
    finally:
        # Clean up the test CSV file
        if os.path.exists(test_csv_path):
            os.remove(test_csv_path)
            print(f"Cleaned up test CSV file: {test_csv_path}")

if __name__ == "__main__":
    test_cache_naming()
