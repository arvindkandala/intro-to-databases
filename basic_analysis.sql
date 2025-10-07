-- rows per year
SELECT year, COUNT(*) AS n
FROM university_rankings
GROUP BY year
ORDER BY year;

-- rows per country
SELECT country, COUNT(*) AS n
FROM university_rankings
GROUP BY country
ORDER BY n DESC, country;

-- rows per country per year
SELECT year, country, COUNT(*) AS total
FROM university_rankings
GROUP BY year, country
ORDER BY year, total DESC
LIMIT 100;
