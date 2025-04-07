-- There should be no entity type codes other than 1 and 2 
CREATE TABLE REPLACE_ME_DB_NAME.should_be_no_records_with_bad_entity_type_code
SELECT * FROM REPLACE_ME_DB_NAME.npidata 
WHERE `Entity_Type_Code` IS NOT NULL
AND Entity_Type_Code != '1' 
AND Entity_Type_Code != '2'
AND Entity_Type_Code != 1 
AND Entity_Type_Code != 2
