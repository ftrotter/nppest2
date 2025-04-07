
DROP TABLE IF EXISTS `taxonomies_normalized`
;

CREATE TABLE taxonomies_normalized AS 
SELECT 
	npi,
	1 AS tax_position,
	Provider_License_Number_1 AS Provider_License_Number,
	Provider_License_Number_State_Code_1  AS Provider_License_Number_State_Code,
	Healthcare_Provider_Primary_Taxonomy_Switch_1 AS Healthcare_Provider_Primary_Taxonomy_Switch,
	Healthcare_Provider_Taxonomy_Group_1 AS Healthcare_Provider_Taxonomy_Group
FROM npidata
WHERE 
	Provider_License_Number_1 IS NOT NULL
OR 	Provider_License_Number_State_Code_1 IS NOT NULL
OR 	Healthcare_Provider_Primary_Taxonomy_Switch_1 IS NOT NULL
OR 	Healthcare_Provider_Taxonomy_Group_1 IS NOT NULL
;



INSERT INTO taxonomies_normalized
SELECT
        npi,
        2 AS tax_position,
        Provider_License_Number_2 AS Provider_License_Number,
        Provider_License_Number_State_Code_2  AS Provider_License_Number_State_Code,
        Healthcare_Provider_Primary_Taxonomy_Switch_2 AS Healthcare_Provider_Primary_Taxonomy_Switch,
        Healthcare_Provider_Taxonomy_Group_2 AS Healthcare_Provider_Taxonomy_Group
FROM npidata
WHERE
        Provider_License_Number_2 IS NOT NULL
OR      Provider_License_Number_State_Code_2 IS NOT NULL
OR      Healthcare_Provider_Primary_Taxonomy_Switch_2 IS NOT NULL
OR      Healthcare_Provider_Taxonomy_Group_2 IS NOT NULL
;



INSERT INTO taxonomies_normalized
SELECT
        npi,
        3 AS tax_position,
        Provider_License_Number_3 AS Provider_License_Number,
        Provider_License_Number_State_Code_3  AS Provider_License_Number_State_Code,
        Healthcare_Provider_Primary_Taxonomy_Switch_3 AS Healthcare_Provider_Primary_Taxonomy_Switch,
        Healthcare_Provider_Taxonomy_Group_3 AS Healthcare_Provider_Taxonomy_Group
FROM npidata
WHERE
        Provider_License_Number_3 IS NOT NULL
OR      Provider_License_Number_State_Code_3 IS NOT NULL
OR      Healthcare_Provider_Primary_Taxonomy_Switch_3 IS NOT NULL
OR      Healthcare_Provider_Taxonomy_Group_3 IS NOT NULL
;



INSERT INTO taxonomies_normalized
SELECT
        npi,
        4 AS tax_position,
        Provider_License_Number_4 AS Provider_License_Number,
        Provider_License_Number_State_Code_4  AS Provider_License_Number_State_Code,
        Healthcare_Provider_Primary_Taxonomy_Switch_4 AS Healthcare_Provider_Primary_Taxonomy_Switch,
        Healthcare_Provider_Taxonomy_Group_4 AS Healthcare_Provider_Taxonomy_Group
FROM npidata
WHERE
        Provider_License_Number_4 IS NOT NULL
OR      Provider_License_Number_State_Code_4 IS NOT NULL
OR      Healthcare_Provider_Primary_Taxonomy_Switch_4 IS NOT NULL
OR      Healthcare_Provider_Taxonomy_Group_4 IS NOT NULL
;



INSERT INTO taxonomies_normalized
SELECT
        npi,
        5 AS tax_position,
        Provider_License_Number_5 AS Provider_License_Number,
        Provider_License_Number_State_Code_5  AS Provider_License_Number_State_Code,
        Healthcare_Provider_Primary_Taxonomy_Switch_5 AS Healthcare_Provider_Primary_Taxonomy_Switch,
        Healthcare_Provider_Taxonomy_Group_5 AS Healthcare_Provider_Taxonomy_Group
FROM npidata
WHERE
        Provider_License_Number_5 IS NOT NULL
OR      Provider_License_Number_State_Code_5 IS NOT NULL
OR      Healthcare_Provider_Primary_Taxonomy_Switch_5 IS NOT NULL
OR      Healthcare_Provider_Taxonomy_Group_5 IS NOT NULL
;



