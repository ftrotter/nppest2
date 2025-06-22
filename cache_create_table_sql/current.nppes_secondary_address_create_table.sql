CREATE TABLE nppes_raw.secondary_address_file (
    "npi" BIGINT NOT NULL,
    "Provider_Secondary_Practice_Location_Address_Line_1" VARCHAR(56),
    "Provider_Secondary_Practice_Location_Address_Line_2" VARCHAR(56),
    "Provider_Secondary_Practice_Location_Address_City_Name" VARCHAR(41),
    "Provider_Secondary_Practice_Location_Address_State_Name" VARCHAR(40),
    "Provider_Secondary_Practice_Location_Address_Postal_Code" VARCHAR(17),
    "Provider_Secondary_Practice_Location_Address_Country_Code_" VARCHAR(3),
    "Provider_Secondary_Practice_Location_Address_Telephone_Num" VARCHAR(20),
    "Provider_Secondary_Practice_Location_Address_Telephone_Ext" VARCHAR(6),
    "Provider_Practice_Location_Address_Fax_Number" VARCHAR(16)
);