import os
import csv

csvpath = os.path.join('Resources','election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Skipping the header
    header = next(csvreader)
    
    # Setting up variables and lists
    total_votes = 0
    total_votes1 = 0
    total_votes2 = 0
    total_votes3 = 0
    candidate_list = []
    all_candidates = []
    candidate1_votes = []
    candidate2_votes = []
    candidate3_votes = []
    
    # Calculations:
    for row in csvreader:
    # Calculating Total number of Votes
        total_votes += 1
        # Create Candidate names list
        candidate_list.append(row[2])  
        if row[2] not in all_candidates:
            all_candidates.append(row[2])
    
        # Creating lists with each candidate's votes
        if "Charles Casper Stockham" in row:
            candidate1_votes.append(row[0])
        if "Diana DeGette" in row:
             candidate2_votes.append(row[0])
        if "Raymon Anthony Doane" in row:
             candidate3_votes.append(row[0])
    
    # Calculating Total Votes for each candidate
    for row in candidate1_votes:
        total_votes1 += 1
    for row in candidate2_votes:
        total_votes2 += 1
    for row in candidate3_votes:
        total_votes3 += 1
    
    # Calculating the percentage of votes each candidate won
    percentage1 = "{:.3f}".format(total_votes1 / total_votes * 100)
    percentage2 = "{:.3f}".format(total_votes2 / total_votes * 100)
    percentage3 = "{:.3f}".format(total_votes3 / total_votes * 100)
    
    # Creating new list with total votes 
    total_votes_list = (total_votes1, total_votes2, total_votes3)

    # Creating a new list with all candidates names and their total votes 
    zip_list = zip(all_candidates, total_votes_list)
    
    # Calculating the maximum amount of votes
    winner_votes = max(total_votes_list)
    
    # Selecting the winner name
    for row in zip_list:
        if winner_votes in row:
            winner = row[0]

    
    # Printing data
    new_line = '\n'
    export = (
    f'{new_line}'
    f'Election Results {new_line}' 
    f'{new_line}'
    f'---------------- {new_line}'
    f'Total Votes: {total_votes} {new_line}'
    f'---------------- {new_line}'
    f'{all_candidates[0]} {percentage1}% ({total_votes1}) {new_line}'
    f'{all_candidates[1]} {percentage2}% ({total_votes2}) {new_line}'
    f'{all_candidates[2]} {percentage3}% ({total_votes3}) {new_line}'
    f'---------------- {new_line}'
    f'Winner: {winner} {new_line}'
    f'----------------')

print(export)

# set variables for output file
output_file = os.path.join("analysis", "analysis_result.csv")
# open the output file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)
    #write the result
    writer.writerow([export])
     