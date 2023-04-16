import os
import csv

#format lines and title
report_file = '-'*70 + '\n'
report_file += 'Election Results\n'
report_file += '-'*70 + '\n'

# Path to collect data from the Resources folder
pypoll_csv = os.path.join('Resources','election_data.csv')
with open(pypoll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    poll_data = list(csvreader)

total_votes = len(poll_data)-1
report_file += (f'Total Votes: {total_votes}\n')
report_file += '-'*70 + '\n'

# initialize dictionary with candidate names and vote count
votes = {}
for candidate in poll_data:
    if candidate[2] != 'Candidate':        
        name = candidate[2]
        # if name is not found, create a new dictionary entry
        votes.setdefault(name,0)
        votes[name] += 1

# sorts the list ascending and gets last (highest) value
most_votes = sorted(list(votes.values()))[-1]

for item in votes.items():
    cand,vcount = item
    report_file += (f'{cand}: {vcount/total_votes*100:.3f}% ({vcount})\n')

# dictionary comprehension to flip keys and values to set most_votes as key and find candidate
winners = {v:k for k,v in votes.items()}

report_file += '-'*70 + '\n'
report_file += (f'Winner: {winners[most_votes]}\n')
report_file += '-'*70 + '\n'

print(report_file)

#create new text file and write report_file
pypoll_text = os.path.join('Analysis','election_results.txt')
with open (pypoll_text, mode='wt', encoding = 'utf-8') as output:
    output.write(report_file)


