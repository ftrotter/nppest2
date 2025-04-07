--  There should be no records that have blank entity_type_code
CREATE TABLE REPLACE_ME_DB_NAME.should_be_no_records_without_entity_type_code
SELECT * FROM REPLACE_ME_DB_NAME.npidata WHERE `Entity_Type_Code` IS NULL
