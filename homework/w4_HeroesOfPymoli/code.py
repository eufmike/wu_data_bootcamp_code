'''
# Unit 4: Assignment - Pandas, Pandas, Pandas
## Project: Heroes of Pymoli

Heroes Of Pymoli Data Analysis

* Of the 1163 active players, the vast majority are male (84%). There also exists, a smaller, but notable proportion of female players (14%).

* Our peak age demographic falls between 20-24 (44.8%) with secondary groups falling between 15-19 (18.60%) and 25-29 (13.4%).

Note

* Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

'''

# %%
import os, sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

# %%
# path = '/Users/michaelshih/Documents/code/education/wu_data_bootcamp_code/HeroesOfPymoli'
path = '/Volumes/MacProSSD2/code/wu_data_bootcamp_code/HeroesOfPymoli'

subfolder = 'Resources'
filename = 'purchase_data.csv'
filepath = os.path.join(path, subfolder, filename)

data = pd.read_csv(filepath, header = 0)
data = pd.DataFrame(data)
data.head(10)

# %%
'''
# Player Count
* Display the total number of players
'''

# %%
playercount = len(data['SN'].unique())
# print(playercount)
playercount_df = pd.DataFrame({'Total Players': [playercount]})
playercount_df

# %%
'''
# Purchasing Analysis (Total)
* Run basic calculations to obtain number of unique items, average price, etc.
* Create a summary data frame to hold the results
* Optional: give the displayed data cleaner formatting
* Display the summary data frame
'''

# %%
unqitm = len(data['Item ID'].unique())
avgprice = data['Price'].mean()
totalprch = len(data['Purchase ID'].unique())
totalprice = data['Price'].sum()

primary_analysis_df = pd.DataFrame({
    'Number of Unique Items': [unqitm],
    'Average Price': [avgprice], 
    'Number of Purchases': [totalprch], 
    'Total Revenue': [totalprice],
})
primary_analysis_df['Average Price'] = primary_analysis_df['Average Price'].map('${:.2f}'.format)
primary_analysis_df['Total Revenue'] = primary_analysis_df['Total Revenue'].map('${:,.2f}'.format)
primary_analysis_df

# %%
'''
# Gender Demographics
* Percentage and Count of Male Players
* Percentage and Count of Female Players
* Percentage and Count of Other / Non-Disclosed
'''

# %%
data_sn = data.loc[:, ['SN', 'Gender']]

gender_factor = data['Gender'].unique()

gender_count = []
for i in gender_factor:
    count = data_sn[data_sn['Gender'] == i]['SN'].nunique()
    gender_count.append(count)

gender_percentage = np.array(gender_count) / playercount * 100

gender_analysis_df_01 = pd.DataFrame({
    'Percentage of Players': gender_percentage, 
    'Total Count': gender_count, 
}, index=gender_factor)
gender_analysis_df_01['Percentage of Players'] = \
    gender_analysis_df_01['Percentage of Players'].map('{:.2f}%'.format)

gender_analysis_df_01

# %%
'''
# Purchasing Analysis (Gender)
* Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
* Create a summary data frame to hold the results
* Optional: give the displayed data cleaner formatting
* Display the summary data frame
'''

# %%
# Purchase Count
gender_purchase_count = data.groupby(['Gender'])[['Purchase ID']].count()

# Average Purchase Price
gender_avg_purchase_price = data.groupby(['Gender'])[['Price']].mean()
gender_avg_purchase_price['Price'] = gender_avg_purchase_price['Price'].map('${:.2f}'.format)

# Total Purchase Value
gender_totalprch = data.groupby(['Gender'])[['Price']].sum()
gender_totalprch['Price'] = gender_totalprch['Price'].map('${:.2f}'.format)

# Average Purchase Total per Person by Gender
gender_data_gb = data.groupby(['Gender', 'SN'])[['Price']].mean()
gender_data_gb_2 = gender_data_gb.groupby(['Gender']).mean()
gender_data_gb_2['Price'] = gender_data_gb_2['Price'].map('${:.2f}'.format)

gender_analysis_df_02 = pd.concat([gender_purchase_count, \
                                    gender_avg_purchase_price, \
                                    gender_totalprch, \
                                    gender_data_gb_2
                                    ], axis = 1)

                                    
gender_analysis_df_02.columns = ['Purchase Count', \
                                    'Average Purchase Price', \
                                    'Total Purchase Value', \
                                    'Avg Purchase Total per Person']
gender_analysis_df_02

# %%
'''
# Age Demographics
* Establish bins for ages
* Categorize the existing players using the age bins. Hint: use pd.cut()
* Calculate the numbers and percentages by age group
* Create a summary data frame to hold the results
* Optional: round the percentage column to two decimal points
* Display Age Demographics Table
'''

# %%
# bin data
bin = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

data_age = data
data_age['age_range'] = pd.cut(data_age['Age'], list(bin), labels = group_names)
data_age

# data processing
age_prch_count = data_age.groupby(['age_range', 'SN'])[['SN']].count()
age_prch_count = age_prch_count.groupby(['age_range']).sum()

