-- Lists all cities contained in the database hbtn_0d_usa

-- Selects the id and name columns for cities, and the name of their respective states, ordered by city id
SELECT cities.id, cities.name, states.name
FROM cities
LEFT JOIN states ON states.id = cities.state_id
ORDER BY cities.id;
