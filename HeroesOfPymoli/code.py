'''
# Unit 4: Assignment - Pandas, Pandas, Pandas
## Project: Heroes of Pymoli

import modules and files
'''

#%%
import os, sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

path = '/Users/michaelshih/Documents/code/education/wu_data_bootcamp_code/HeroesOfPymoli'
subfolder = 'Resources'
filename = 'purchase_data.csv'
filepath = os.path.join(path, subfolder, filename)

data = pd.read_csv(filepath, header = 0)
data = pd.DataFrame(data)

'''
# Print the head of "purchase_data.csv"
'''
#%%
data
#%%
'''
# Report
## Player Count
Total Number of Players
'''
#%%
playercount = len(data['SN'].unique())
print(playercount)
'''
## Purchasing Analysis (Total)
Number of Unique Items
'''
unqitm = len(data['Item ID'].unique())
print(unqitm)
'''
Average Purchase Price
'''
avgprice = data['Price'].mean()
print(avgprice)
'''
Total Number of Purchases
'''
totalprch = len(data['Purchase ID'].unique())
print(totalprch)
'''
Total Revenue
'''
totalprice = data['Price'].sum()
print(totalprice)

#%%
'''
## Gender Demographics
Percentage and Count of Male Players
Percentage and Count of Female Players
Percentage and Count of Other / Non-Disclosed
'''
data_sn = data.loc[:, ['SN', 'Gender']]

gender_factor = data['Gender'].unique()
print(gender_factor)
gender_count = []
for i in gender_factor:
    count = data_sn[data_sn['Gender'] == i]['SN'].nunique()
    gender_count.append(count)

Male_percentage = gender_count[0]/playercount * 100
print(Male_percentage)

Female_percentage = gender_count[2]/playercount * 100
print(Female_percentage)

other_percentage = gender_count[1]/playercount * 100
print(other_percentage)

#%%
'''
## Purchasing Analysis (Gender)
### The below each broken by gender
Purchase Count
Average Purchase Price
Total Purchase Value
Average Purchase Total per Person by Gender
'''



