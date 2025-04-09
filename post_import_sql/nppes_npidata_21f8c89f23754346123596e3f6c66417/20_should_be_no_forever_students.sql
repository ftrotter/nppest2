-- There should be no forever students
-- First find all of the NPIs that are -only- students
CREATE TABLE study_only_students AS 
SELECT npi 
FROM taxonomies_normalized
WHERE Healthcare_Provider_Taxonomy_Code = '390200000X'
AND npi NOT IN (
  SELECT npi 
  FROM taxonomies_normalized
  WHERE Healthcare_Provider_Taxonomy_Code != '390200000X'
)
;
CREATE TABLE should_be_no_forever_students AS
SELECT study_only_students.npi 
FROM study_only_students
JOIN npidata ON 
  npidata.npi = study_only_students.npi
WHERE npidata.Provider_Enumeration_Date > -- greater than six years ago
  DATE_SUB(CURDATE(), INTERVAL 6 YEAR)