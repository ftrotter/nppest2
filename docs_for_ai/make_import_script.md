Make the csv import script
=============

Please place the import script in import_raw_csv_file.py

* The import script is both a command line script and a class with single static function called import_raw_csv_file
* The script can be called from the command line directly, or it can be imported into another python script which can then use its static function.
* when called from the command line, this script accepts several flagged arguments. csvfilepath= is the full path of the csv file, db = database to import to and table= is the tablename to import to
* Uses the CSVRawImport.py class to generate the SQL needed to import the CSV file. 
* Create a SQL alchemy engine connection using the sql credentials found in the .env file (look in template_env.txt for the specific variable names there). This function will return a list of SQL commands
* each SQL command in the list will contain three strings, which need to be replaced with the arguments: REPLACE_ME_CSV_FULL_PATH, REPLACE_ME_DB_NAME, and REPLACE_ME_TABLE_NAME
* The db and table name arguments should begin with a alpha character, have no spaces or special characters other than underscore. Through an error if this rule is not followed.
* print and then execute the SQL commands one at a time in order, and display an error that results. If there is a SQL error, stop execution of the program.
