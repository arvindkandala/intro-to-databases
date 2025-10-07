# intro-to-databases
To explore the data, I simply found the number of entries per year, entries per country, and entries per country each year.

For the question:
    The ranking committee has decided to publish new results for a new university in 2014. Insert this university into the database.
        Institution: Duke Tech
        Country: USA
        World Rank: 350
        Score: 60.5
I added in a row with the above details.


To answer the question 
    "A policy consultant has reached out to you with the following question. How many universities from Japan show up in the global top 200 in 2013?"
I made a query selects rows with Japan as the country, 2013 as the year, and rank better than 200.


For this question
    The score for University of Oxford in 2014 was miscalculated. Increase its score by +1.2 points. Update the row to reflect this update.
Oxford's score was 97.51 before the update. Afterwards, it was 98.21.


For the question:
    After reviewing, the ranking committee decided that universities with a score below 45 in 2015 should not have been included in the published dataset. Clean up the records to reflect this.
I deleted the rows score below 45 from the table