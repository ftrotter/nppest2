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

