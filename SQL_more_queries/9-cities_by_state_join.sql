-- A script that lists all cities and their corresponding state names, sorted by city id
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states
ON cities.state_id = states.id
ORDER BY cities.id ASC;
