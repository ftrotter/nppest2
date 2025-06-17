#!/usr/bin/env python3
import os
import re
import sys
import argparse
import pymysql
from typing import List
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from CSVRawImport import CSVRawImport

class ImportRawCSVFile:
    @staticmethod
    def import_raw_csv_file(csvfilepath: str, db: str, table: str) -> None:
        """
        Import a CSV file into a MySQL database table.
        
        Args:
            csvfilepath (str): Full path to the CSV file
            db (str): Database name
            table (str): Table name
            
        Raises:
            ValueError: If db or table name is invalid
            FileNotFoundError: If the CSV file does not exist
            Exception: If there's an error executing SQL
        """
        # Validate db and table names
        if not re.match(r'^[a-zA-Z][a-zA-Z0-9_]*$', db):
            raise ValueError("Database name must begin with an alpha character and contain only alphanumeric characters and underscores")
        
        if not re.match(r'^[a-zA-Z][a-zA-Z0-9_]*$', table):
            raise ValueError("Table name must begin with an alpha character and contain only alphanumeric characters and underscores")
        
        # Load environment variables
        load_dotenv()
        
        # Get database connection details from environment variables
        db_connection = os.getenv('DB_CONNECTION', 'mysql')
        db_host = os.getenv('DB_HOST', 'localhost')
        db_port = os.getenv('DB_PORT', '3306')
        db_username = os.getenv('DB_USERNAME', '')
        db_password = os.getenv('DB_PASSWORD', '')
        
        # Check if we have valid database credentials
        has_valid_credentials = db_username and db_password
        
        try:
            # Generate SQL statements using CSVRawImport
            sql_statements = CSVRawImport.fromFileToLoadDataSQL(csvfilepath)
            
            # Replace placeholders in SQL statements
            for i in range(len(sql_statements)):
                sql_statements[i] = sql_statements[i].replace('REPLACE_ME_CSV_FULL_PATH', csvfilepath)
                sql_statements[i] = sql_statements[i].replace('REPLACE_ME_DB_NAME', db)
                sql_statements[i] = sql_statements[i].replace('REPLACE_ME_TABLE_NAME', table)
            
            # If we have valid credentials, execute the SQL statements
            if has_valid_credentials:
                # Create SQLAlchemy engine with PyMySQL
                connection_string = f"{db_connection}+pymysql://{db_username}:{db_password}@{db_host}:{db_port}"
                # Add local_infile=True to enable LOAD DATA LOCAL INFILE capability
                engine = create_engine(connection_string, echo=False, connect_args={"local_infile": True})
                
                # Execute SQL statements
                with engine.connect() as connection:
                    for sql in sql_statements:
                        print(f"Executing SQL: {sql}")
                        try:
                            connection.execute(text(sql))
                            connection.commit()
                            print("SQL executed successfully")
                        except Exception as e:
                            print(f"Error executing SQL: {e}")
                            # Stop execution if there's an error
                            sys.exit(1)
                    
                print(f"CSV file {csvfilepath} successfully imported into {db}.{table}")
            else:
                # Just print the SQL statements without executing them
                print("\nNo valid database credentials found in .env file.")
                print("Generating SQL statements without executing them:\n")
                for sql in sql_statements:
                    print(f"{sql}\n")
                print(f"SQL statements for importing {csvfilepath} into {db}.{table} have been generated.")
                print("To execute these statements, add valid database credentials to your .env file and run this script again.")
            
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

def main():
    """
    Main function to parse command line arguments and call the import function.
    """
    parser = argparse.ArgumentParser(description='Import a CSV file into a MySQL database table')
    parser.add_argument('--csvfilepath', required=True, help='Full path to the CSV file')
    parser.add_argument('--db', required=True, help='Database name')
    parser.add_argument('--table', required=True, help='Table name')
    
    args = parser.parse_args()
    
    try:
        ImportRawCSVFile.import_raw_csv_file(args.csvfilepath, args.db, args.table)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
