SELECT COUNT(*) AS deleting
FROM university_rankings
WHERE year = 2015 AND score IS NOT NULL AND score < 45;

DELETE FROM university_rankings
WHERE year = 2015 AND score IS NOT NULL AND score < 45;