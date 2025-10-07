SELECT COUNT(*) AS remaining
FROM university_rankings
WHERE year = 2015 AND score IS NOT NULL AND score < 45;