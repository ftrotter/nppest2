# nppest2
NPPEST is a long-time project to specifically highlight ongoing data problems in NPPES. 

* It includes a simplified import script, to get the [NPPES data download](https://download.cms.gov/nppes/NPI_Files.html) into a MySQL database.
* Based on the contents of the database it has a series of expectations, expressed using [Great Expectations](https://greatexpectations.io/)
* That will details the current internal inconistencies within the NPPES dataset. 

## usage

* download a current monthly version of the nppes data, and unzip it into ./data/your_nppes_data_month/
* Import the raw data using variations on the following commands
* python import_raw_csv_file.py --csvfilepath=./data/unzipped/endpoint_pfile_20050523-YOURDATEHERE.csv --db=raw_nppes --table=endpoint 
* python import_raw_csv_file.py --csvfilepath=./data/unzipped/othername_pfile_20050523-YOURDATEHERE.csv --db=raw_nppes --table=othername 
* python import_raw_csv_file.py --csvfilepath=./data/unzipped/pl_pfile_20050523-YOURDATEHERE.csv --db=raw_nppes --table=practicelocation 
* python import_raw_csv_file.py --csvfilepath=./data/unzipped/npidata_pfile_20050523-YOURDATEHERE.csv --db=raw_nppes --table=npidata 



