import os
import csv
import re
import subprocess
import hashlib
import glob
try:
    from tqdm import tqdm
    TQDM_AVAILABLE = True
except ImportError:
    TQDM_AVAILABLE = False
    print("Warning: tqdm library not found. Progress bar will not be displayed.")
    print("To install tqdm, run: pip install tqdm")

class CSVRawImport:
    @staticmethod
    def mysql_string_rename(column_name):
        """
        Convert a string to a MySQL-friendly column name:
        - Convert special characters and spaces to underscores
        - Prefix with underscore if the first character is a digit
        - Limit to 60 characters
        
        Args:
            column_name (str): The original column name
            
        Returns:
            str: MySQL-friendly column name
        """
        # Replace special characters and spaces with underscores
        renamed = re.sub(r'[^a-zA-Z0-9]', '_', column_name)
        
        # Prefix with underscore if the first character is a digit
        if renamed and renamed[0].isdigit():
            renamed = '_' + renamed
            
        # Limit to 60 characters
        return renamed[:60]
    
    @staticmethod
    def fromFileToLoadDataSQL(full_path_to_csv_file):
        """
        Process a CSV file and generate SQL statements for importing the data into a MySQL database.
        Uses a caching mechanism to avoid recalculating column lengths for previously processed headers.
        
        Args:
            full_path_to_csv_file (str): Full path to the CSV file
            
        Returns:
            list: List of SQL statements
            
        Raises:
            FileNotFoundError: If the CSV file does not exist
            ValueError: If the CSV file is empty or has inconsistent column counts
        """
        # Verify that the CSV file exists and is readable
        if not os.path.isfile(full_path_to_csv_file):
            raise FileNotFoundError(f"CSV file not found: {full_path_to_csv_file}")
        
        print(f"Studying CSV file: {os.path.basename(full_path_to_csv_file)}")

        # Get file size for progress bar
        file_size = os.path.getsize(full_path_to_csv_file)
        print(f"File size: {file_size / (1024 * 1024):.2f} MB")

        # Count the number of lines in the file using wc -l command
        result = subprocess.run(['wc', '-l', full_path_to_csv_file], capture_output=True, text=True)
        line_count = int(result.stdout.strip().split()[0])        
        print(f"Line count: {line_count:,} lines")
        
        # Read just the header line to calculate MD5 hash
        with open(full_path_to_csv_file, 'r', newline='') as csvfile:
            header_line = csvfile.readline()
            if not header_line:
                raise ValueError("CSV file is empty")
            
            # Parse header row
            header_row = next(csv.reader([header_line]))
            
            # Convert column names to MySQL-friendly names
            column_names = [CSVRawImport.mysql_string_rename(col) for col in header_row]
            
            # Create lowercase header string for MD5 calculation
            lowercase_header = ','.join([h.lower() for h in header_row])
            
            # Calculate MD5 hash of the lowercase header
            md5_hash = hashlib.md5(lowercase_header.encode()).hexdigest()
            
            # Check if cached CREATE TABLE SQL exists
            cache_dir = "create_table_sql_cache"
            cache_pattern = os.path.join(cache_dir, f"{md5_hash}.*.sql")
            
            # Ensure cache directory exists
            if not os.path.exists(cache_dir):
                os.makedirs(cache_dir)
            
            # Initialize SQL statements list
            sql_statements = []
            
            # CREATE DATABASE statement
            sql_statements.append("CREATE DATABASE IF NOT EXISTS REPLACE_ME_DB_NAME;")
            
            # DROP TABLE statement
            sql_statements.append("DROP TABLE IF EXISTS REPLACE_ME_DB_NAME.REPLACE_ME_TABLE_NAME;")
            
            # Check if cached CREATE TABLE SQL exists using glob pattern
            cache_files = glob.glob(cache_pattern)
            
            if cache_files:
                # Use the first matching file
                cache_file = cache_files[0]
                print(f"Found cached CREATE TABLE SQL for this header structure: {cache_file}")
                
                # Load CREATE TABLE SQL from cache
                with open(cache_file, 'r') as f:
                    create_table_sql = f.read()
                
                sql_statements.append(create_table_sql)
            else:
                print(f"No cached CREATE TABLE SQL found. Analyzing CSV file to determine column lengths...")
                
                # Read the CSV file to determine column lengths
                with open(full_path_to_csv_file, 'r', newline='') as full_csvfile:
                    # Create a progress bar if tqdm is available
                    if TQDM_AVAILABLE:
                        pbar = tqdm(total=file_size, unit='B', unit_scale=True, desc="Learning: ")
                    
                    # Skip the header line (we already read it)
                    full_csvfile.readline()
                    
                    # Track position after reading header
                    current_position = len(header_line)
                    if TQDM_AVAILABLE:
                        pbar.update(current_position)
                    
                    # Initialize dictionary to track maximum length of data in each column
                    max_lengths = {col: 0 for col in column_names}
                    
                    # Read the first data line to ensure the file has at least one data row
                    first_data_line = full_csvfile.readline()
                    if not first_data_line:
                        raise ValueError("CSV file does not contain any data rows")
                    
                    # Update position after reading first data line
                    current_position += len(first_data_line)
                    if TQDM_AVAILABLE:
                        pbar.update(len(first_data_line))
                    
                    # Parse first data row
                    first_data_row = next(csv.reader([first_data_line]))
                    
                    # Check if the first data row has the same number of columns as the header
                    if len(first_data_row) != len(header_row):
                        raise ValueError(f"Inconsistent column count: Header has {len(header_row)} columns, but data row has {len(first_data_row)} columns")
                    
                    # Update max lengths based on the first data row
                    for i, value in enumerate(first_data_row):
                        max_lengths[column_names[i]] = max(max_lengths[column_names[i]], len(value))
                    
                    # Process the rest of the data rows
                    row_number = 2  # Start from 2 because we've already processed the header (1) and first data row
                    
                    # Read and process the rest of the file line by line
                    for line in full_csvfile:
                        # Update position
                        line_length = len(line)
                        current_position += line_length
                        
                        # Update progress bar
                        if TQDM_AVAILABLE:
                            pbar.update(line_length)
                        
                        # Parse the line
                        row = next(csv.reader([line]))
                        row_number += 1
                        
                        # Check if the row has the same number of columns as the header
                        if len(row) != len(header_row):
                            raise ValueError(f"Inconsistent column count at row {row_number}: Header has {len(header_row)} columns, but data row has {len(row)} columns")
                        
                        # Update max lengths
                        for i, value in enumerate(row):
                            max_lengths[column_names[i]] = max(max_lengths[column_names[i]], len(value))
                    
                    # Close the progress bar when done
                    if TQDM_AVAILABLE:
                        pbar.close()
                
                # CREATE TABLE statement
                create_table_sql = "CREATE TABLE REPLACE_ME_DB_NAME.REPLACE_ME_TABLE_NAME (\n"
                for i, col in enumerate(column_names):
                    # Add 1 to the max length to ensure there's room for the data
                    varchar_length = max_lengths[col] + 1
                    create_table_sql += f"    `{col}` VARCHAR({varchar_length})"
                    if i < len(column_names) - 1:
                        create_table_sql += ","
                    create_table_sql += "\n"
                create_table_sql += ");"
                
                # Add CREATE TABLE SQL to statements list
                sql_statements.append(create_table_sql)
                
                # Save CREATE TABLE SQL to cache with default name
                cache_file = os.path.join(cache_dir, f"{md5_hash}.replace_me.sql")
                print(f"Saving CREATE TABLE SQL to cache: {cache_file}")
                with open(cache_file, 'w') as f:
                    f.write(create_table_sql)
        
        # LOAD DATA LOCAL INFILE statement
        load_data_sql = """LOAD DATA LOCAL INFILE 'REPLACE_ME_CSV_FULL_PATH'
INTO TABLE REPLACE_ME_DB_NAME.REPLACE_ME_TABLE_NAME
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\\n'
IGNORE 1 LINES
("""
        
        # Use @var for each column to read into user variables
        load_data_sql += ", ".join([f"@{col}" for col in column_names])
        load_data_sql += ")\n"
        load_data_sql += "SET\n"
        
        # Add SET statements to assign from user variables and handle empty cells as NULL
        set_statements = []
        for col in column_names:
            set_statements.append(f"`{col}` = NULLIF(@{col}, '')")
        
        load_data_sql += ",\n".join(set_statements)
        load_data_sql += ";"
        
        sql_statements.append(load_data_sql)
        
        return sql_statements
