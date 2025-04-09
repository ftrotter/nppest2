# NPPEST2
NPPEST is a long-time project to specifically highlight ongoing data problems in NPPES.
The previous version was written in PHP, but this version has been updated to run in python. 

* It includes a simplified import script, to get the [NPPES data download](https://download.cms.gov/nppes/NPI_Files.html) into a MySQL database.

* Then there are series of queries which detail the current internal inconistencies within the NPPES public use file.

## Usage

* download a current monthly version of the nppes data, and unzip it into ./data/your_nppes_data_month/
* copy template_env.txt to .env and modify its contents to connect to a MySQL/MariaDB database.
* Import the raw data using variations on the following commands
* python import_raw_csv_file.py --csvfilepath=./data/unzipped/endpoint_pfile_20050523-YOURDATEHERE.csv --db=raw_nppes --table=endpoint
* python import_raw_csv_file.py --csvfilepath=./data/unzipped/othername_pfile_20050523-YOURDATEHERE.csv --db=raw_nppes --table=othername
* python import_raw_csv_file.py --csvfilepath=./data/unzipped/pl_pfile_20050523-YOURDATEHERE.csv --db=raw_nppes --table=practicelocation
* python import_raw_csv_file.py --csvfilepath=./data/unzipped/npidata_pfile_20050523-YOURDATEHERE.csv --db=raw_nppes --table=npidata
* Then run all of the code in post_import_sql directory. Hopefully this too will someday be automated.
* This will generate a series of tables in your mysql database showing the various problems with the NPPES data.
* Run the create_problems_report.py script from the command line, to generate the ProblemsWithNPPES.md page dynamically.

## Problems with the NPPES data

Once the data is complete take a look at your updated [ProblemsWithNPPES.md](./ProblemsWithNPPES.md) file. You can always just look at the last run from the public version on github, but the version you download with this repo is likely to be out-of-date.

