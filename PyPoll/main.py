import os
import csv

# def percentage(numbers):
#     length = len(numbers)
#     total = 369711
#     return length * 100 / total 

csvpath = os.path.join('Resources','election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Skipping the header
    header = next(csvreader)

    total_votes = 0
    total_votes1 = 0
    total_votes2 = 0
    total_votes3 = 0
    candidate_list = []
    all_candidates = []
    candidate1_votes = []
    candidate2_votes = []
    candidate3_votes = []
    
    for row in csvreader:
    # Calculation Total number of Votes
        total_votes += 1
        # Create Candidate names list
        candidate_list.append(row[2])  
        if row[2] not in all_candidates:
            all_candidates.append(row[2])
        if "Charles Casper Stockham" in row:
            candidate1_votes.append(row[0])
        if "Diana DeGette" in row:
             candidate2_votes.append(row[0])
        if "Raymon Anthony Doane" in row:
             candidate3_votes.append(row[0])
    
    #print(candidate1_votes)

    # Calculating Total Votes for Candidate 1
    for row in candidate1_votes:
        total_votes1 += 1
    for row in candidate2_votes:
        total_votes2 += 1
    for row in candidate3_votes:
        total_votes3 += 1
    
    percentage1 = "{:.3f}".format(total_votes1 / total_votes * 100)
    percentage2 = "{:.3f}".format(total_votes2 / total_votes * 100)
    percentage3 = "{:.3f}".format(total_votes3 / total_votes * 100)
    
    total_votes_list = (total_votes1, total_votes2, total_votes3)
    zip_list = zip(all_candidates, total_votes_list)
    winner_votes = max(total_votes_list)
    
    for row in zip_list:
        if winner_votes in row:
            winner = row[0]

    
    # Printing data
    print("Election Results")
    print("----------------")
    print(f'Total Votes: {total_votes}')
    print("----------------")
    print(f'{all_candidates[0]} {percentage1}% ({total_votes1})')
    print(f'{all_candidates[1]} {percentage2}% ({total_votes2})')
    print(f'{all_candidates[2]} {percentage3}% ({total_votes3})')
    print("----------------")
    print(f'Winner: {winner}')
    print("----------------")
