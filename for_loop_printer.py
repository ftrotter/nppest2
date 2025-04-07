



for i in range(2,16):
    sql = f"""
INSERT INTO taxonomies_normalized
SELECT
        npi,
        {i} AS tax_position,
        Healthcare_Provider_Taxonomy_Code_{i} AS Healthcare_Provider_Taxonomy_Code,
        Provider_License_Number_{i} AS Provider_License_Number,
        Provider_License_Number_State_Code_{i}  AS Provider_License_Number_State_Code,
        Healthcare_Provider_Primary_Taxonomy_Switch_{i} AS Healthcare_Provider_Primary_Taxonomy_Switch,
        Healthcare_Provider_Taxonomy_Group_{i} AS Healthcare_Provider_Taxonomy_Group
FROM npidata
WHERE
        Provider_License_Number_{i} IS NOT NULL
OR      Provider_License_Number_State_Code_{i} IS NOT NULL
OR      Healthcare_Provider_Primary_Taxonomy_Switch_{i} IS NOT NULL
OR      Healthcare_Provider_Taxonomy_Group_{i} IS NOT NULL
;

"""    

    print(sql)


