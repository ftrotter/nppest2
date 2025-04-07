# nppest2
NPPEST is a long-time project to specifically highlight ongoing data problems in NPPES. 

* It includes a simplified import script, to get the [NPPES data download](https://download.cms.gov/nppes/NPI_Files.html) into a MySQL database.
* Based on the contents of the database it has a series of expectations, expressed using [Great Expectations](https://greatexpectations.io/)
* That will details the current internal inconistencies within the NPPES dataset. 

## usage

* download a current monthly version of the nppes data, and unzip it into ./data/your_nppes_data_month/
* run `python import_nppes_dir.py ./data/your_nppes_data_month/
* 
