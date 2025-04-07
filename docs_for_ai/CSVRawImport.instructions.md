Build CSVRawImport class
=======

Please help me create a CSVRawImport class in the CSVRawImport.py file

How to build CSVRawImport
-------

* The file /CSVRawImport.py should contain a class which contains a static function 'fromFileToLoadDataSQL'.
* fromFileToLoadDataSQL should accept a single argument: full_path_to_csv_file
* Verify that the csv file exists, and that it is readable and contains at least two lines of data (a header and one row of data). If it does throw an appropriate error.
* The first line of the csv file will contain its column names. Import this first line and convert all of the strings there into the column names using the mysql_string_rename function below
* Using the csv modile (import csv), loop over every line of the csv file. Maintain a dictionary, using the column names that are already calculated, to remember the maximum length of the data in each column.
* If any row of data in the csv file has more or less columns of data then the first row (i.e. the column header row), generate throw an appropriate error.
* The the function will generate a python list of sql strings.
* For all of the following sql statements going into this list, using REPLACE_ME_DB_NAME and REPLACE_ME_TABLE_NAME as the database and table names inside the SQL statements. Similary use REPLACE_ME_CSV_FULL_PATH for the csv file name. Do not assume the correct database has been selected in the sql connection. Always fully specify the REPLACE_ME_DB_NAME.REPLACE_ME_TABLE_NAME.  
* The SQL steps to include in the list are:
  * CREATE DATABASE IF NOT EXISTS for the REPLACE_ME_DB_NAME
  * DROP TABLE IF EXISTS for the REPLACE_ME_TABLE_NAME
  * CREATE TABLE Statement for the new table, using the specific column names calculated for the table. Always use the VARCHAR column type, and always use a VARCHAR length of exactly one character longer than longest string found in the CSV file for that column.
  * LOAD DATA LOCAL INFILE  statement as appropriate for a standard CSV file, with one line of header instead of data. Use the SET command for each column to ensure that when the csv contains a blank cell it is imported as a NULL in mysql, using the NULLIF function on each cell of data.
* Return the list of sql statements as the result of the function

mysql_string_rename static function
--------

* Convert any special characters in the string, including spaces, into underscore.
* If the first character of the string is a numeric digit, it should be prefixed with an underscore.
* Then it should take the first 60 characters of this calculated string and return this as the result
