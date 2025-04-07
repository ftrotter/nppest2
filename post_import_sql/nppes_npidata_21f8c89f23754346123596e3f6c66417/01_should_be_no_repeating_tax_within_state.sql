-- There should be no repeating taxonomy within the same state. This is done to provide additional "licensing" data, but these should be "indentifiers"
CREATE TABLE should_be_no_duplicate_taxonomies_except_multi_state 
SELECT 
	npi,
	COUNT(DISTINCT(
