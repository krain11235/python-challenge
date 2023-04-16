import os
import csv

# Formatting lines and title
report_file = '-'*70 + '\n'
report_file += 'Financial Analysis\n'
report_file += '-'*70 + '\n'

# Path to collect data from the Resources folder
pybank_csv = os.path.join('Resources','budget_data.csv')

# listify the file contents
with open(pybank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    bank_data = list(csvreader)
    
# month_count = len(bank_data)-1 #(other method)
# initialize variables
months = 0
profit_sum = 0

#iterate through the list to count months and sum profits
for row in bank_data:
    if row[0] != 'Date':
        months += 1
        profit_sum += (int(row[1]))

# initialize variables and empty new profit and loss list
greatest_profit = 0
greatest_loss = 0
greatest_profit_date ='' 
greatest_loss_date = ''
total_pnl_diffs = 0
count_pnl_diffs = 0
delta_pnl = []

#interate through original list and create new list with dates and differences
for i in range(1,months):    
    difference = int(bank_data[i+1][1])-int(bank_data[i][1])
    delta_pnl.append([bank_data[i+1][0],difference])
    count_pnl_diffs += 1
    total_pnl_diffs += difference
    if difference > greatest_profit:
        greatest_profit = difference
        greatest_profit_date = bank_data[i+1][0]
    elif difference < greatest_loss:
        greatest_loss = difference
        greatest_loss_date = bank_data[i+1][0]   

average_change = round(float(total_pnl_diffs/count_pnl_diffs),2)

report_file += (f'Total Months: {months}\n')
report_file += (f'Total: ${profit_sum}\n')
report_file += (f'Average Change: ${average_change}\n')
report_file += (f'Greatest Increase in Profits: {greatest_profit_date} (${greatest_profit})\n')
report_file += (f'Greatest Decrease in Profits: {greatest_loss_date} (${greatest_loss})\n')
report_file += '-'*70 + '\n'

print(report_file)

#create new text file and write report_file results
pybank_text = os.path.join('Analysis','profit_and_loss.txt')
with open (pybank_text, mode='wt', encoding = 'utf-8') as output:
    output.write(report_file)
