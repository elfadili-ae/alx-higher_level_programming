-- avg temperature/city
SELECT city, AVG(value) AS avg_temp FROM temperatures
GROUP BY city
ORDER BY city;
