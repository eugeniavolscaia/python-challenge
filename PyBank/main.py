import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skiping the header
    header = next(csvreader)
   
    # Definind variables and lists
    total_months = 0
    total_amount = 0
    num_data = []
    differences = []
    csvreader_date = []
    
    #Calculations:
    for row in csvreader:
        # Calculating the Total number of months
        total_months += 1
        # Calculating net total amount
        total_amount += int(row[1])
        #Create num_data - list of Profit/Loss
        profit_loss = int(row[1])
        num_data.append(profit_loss)
        #Create csvreade_date - list of Month/Year
        date = (row[0])
        csvreader_date.append(date)

    # Creating a list with Profit/loss differences 
    i = 0
    while i < (len(num_data) - 1):    
        result = num_data[i+1] - num_data[i]
        differences.append(result)
        i += 1
    
    # Calculating average of Differences
    total = 0.0
    for number in differences:
        total += number
    average = total/len(differences)
    
    # Calculating greatest Increase/Decrease
    greatest_increase = max(differences)
    greatest_decrease = min(differences)

    # Difference list is one element shorter with the result shifted up
    differences.insert(0,"0")

    # Creating list with Date and Profit/Loss changes
    csvreader_zip = zip(csvreader_date, differences) 

    # Attributing Date to the greatest Increase/Decrease
    for row in csvreader_zip:
        if greatest_increase in row:
            greatest_increase_date = (row[0])
        
        if greatest_decrease in row:
            greatest_decrease_date = (row[0])

    # Printing data
    new_line = '\n'
    export = (f' Financial Analysis {new_line } ------------------ {new_line}'    
    f' Total Months: {total_months} {new_line} Total: ${total_amount} {new_line}'
    f' Average Change:  ${round(average,2)} {new_line}'
    f' Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase}) {new_line}'
    f' Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})')

print(export)   

# set variable for output file
output_file = os.path.join("analysis","analysis_result.csv")
# open the output file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)
    # write the result
    writer.writerow([export])


    


   