INSERT INTO taxonomies_normalized
SELECT
        npi,
        6 AS tax_position,
        Provider_License_Number_6 AS Provider_License_Number,
        Provider_License_Number_State_Code_6  AS Provider_License_Number_State_Code,
        Healthcare_Provider_Primary_Taxonomy_Switch_6 AS Healthcare_Provider_Primary_Taxonomy_Switch,
        Healthcare_Provider_Taxonomy_Group_6 AS Healthcare_Provider_Taxonomy_Group
FROM npidata
WHERE
        Provider_License_Number_6 IS NOT NULL
OR      Provider_License_Number_State_Code_6 IS NOT NULL
OR      Healthcare_Provider_Primary_Taxonomy_Switch_6 IS NOT NULL
OR      Healthcare_Provider_Taxonomy_Group_6 IS NOT NULL
;



INSERT INTO taxonomies_normalized
SELECT
        npi,
        7 AS tax_position,
        Provider_License_Number_7 AS Provider_License_Number,
        Provider_License_Number_State_Code_7  AS Provider_License_Number_State_Code,
        Healthcare_Provider_Primary_Taxonomy_Switch_7 AS Healthcare_Provider_Primary_Taxonomy_Switch,
        Healthcare_Provider_Taxonomy_Group_7 AS Healthcare_Provider_Taxonomy_Group
FROM npidata
WHERE
        Provider_License_Number_7 IS NOT NULL
OR      Provider_License_Number_State_Code_7 IS NOT NULL
OR      Healthcare_Provider_Primary_Taxonomy_Switch_7 IS NOT NULL
OR      Healthcare_Provider_Taxonomy_Group_7 IS NOT NULL
;



INSERT INTO taxonomies_normalized
SELECT
        npi,
        8 AS tax_position,
        Provider_License_Number_8 AS Provider_License_Number,
        Provider_License_Number_State_Code_8  AS Provider_License_Number_State_Code,
        Healthcare_Provider_Primary_Taxonomy_Switch_8 AS Healthcare_Provider_Primary_Taxonomy_Switch,
        Healthcare_Provider_Taxonomy_Group_8 AS Healthcare_Provider_Taxonomy_Group
FROM npidata
WHERE
        Provider_License_Number_8 IS NOT NULL
OR      Provider_License_Number_State_Code_8 IS NOT NULL
OR      Healthcare_Provider_Primary_Taxonomy_Switch_8 IS NOT NULL
OR      Healthcare_Provider_Taxonomy_Group_8 IS NOT NULL
;



INSERT INTO taxonomies_normalized
SELECT
        npi,
        9 AS tax_position,
        Provider_License_Number_9 AS Provider_License_Number,
        Provider_License_Number_State_Code_9  AS Provider_License_Number_State_Code,
        Healthcare_Provider_Primary_Taxonomy_Switch_9 AS Healthcare_Provider_Primary_Taxonomy_Switch,
        Healthcare_Provider_Taxonomy_Group_9 AS Healthcare_Provider_Taxonomy_Group
FROM npidata
WHERE
        Provider_License_Number_9 IS NOT NULL
OR      Provider_License_Number_State_Code_9 IS NOT NULL
OR      Healthcare_Provider_Primary_Taxonomy_Switch_9 IS NOT NULL
OR      Healthcare_Provider_Taxonomy_Group_9 IS NOT NULL
;



INSERT INTO taxonomies_normalized
SELECT
        npi,
        10 AS tax_position,
        Provider_License_Number_10 AS Provider_License_Number,
        Provider_License_Number_State_Code_10  AS Provider_License_Number_State_Code,
        Healthcare_Provider_Primary_Taxonomy_Switch_10 AS Healthcare_Provider_Primary_Taxonomy_Switch,
        Healthcare_Provider_Taxonomy_Group_10 AS Healthcare_Provider_Taxonomy_Group
FROM npidata
WHERE
        Provider_License_Number_10 IS NOT NULL
OR      Provider_License_Number_State_Code_10 IS NOT NULL
OR      Healthcare_Provider_Primary_Taxonomy_Switch_10 IS NOT NULL
OR      Healthcare_Provider_Taxonomy_Group_10 IS NOT NULL
;



