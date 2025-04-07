-- There should be no repeating taxonomy within the same state. This is done to provide additional "licensing" data, but these should be "indentifiers"
CREATE TABLE should_be_no_redundant_taxonomies 
SELECT firstone.*  
FROM taxonomies_normalized AS firstone 
JOIN taxonomies_normalized AS secondone ON (
	firstone.npi = secondone.npi 
		AND
	firstone.Healthcare_Provider_Taxonomy_Code = 
	secondone.Healthcare_Provider_Taxonomy_Code
		AND 
	firstone.tax_position != 
	secondone.tax_position
		AND
	firstone.Provider_License_Number_State_Code IS NULL
		AND 
	firstone.Provider_License_Number IS NULL

	)
