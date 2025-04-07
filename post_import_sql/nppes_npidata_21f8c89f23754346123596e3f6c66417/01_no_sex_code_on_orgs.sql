-- there should be no sex codes on organization
CREATE TABLE should_be_no_sex_codes_on_orgs 
SELECT npi, Provider_Sex_Code 
FROM npidata 
WHERE Entity_Type_Code = 2
AND Provider_Sex_Code IS NOT NULL
