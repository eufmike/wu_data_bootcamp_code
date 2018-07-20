#%%
import os
import csv

# 
#%%
#print (__file__)
#print (os.path.dirname(__file__))
# print (os.path.abspath(__file__))

#%%
dir = ('/Users/major_minor1982/documents/code/Python/'
        'python-challenge/PyBank/')
# dir = '..'
subfolder = 'Resources'
filename = 'budget_data.csv'

filepath = os.path.join(dir, subfolder, filename)
print(filepath)

#%%
# extract data from csv file
with open(filepath, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',')
        # print(csvreader)

        csv_header = next(csvreader)
        # print(f"CSV Header: {csv_header}")
        print(f"CSV Header: {csv_header}")     

        colDate = []
        colRevenue = []
        for row in csvreader:
                colDate.append(row[0])
                colRevenue.append(float(row[1]))
        # print(colDate)
        # print(colRevenue)

#%%
# The total number of months included in the dataset
# len()
total_month = len(colDate)
# print(total_month)

# The total net amount of "Profit/Losses" over the entire period
# sum()
total_net_amount = sum(colRevenue)
# print(total_net_amount)

# The average change in "Profit/Losses" between months over the entire period
# mean()
average_change = total_net_amount/total_month
# print(average_change)

# The greatest increase in profits (date and amount) over the entire period
# max()
greatest_increase = max(colRevenue)
greatest_increase_idx = colRevenue.index(greatest_increase)
# print(greatest_increase)
# print(greatest_increase_idx)

# The greatest decrease in losses (date and amount) over the entire period
# min()
greatest_decrease = min(colRevenue)
greatest_decrease_idx = colRevenue.index(greatest_decrease)
# print(greatest_decrease)
# print(greatest_decrease_idx)

#%%
print(
'''
Financial Analysis
----------------------------
Total Months: {0}
Total: {1:.2f}
Average  Change: {2:.2f}
Greatest Increase in Profits: {3} ({4:.2f})
Greatest Decrease in Profits: {5} ({6:.2f})
'''.format(total_month, \
            total_net_amount, \
            average_change, \
            colDate[greatest_increase_idx], \
            greatest_increase, \
            colDate[greatest_decrease_idx], \
            greatest_decrease
            )
)

# output file
output_path = os.path.join(dir, 'result.txt')
with open(output_path, 'w') as file:
        file.write('''Financial Analysis
----------------------------
Total Months: {0}
Total: {1:.2f}
Average  Change: {2:.2f}
Greatest Increase in Profits: {3} ({4:.2f})
Greatest Decrease in Profits: {5} ({6:.2f})
'''.format(total_month, \
total_net_amount, \
average_change, \
colDate[greatest_increase_idx], \
greatest_increase, \
colDate[greatest_decrease_idx], \
greatest_decrease
)



        )