age_prch_count = age_prch_count.rename(index=str, columns={'SN': 'Total Count'})

# Average Purchase Price
age_prch_percentage = np.array(age_prch_count['Total Count']) / playercount * 100

age_prch_count['Percentage of Players'] = age_prch_percentage
age_prch_count['Percentage of Players'] = age_prch_count['Percentage of Players'].map("{:.2f}%".format)
age_prch_count

age_analysis_df_01 = age_prch_count

# %%
'''
# Purchasing Analysis (Age)
* Bin the purchase_data data frame by age
* Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
* Create a summary data frame to hold the results
* Optional: give the displayed data cleaner formatting
* Display the summary data frame
'''

# %%
# Purchase Count
age_purchase_count = data.groupby(['age_range'])[['Purchase ID']].count()
age_purchase_count['Purchase ID'] = age_purchase_count['Purchase ID'].map("${:.2f}".format)

# Average Purchase Price
age_avg_purchase_price = data.groupby(['age_range'])[['Price']].mean()
age_avg_purchase_price['Price'] = age_avg_purchase_price['Price'].map("${:.2f}".format)

# Total Purchase Value
age_totalprch = data.groupby(['age_range'])[['Price']].sum()
age_totalprch['Price'] = age_totalprch['Price'].map("${:.2f}".format)

# Average Purchase Total per Person
age_prch_count = data_age.groupby(['age_range', 'SN'])[['Price']].mean()
age_prch_count = age_prch_count.groupby(['age_range']).mean()
age_prch_count['Price'] = age_prch_count['Price'].map("${:.2f}".format)

age_analysis_df_02 = pd.concat([age_purchase_count, \
                                age_avg_purchase_price, \
                                age_totalprch,\
                                age_prch_count
                                ], axis = 1)
age_analysis_df_02.columns = ['Purchase Count', \
                                'Average Purchase Price', \
                                'Total Purchase Value', \
                                'Avg Purchase Total per Person']
age_analysis_df_02

# %%
'''
# Top Spenders
* Run basic calculations to obtain the results in the table below
* Create a summary data frame to hold the results
* Sort the total purchase value column in descending order
* Optional: give the displayed data cleaner formatting
* Display a preview of the summary data frame
'''

# %%
spender_top_sum = data.groupby(['SN'])[['Price']].sum()
spender_top_count = data.groupby(['SN'])[['Purchase ID']].count()
spender_top_avg = data.groupby(['SN'])[['Price']].mean()
spender_top = pd.concat([spender_top_count, spender_top_avg, spender_top_sum], axis = 1)
spender_top.columns = ['Purchase Count', 'Average Purchase Price', 'Total Purchase Value'] 
spender_top = spender_top.sort_values('Total Purchase Value', ascending=False)

# clean format
spender_top['Average Purchase Price'] = spender_top['Average Purchase Price'].map("${:.2f}".format)
spender_top['Total Purchase Value'] = spender_top['Total Purchase Value'].map("${:.2f}".format)

topspender_analysis_df = spender_top.head(5)
topspender_analysis_df

# %%
'''
# Most Popular Items
* Retrieve the Item ID, Item Name, and Item Price columns
* Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
* Create a summary data frame to hold the results
* Sort the purchase count column in descending order
* Optional: give the displayed data cleaner formatting
* Display a preview of the summary data frame
'''

# %%
item_top_count = data.groupby(['Item ID', 'Item Name'])[['Purchase ID']].count()
item_top_avg = data.groupby(['Item ID', 'Item Name'])[['Price']].mean()
item_top_sum = data.groupby(['Item ID', 'Item Name'])[['Price']].sum()
item_top = pd.concat([item_top_count, item_top_avg, item_top_sum], axis = 1)

item_top.columns = ['Purchase Count', 'Average Purchase Price', 'Total Purchase Value'] 
item_top = item_top.sort_values('Purchase Count', ascending=False)

item_top['Average Purchase Price'] = item_top['Average Purchase Price'].map("${:.2f}".format)
item_top['Total Purchase Value'] = item_top['Total Purchase Value'].map("${:.2f}".format)

topitem_analysis_df = item_top.head(5)
topitem_analysis_df

# %%
'''
# Most Profitable Items
* Sort the above table by total purchase value in descending order
* Optional: give the displayed data cleaner formatting
* Display a preview of the data frame
'''

# %%
item_top_2 = pd.concat([item_top_count, item_top_avg, item_top_sum], axis = 1)
item_top_2.columns = ['Purchase Count', 'Average Purchase Price', 'Total Purchase Value'] 
item_top_2 = item_top_2.sort_values('Total Purchase Value', ascending=False)

item_top_2['Average Purchase Price'] = item_top_2['Average Purchase Price'].map("${:.2f}".format)
item_top_2['Total Purchase Value'] = item_top_2['Total Purchase Value'].map("${:.2f}".format)

topitem_analysis_df_2 = item_top_2.head(5)
topitem_analysis_df_2