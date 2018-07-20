#!/Users/michaelshih/anaconda3/envs/wudata/bin/python

#%%
import pandas as pd
import numpy as np 
import os

dir = '/Users/michaelshih/documents/code/education/wu_data_bootcamp_code/python-challenge/PyBank'
os.chdir(dir)
print(os.getcwd())

#%%
subdir = 'resources'
filename = 'budget_data.csv'
filepath = os.path.join(dir, subdir, filename)
# print(filepath)

#%%
data = pd.read_csv(filepath)
data = pd.DataFrame(data)
# data

#%%
# The total number of months included in the dataset
# data.shape: caution: .shape will create a tuple, no "()" needed
nrow = data.shape[0]
ncol = data.shape[1]
#print(nrow)
#print(ncol)

# a better option is unique() + len()
# It can avoid replication gets counted. 
total_nunber_month = data.Date.nunique()
#print(total_nunber_month)

#%%
# The total net amount of "Profit/Losses" over the entire period
# sum()
total_net_amount = data.Revenue.sum()
#print(total_net_amount)

#%%
# The average change in "Profit/Losses" between months over the entire period
# mean()
average_change = data.Revenue.mean()
#print(average_change)

#%%
# The greatest increase in profits (date and amount) over the entire period
# max()
greatest_increase = data.Revenue.max()
greatest_increase_idx = data.Revenue.idxmax()
#print(greatest_increase)
#print(greatest_increase_idx)

#%%
# The greatest decrease in losses (date and amount) over the entire period
# min()
greatest_decrease = data.Revenue.min()
greatest_decrease_idx = data.Revenue.idxmin()
#print(greatest_decrease)
#print(greatest_decrease_idx)

#%%
# print results
print(
'''
Financial Analysis
----------------------------
Total Months: {0}
Total: {1}
Average  Change: {2}
Greatest Increase in Profits: {3} ({4})
Greatest Decrease in Profits: {5} ({6})
'''.format(total_nunber_month, \
            total_net_amount, \
            average_change, \
            data.Date.iloc[greatest_increase_idx], \
            greatest_increase, \
            data.Date.iloc[greatest_decrease_idx], \
            greatest_decrease
            )
)