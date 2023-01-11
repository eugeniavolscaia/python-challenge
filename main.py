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
    
    for row in csvreader:
        # Calculating the Total number of months
        total_months += 1
        # Calculating net total amount
        total_amount += int(row[1])
        #Create num_data - list of Profit/Loss
        profit_loss = int(row[1])
        num_data.append(profit_loss)

    i = 0
    while i < (len(num_data) - 1):
        #for number in (num_data):    
        result = num_data[i+1] - num_data[i]
        differences.append(result)
        i += 1  

    print("Financial Analysis")
    print("------------------")    
    print(f'Total Months: {total_months}')
    print(f'Total: {total_amount}')
    print(f'Average Change:  {average(differences)}')
       
   

   







   

   



