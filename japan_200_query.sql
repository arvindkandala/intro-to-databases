SELECT country, count(*) as total
FROM university_rankings
WHERE country = 'Japan'
AND world_rank<=200
AND year = '2013'
GROUP BY country;