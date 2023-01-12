import os
import csv

def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length

csvpath = os.path.join('Resources','budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skiping the header
    header = next(csvreader)
   
    # Calculations
    total_months = 0
    total_amount = 0
    num_data = []
    differences = []
    csvreader_date = []
    
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

    i = 0
    while i < (len(num_data) - 1):    
        result = num_data[i+1] - num_data[i]
        differences.append(result)
        i += 1  

    # Printing data
    print("Financial Analysis")
    print("------------------")    
    print(f'Total Months: {total_months}')
    print(f'Total: {total_amount}')
    print(f'Average Change:  {average(differences)}')

    greatest_increase = max(differences)
    
    # Difference list is one element shorter with the result shifted up
    differences.insert(0,"0")

    csvreader_zip = zip(csvreader_date, differences) 
    for row in csvreader_zip:
        if greatest_increase in row:
            print(f'Greatest Increase in Profits: {row[0]} ( {greatest_increase} )')   
   

   







   

   



