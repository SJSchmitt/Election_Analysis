# Analysis of a Colorado Election Audit

## Overview of Election Audit
<!-- explain the purpose of this Audit -->
This [Python script](PyPoll_Challenge.py) was created to analyze the results of a Colorado Election.  Voters in these elections span three counties: Arapahoe, Denver, and Jefferson, with three candidates to vote from: Charles Caspar Stockham, Diana DeGette, and Raymon Anthony Doane.  We calculated the voter turnout per county and the votes each candidate received, allowing us to find which county had the highest turnout and each candidate's percentage of the popular vote, along with who won the election.

## Election Audit Results
<!-- use a bulleted list to address the following questions:
    How many votes were cast in this congressional election?
    Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
    Which county had the largest number of votes?
    Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
    Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
-->
The Colorado Board of Elections provided us with a list of questions our script needed to answer, using data from [this CSV file](Resources/election_results.csv).  We used Python's `os` and `csv ` libraries to assist in reading the input file and printing the results to a text file.  The `os` library was used to create relative paths based on the operating system in use, as Windows and Mac systems format paths differently, while the `csv` library added the `reader()` function, which enabled us to iterate through the data file by row.  

### Election Questions and Answers

- ***How many votes were cast in this congressional election? <br />***
    In this election, 369,711 votes were cast.  
- ***Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct. <br />***
    Denver County had 82.8% of voters, with 306,055 votes.  
    Jefferson County had 10.5% of the vote, with 38,855 votes.  
    Arapahoe had the smallest turnout, contributing only 6.7% of the vote, with 24,801 votes.
- ***Which county had the largest number of votes? <br />***
    Denver County had the largest number of votes, at 306,055 votes making up 82.8% of the popular vote.
- ***Provide a breakdown of the number of votes and the percentage of the total votes each candidate received. <br />***
    Charles Caspar Stockham received 23.0% of the popular vote, with 85,213 votes.  
    Diana DeGette received 73.8% of the popular vote, with 272,892 votes.
    Raymon Anthony Doane received 3.1% of the popular vote, with 11,606 votes.
- ***Which candidate won the election, what was their vote count, and what was their percentage of the total votes? <br />*** 
    Diana DeGette won the election, with 272,892 votes contributing 73.8% of the total votes.
    
Our code wrote these results to the terminal and to [a text file](Analysis/election_results.txt).  My terminal output using Visual Studio Code is shown below:

[An image of a VS Code terminal, showing the same results as the election_results.txt file](Analysis/terminal_output.png)

## Election Audit Summary
<!-- In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections. -->

We wrote this code to be robust, candidate and county names are not hard-coded in, but rather extracted from the CSV we read from.  We initialized empty lists for candidate names and empty dictionaries for candidate and county results, then we added any name that wasn't already in the appropriate dictionary to that dictionary as we iterated through the CSV rows.
```
candidate_options = []
candidate_votes = {}
for row in reader:
  candidate_name = row[2]
  if candidate_name not in candidate_list:
    candidate_options.append(candidate_name)
    candidate_votes[candidate_name] = 0
```
This allows our script to be used for any counties with any candidates, provided the input data follows the same format.  If it didn't follow the same format, it would be a simple matter to change the indices representing which CSV column holds county and candidate names.  

<!-- one modification would be for the script to take user input for the path to the data file and the output file, so that the python code wouldn't have to be touched between uses.-->
However, our script does hard-code the paths to our input and output files.  A small modification to make this script easier to use for other elections would be to allow the user to define those paths, using `input()`.  In this case, it would probably be better to change from the relative paths we used to absolute paths, so that users don't have to organize their files or edit the script to make the script work.

Another modification could be to track candidates' results by county, as well as their overall results.  This could be done with a nested dictionary, such as the following:
```
results_by_county = {"County_1":{"Candidate_1":x, "Candidate_2": y, "Candidate_3": z}, 
                    "County_2":{"Candidate_1": a, "Candidate_2": b, "Candidate_3": c}}
``` 
This is a popular way to view US presidential election results, as well as more localized results.  Additionally, not all elections are decided by popular vote, some are decided by number of districts won instead.  I would also recommend removing lines that print "The winner is:", unless we also incorporate a way to determine which metric will be used to evaluate the winner.  Or, if not remove that, add a new header line that makes it clear we are referring to the popular vote and not necessarily the overall election results.
