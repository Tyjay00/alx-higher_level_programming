-- Lists all the cities of California that can be found in the database hbtn_0d_usa

-- Selects the id and name columns for cities in California, ordered by id
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
