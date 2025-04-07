-- How many distinct values for credentials are there
CREATE TABLE study_distinct_credentials
SELECT 
	'Provider_Credential_Text                        ' AS field_source,
	Provider_Credential_Text,
	COUNT(*) AS row_count
FROM npidata
GROUP BY Provider_Credential_Text
;
INSERT INTO study_distinct_credentials
SELECT 
	'Provider_Other_Credential_Text' AS field_source,
	Provider_Other_Credential_Text,
	COUNT(*) AS row_count
FROM npidata
GROUP BY Provider_Other_Credential_Text
;
INSERT INTO study_distinct_credentials
SELECT 'Authorized_Official_Credential_Text' AS field_source,
	Authorized_Official_Credential_Text,
	COUNT(*) AS row_count
FROM npidata
GROUP BY Authorized_Official_Credential_Text
;
 
