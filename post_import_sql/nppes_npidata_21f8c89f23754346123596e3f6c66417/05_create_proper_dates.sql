-- This CTAS statement creates a new table with the proper date formats from rawnpidata called npidata.
-- In this new table, the dates should be MYSQL DATE columns, and the npi field should be a BIGINT(20) instead of a VARCHAR(10).
-- The new table will be called npidata.
-- The new table will be created in the same schema as the original table, other than the changes described. 
-- The structure of the old table can be found incache_create_table_sql/21f8c89f23754346123596e3f6c66417.replace_me.sql
-- The string contents of the Date fields has the structure of "01/16/2024"

DROP TABLE IF EXISTS npidata;

CREATE TABLE npidata AS
SELECT 
    CAST(npi AS UNSIGNED) AS npi,
    Entity_Type_Code,
    CAST(Replacement_NPI AS UNSIGNED) AS Replacement_NPI,
    Employer_Identification_Number_EIN,
    Provider_Organization_Name_Legal_Business_Name,
    Provider_Last_Name_Legal_Name,
    Provider_First_Name,
    Provider_Middle_Name,
    Provider_Name_Prefix_Text,
    Provider_Name_Suffix_Text,
    Provider_Credential_Text,
    Provider_Other_Organization_Name,
    Provider_Other_Organization_Name_Type_Code,
    Provider_Other_Last_Name,
    Provider_Other_First_Name,
    Provider_Other_Middle_Name,
    Provider_Other_Name_Prefix_Text,
    Provider_Other_Name_Suffix_Text,
    Provider_Other_Credential_Text,
    Provider_Other_Last_Name_Type_Code,
    Provider_First_Line_Business_Mailing_Address,
    Provider_Second_Line_Business_Mailing_Address,
    Provider_Business_Mailing_Address_City_Name,
    Provider_Business_Mailing_Address_State_Name,
    Provider_Business_Mailing_Address_Postal_Code,
    Provider_Business_Mailing_Address_Country_Code,
    Provider_Business_Mailing_Address_Telephone_Number,
    Provider_Business_Mailing_Address_Fax_Number,
    Provider_First_Line_Business_Practice_Location_Address,
    Provider_Second_Line_Business_Practice_Location_Address,
    Provider_Business_Practice_Location_Address_City_Name,
    Provider_Business_Practice_Location_Address_State_Name,
    Provider_Business_Practice_Location_Address_Postal_Code,
    Provider_Business_Practice_Location_Address_Country_Code,
    Provider_Business_Practice_Location_Address_Telephone_Number,
    Provider_Business_Practice_Location_Address_Fax_Number,
    STR_TO_DATE(Provider_Enumeration_Date, '%m/%d/%Y') AS Provider_Enumeration_Date,
    STR_TO_DATE(Last_Update_Date, '%m/%d/%Y') AS Last_Update_Date,
    NPI_Deactivation_Reason_Code,
    STR_TO_DATE(NPI_Deactivation_Date, '%m/%d/%Y') AS NPI_Deactivation_Date,
    STR_TO_DATE(NPI_Reactivation_Date, '%m/%d/%Y') AS NPI_Reactivation_Date,
    Provider_Sex_Code,
    Authorized_Official_Last_Name,
    Authorized_Official_First_Name,
    Authorized_Official_Middle_Name,
    Authorized_Official_Title_or_Position,
    Authorized_Official_Telephone_Number,
    Is_Sole_Proprietor,
    Is_Organization_Subpart,
    Parent_Organization_LBN,
    Parent_Organization_TIN,
    Authorized_Official_Name_Prefix_Text,
    Authorized_Official_Name_Suffix_Text,
    Authorized_Official_Credential_Text,
    STR_TO_DATE(Certification_Date, '%m/%d/%Y') AS Certification_Date
FROM 
    rawnpidata;

-- Add primary key to the npi field
ALTER TABLE npidata ADD PRIMARY KEY (npi);

-- Add indexes for commonly queried fields
ALTER TABLE npidata ADD INDEX idx_provider_name (Provider_Last_Name_Legal_Name, Provider_First_Name);
ALTER TABLE npidata ADD INDEX idx_enumeration_date (Provider_Enumeration_Date);
ALTER TABLE npidata ADD INDEX idx_last_update_date (Last_Update_Date);
ALTER TABLE npidata ADD INDEX idx_org_name (Provider_Organization_Name_Legal_Business_Name);
ALTER TABLE npidata ADD INDEX idx_other_org_name (Provider_Other_Organization_Name);
ALTER TABLE npidata ADD INDEX idx_other_credential (Provider_Other_Credential_Text);
ALTER TABLE npidata ADD INDEX idx_credential (Provider_Credential_Text);
ALTER TABLE npidata ADD INDEX idx_sex_code (Provider_Sex_Code);
ALTER TABLE npidata ADD INDEX idx_certification_date (Certification_Date);
