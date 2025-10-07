SELECT year, institution, score
FROM university_rankings
WHERE year = 2014 AND institution = 'University of Oxford';

-- score was 97.51 before update


UPDATE university_rankings
SET score = ROUND(score + 1.2, 2)
WHERE year = 2014
AND institution = 'University of Oxford';
