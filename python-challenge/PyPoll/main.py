#!/Users/michaelshih/anaconda3/envs/wudata/bin/python

#%%
import os
import csv

dir = ('/Users/major_minor1982/Documents/code/Python/python-challenge/PyPoll')
subdir = 'resources'
filename = 'election_data.csv'

filepath = os.path.join(dir, subdir, filename)
# print(filepath)

#%%
# extract data from csv file
with open(filepath, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',')
        # print(csvreader)

        csv_header = next(csvreader)
        # print(f"CSV Header: {csv_header}")
        
        colVoter = []
        colCounty = []
        colCandidate = []
        for row in csvreader:
                colVoter.append(row[0])
                colCounty.append(row[1])
                colCandidate.append(row[2])
        
        # print(colDate)
        # print(colRevenue)



#%%
print(""" 
Election Results
-------------------------""")

# The total number of votes cast
# len()
total_vote = len(colVoter)
print('Total Votes: {}'.format(total_vote))
print("-------------------------")

# A complete list of candidates who received votes
# set()
candidate_set = set(colCandidate)
cadidate_list = list(candidate_set)
cadidate_list = sorted(cadidate_list, key=str.lower)
# print(cadidate_list)


#print vote
votecount = []
votepercentage = []
for candidate in cadidate_list:
    candidate_idx = []
    vote_count = 0
    for idx in range(len(colCandidate)):
        if colCandidate[idx] == candidate:
            vote_count += 1     
           
    vote_percentage = vote_count/total_vote*100
    
    votecount.append(vote_count)
    votepercentage.append(vote_percentage)

    # print(candidate)
    # print(vote_count)
    # print(vote_percentage)
    
    print('{0}: {1:.3f}% ({2})'.format(candidate, \
                                vote_percentage,
                                vote_count)        
                                )
print("-------------------------")

# print the winner
winner_idx = votecount.index(max(votecount))
print('Winner: {}'.format(cadidate_list[winner_idx]))
print("-------------------------")

# output file
output_path = os.path.join(dir, 'result.txt')

with open(output_path, 'w') as file:
        file.write('Election Results\n'
                '-------------------------\n'
                ) 
        file.write('Total Votes: {}\n'.format(total_vote))
        file.write('-------------------------\n')
        for idx in range(len(cadidate_list)):
                file.write('{0}: {1:.3f}% ({2})\n'.format(cadidate_list[idx], \
                                votepercentage[idx],
                                votecount[idx])        
                                )
        file.write('-------------------------\n')
        file.write('Winner: {}\n'.format(cadidate_list[winner_idx]))
        file.write('-------------------------\n')
