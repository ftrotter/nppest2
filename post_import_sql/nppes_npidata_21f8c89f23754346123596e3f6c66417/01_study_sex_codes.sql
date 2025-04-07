-- What are the counts for the various sex codes?
CREATE TABLE REPLACE_ME_DB_NAME.study_provider_sex_code 
SELECT Provider_Sex_Code , COUNT(*) AS row_count 
FROM REPLACE_ME_DB_NAME.npidata 
GROUP BY Provider_Sex_Code; 
