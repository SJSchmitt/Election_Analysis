# The data we need to retrieve:
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# 1. initialize a vote counter
total_votes = 0

# 2. list candidates
candidate_options = []

# 4.  Declare dict to count votes for each candidate
candidate_votes = {}

# 5.  Determine the winner by popular vote
winning_candidate = ''
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.

     # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in file
    for row in file_reader:
        # 1a. Add to total vote count
        total_votes += 1

        # 2a.  Get candidate name from each row
        candidate_name = row[2]

        # 2b. check if candidate is already in list, append if it is not
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # 4a.  initialize vote counter for each candidate
            candidate_votes[candidate_name] = 0

        # 4b.  Count votes for each candidate
        candidate_votes[candidate_name] += 1
    
    # Save the results to our text file.
    with open(file_to_save, "w") as txt_file:

        # Create opening results for text file
        election_results = (
            f"Election Results\n"
            f"-----------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-----------------------------\n"
        )

        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_results)

        # 3.  Calculate percentage of the vote for each candidate
        for candidate_name in candidate_votes:
            votes = candidate_votes[candidate_name]
            vote_percentage = float(votes) / float(total_votes) * 100
            # 3a.  Print candidate vote percentages
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}%  {votes:,}\n")

            # Print each candidate, their voter count, and percentage to the terminal.
            print(candidate_results)
            #  Save the candidate results to our text file.
            txt_file.write(candidate_results)

            # 5a. Determine highest vote and percentage
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate_name

        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)
            
        
    