INSERT INTO taxonomies_normalized
SELECT
        npi,
        11 AS tax_position,
        Provider_License_Number_11 AS Provider_License_Number,
        Provider_License_Number_State_Code_11  AS Provider_License_Number_State_Code,
        Healthcare_Provider_Primary_Taxonomy_Switch_11 AS Healthcare_Provider_Primary_Taxonomy_Switch,
        Healthcare_Provider_Taxonomy_Group_11 AS Healthcare_Provider_Taxonomy_Group
FROM npidata
WHERE
        Provider_License_Number_11 IS NOT NULL
OR      Provider_License_Number_State_Code_11 IS NOT NULL
OR      Healthcare_Provider_Primary_Taxonomy_Switch_11 IS NOT NULL
OR      Healthcare_Provider_Taxonomy_Group_11 IS NOT NULL
;



INSERT INTO taxonomies_normalized
SELECT
        npi,
        12 AS tax_position,
        Provider_License_Number_12 AS Provider_License_Number,
        Provider_License_Number_State_Code_12  AS Provider_License_Number_State_Code,
        Healthcare_Provider_Primary_Taxonomy_Switch_12 AS Healthcare_Provider_Primary_Taxonomy_Switch,
        Healthcare_Provider_Taxonomy_Group_12 AS Healthcare_Provider_Taxonomy_Group
FROM npidata
WHERE
        Provider_License_Number_12 IS NOT NULL
OR      Provider_License_Number_State_Code_12 IS NOT NULL
OR      Healthcare_Provider_Primary_Taxonomy_Switch_12 IS NOT NULL
OR      Healthcare_Provider_Taxonomy_Group_12 IS NOT NULL
;



INSERT INTO taxonomies_normalized
SELECT
        npi,
        13 AS tax_position,
        Provider_License_Number_13 AS Provider_License_Number,
        Provider_License_Number_State_Code_13  AS Provider_License_Number_State_Code,
        Healthcare_Provider_Primary_Taxonomy_Switch_13 AS Healthcare_Provider_Primary_Taxonomy_Switch,
        Healthcare_Provider_Taxonomy_Group_13 AS Healthcare_Provider_Taxonomy_Group
FROM npidata
WHERE
        Provider_License_Number_13 IS NOT NULL
OR      Provider_License_Number_State_Code_13 IS NOT NULL
OR      Healthcare_Provider_Primary_Taxonomy_Switch_13 IS NOT NULL
OR      Healthcare_Provider_Taxonomy_Group_13 IS NOT NULL
;



INSERT INTO taxonomies_normalized
SELECT
        npi,
        14 AS tax_position,
        Provider_License_Number_14 AS Provider_License_Number,
        Provider_License_Number_State_Code_14  AS Provider_License_Number_State_Code,
        Healthcare_Provider_Primary_Taxonomy_Switch_14 AS Healthcare_Provider_Primary_Taxonomy_Switch,
        Healthcare_Provider_Taxonomy_Group_14 AS Healthcare_Provider_Taxonomy_Group
FROM npidata
WHERE
        Provider_License_Number_14 IS NOT NULL
OR      Provider_License_Number_State_Code_14 IS NOT NULL
OR      Healthcare_Provider_Primary_Taxonomy_Switch_14 IS NOT NULL
OR      Healthcare_Provider_Taxonomy_Group_14 IS NOT NULL
;



INSERT INTO taxonomies_normalized
SELECT
        npi,
        15 AS tax_position,
        Provider_License_Number_15 AS Provider_License_Number,
        Provider_License_Number_State_Code_15  AS Provider_License_Number_State_Code,
        Healthcare_Provider_Primary_Taxonomy_Switch_15 AS Healthcare_Provider_Primary_Taxonomy_Switch,
        Healthcare_Provider_Taxonomy_Group_15 AS Healthcare_Provider_Taxonomy_Group
FROM npidata
WHERE
        Provider_License_Number_15 IS NOT NULL
OR      Provider_License_Number_State_Code_15 IS NOT NULL
OR      Healthcare_Provider_Primary_Taxonomy_Switch_15 IS NOT NULL
OR      Healthcare_Provider_Taxonomy_Group_15 IS NOT NULL
;


