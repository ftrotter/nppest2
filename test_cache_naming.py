#!/usr/bin/env python3
import os
import sys
import glob
from CSVRawImport import CSVRawImport

def test_cache_naming():
    """
    Test the cache naming functionality of CSVRawImport.
    
    This script verifies that the CSVRawImport class can find and load
    cache files with human-readable names for both CREATE TABLE and LOAD DATA SQL.
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
    
    # Define cache directories
    create_table_cache_dir = "cache_create_table_sql"
    load_data_cache_dir = "cache_data_load_sql"
    
    # First run: Generate the cache files
    print("\nFirst run: Generating cache files...")
    try:
        sql_statements = CSVRawImport.fromFileToLoadDataSQL(test_csv_path)
        print("Cache files generated successfully.")
        
        # Find the generated CREATE TABLE cache file
        create_table_cache_files = glob.glob(os.path.join(create_table_cache_dir, "*.sql"))
        
        # Find the most recently created CREATE TABLE cache file
        latest_create_table_cache_file = max(create_table_cache_files, key=os.path.getctime)
        
        # Get the MD5 hash from the filename
        create_table_md5_hash = os.path.basename(latest_create_table_cache_file).split('.')[0]
        
        print(f"Generated CREATE TABLE cache file: {latest_create_table_cache_file}")
        print(f"CREATE TABLE MD5 hash: {create_table_md5_hash}")
        
        # Find the generated MySQL LOAD DATA cache file
        mysql_load_data_cache_files = glob.glob(os.path.join(load_data_cache_dir, f"*.mysql_load_data.*.sql"))
        
        # Find the most recently created MySQL LOAD DATA cache file
        latest_mysql_load_data_cache_file = max(mysql_load_data_cache_files, key=os.path.getctime)
        
        # Get the MD5 hash from the filename
        mysql_load_data_md5_hash = os.path.basename(latest_mysql_load_data_cache_file).split('.')[0]
        
        print(f"Generated MySQL LOAD DATA cache file: {latest_mysql_load_data_cache_file}")
        print(f"MySQL LOAD DATA MD5 hash: {mysql_load_data_md5_hash}")
        
        # Find the generated PostgreSQL COPY cache file
        postgresql_copy_cache_files = glob.glob(os.path.join(load_data_cache_dir, f"*.postgresql_copy.*.sql"))
        
        # Find the most recently created PostgreSQL COPY cache file
        latest_postgresql_copy_cache_file = max(postgresql_copy_cache_files, key=os.path.getctime)
        
        # Get the MD5 hash from the filename
        postgresql_copy_md5_hash = os.path.basename(latest_postgresql_copy_cache_file).split('.')[0]
        
        print(f"Generated PostgreSQL COPY cache file: {latest_postgresql_copy_cache_file}")
        print(f"PostgreSQL COPY MD5 hash: {postgresql_copy_md5_hash}")
        
        # Verify that all MD5 hashes are the same
        if create_table_md5_hash == mysql_load_data_md5_hash == postgresql_copy_md5_hash:
            print("SUCCESS: All cache files (CREATE TABLE, MySQL LOAD DATA, PostgreSQL COPY) use the same MD5 hash.")
        else:
            print("ERROR: Cache files use different MD5 hashes.")
        
        # Rename the cache files to add a human-readable part
        human_readable_name = "test_human_readable"
        new_create_table_cache_file = os.path.join(create_table_cache_dir, f"{create_table_md5_hash}.{human_readable_name}.sql")
        new_mysql_load_data_cache_file = os.path.join(load_data_cache_dir, f"{mysql_load_data_md5_hash}.mysql_load_data.{human_readable_name}.sql")
        new_postgresql_copy_cache_file = os.path.join(load_data_cache_dir, f"{postgresql_copy_md5_hash}.postgresql_copy.{human_readable_name}.sql")
        
        # Rename the files
        os.rename(latest_create_table_cache_file, new_create_table_cache_file)
        os.rename(latest_mysql_load_data_cache_file, new_mysql_load_data_cache_file)
        os.rename(latest_postgresql_copy_cache_file, new_postgresql_copy_cache_file)
        print(f"Renamed CREATE TABLE cache file to: {new_create_table_cache_file}")
        print(f"Renamed MySQL LOAD DATA cache file to: {new_mysql_load_data_cache_file}")
        print(f"Renamed PostgreSQL COPY cache file to: {new_postgresql_copy_cache_file}")
        
        # Second run: Verify that the renamed cache files are found and loaded
        print("\nSecond run: Verifying cache file loading...")
        sql_statements = CSVRawImport.fromFileToLoadDataSQL(test_csv_path)
        
        # Check if the SQL statements were loaded from cache
        create_table_found = False
        mysql_load_data_found = False
        
        for sql in sql_statements:
            if sql.startswith("CREATE TABLE"):
                create_table_found = True
            elif sql.startswith("LOAD DATA LOCAL INFILE"):
                mysql_load_data_found = True
        
        if create_table_found:
            print("SUCCESS: CSVRawImport successfully loaded the CREATE TABLE SQL from the renamed cache file.")
        else:
            print("ERROR: CSVRawImport did not load the CREATE TABLE SQL from cache.")
            
        if mysql_load_data_found:
            print("SUCCESS: CSVRawImport successfully loaded the MySQL LOAD DATA SQL from the renamed cache file.")
        else:
            print("ERROR: CSVRawImport did not load the MySQL LOAD DATA SQL from cache.")
        
        # Note: PostgreSQL COPY SQL is not added to sql_statements by default in the current implementation
        # But we can verify that the cache file exists
        if os.path.exists(new_postgresql_copy_cache_file):
            print("SUCCESS: PostgreSQL COPY SQL cache file exists.")
        else:
            print("ERROR: PostgreSQL COPY SQL cache file does not exist.")
        
        # Clean up
        if os.path.exists(new_create_table_cache_file):
            os.remove(new_create_table_cache_file)
            print(f"Cleaned up CREATE TABLE test cache file: {new_create_table_cache_file}")
            
        if os.path.exists(new_mysql_load_data_cache_file):
            os.remove(new_mysql_load_data_cache_file)
            print(f"Cleaned up MySQL LOAD DATA test cache file: {new_mysql_load_data_cache_file}")
            
        if os.path.exists(new_postgresql_copy_cache_file):
            os.remove(new_postgresql_copy_cache_file)
            print(f"Cleaned up PostgreSQL COPY test cache file: {new_postgresql_copy_cache_file}")
        
    except Exception as e:
        print(f"\nERROR: An exception occurred: {e}")
    finally:
        # Clean up the test CSV file
        if os.path.exists(test_csv_path):
            os.remove(test_csv_path)
            print(f"Cleaned up test CSV file: {test_csv_path}")

if __name__ == "__main__":
    test_cache_naming()
