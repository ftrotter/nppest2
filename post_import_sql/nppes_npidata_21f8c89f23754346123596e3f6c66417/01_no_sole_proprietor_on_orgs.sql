-- there should be no sole proprietors on organizational records
CREATE TABLE should_be_no_org_sole_proprietor
SELECT npi, Is_Sole_Proprietor 
FROM npidata 
WHERE Entity_Type_Code = 2
AND Is_Sole_Proprietor IS NOT NULL
