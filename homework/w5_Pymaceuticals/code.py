# %%
import os, sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from cycler import cycler
import time

# office
# path = '/Users/michaelshih/Documents/code/education/wu_data_bootcamp_code/homework/w5_Pymaceuticals'

# laptop
path = '/Users/major_minor1982/Documents/code/Python/wu_data_bootcamp_code/homework/w5_Pymaceuticals'

# load data
subfolder = 'data'
filename_1 = 'clinicaltrial_data.csv'
filepath_1 = os.path.join(path, subfolder, filename_1)
filename_2 = 'mouse_drug_data.csv'
filepath_2 = os.path.join(path, subfolder, filename_2)

ClinicalTrialData = pd.DataFrame(pd.read_csv(filepath_1))
MouseDrugData = pd.DataFrame(pd.read_csv(filepath_2))

# %%
# merge data
data = ClinicalTrialData.merge(MouseDrugData, left_on = 'Mouse ID', right_on = 'Mouse ID', how = 'outer')
data.head(100)

# %%
# check types of each column
data.dtypes

# %%
# group data
data_avg = data.groupby(['Drug', 'Timepoint'])['Metastatic Sites', 'Tumor Volume (mm3)'].mean()
data_sem = data.groupby(['Drug', 'Timepoint'])['Metastatic Sites', 'Tumor Volume (mm3)'].sem()

# return group factors
drug = list(data_avg.index.levels[0])
timepoint = list(data_avg.index.levels[1])

# %% 
# Tumor Size During Treatment
# plot
ax = plt.subplot(111)
for i in drug:
    ax.errorbar(x = timepoint, y = data_avg.loc[i, 'Metastatic Sites'], 
                 yerr = data_sem.loc[i, 'Metastatic Sites'], 
                 capsize = 3, marker='o'
                 )
ax.legend(drug, loc=9, bbox_to_anchor=(0.5, -0.15), ncol = 2)
ax.grid(True)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.set_xlim(-3, 48)
ax.set_title('Metastatic Spread During Treatment')
ax.set_xlabel('Timepoint (day)')
ax.set_ylabel('Metastatic Site(s)')
plt.show()

# %%
# Metastatic Spread During Treatment
# plot
ax = plt.subplot(111)
for i in drug:
    ax.errorbar(x = timepoint, y = data_avg.loc[i, 'Tumor Volume (mm3)'], 
                 yerr = data_sem.loc[i, 'Tumor Volume (mm3)'], 
                 capsize = 3, marker='o'
                 )
ax.legend(drug, loc=9, bbox_to_anchor=(0.5, -0.15), ncol = 2)
ax.grid(True)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.set_xlim(-3, 48)
ax.set_title('Tumor Response to Treatment')
ax.set_xlabel('Timepoint (day)')
ax.set_ylabel('Tumor Volume ($mm^3$)')
plt.show()

# %%
# Survival chart
# return max mouse count
data_count = data.groupby(['Drug', 'Timepoint'])['Mouse ID'].count()
data_count
mouse_max_count = list(data_count.groupby('Drug').max())

# map 1st day count to a new column
maxcountmatch = dict(zip(drug, mouse_max_count))
data['max'] = data['Drug'].map(maxcountmatch)
data.head(50)

# group data and return a dataframe includes:
# 1. count at each drug and timepoint
# 2. max mouse count
data_count_max = data.groupby(['Drug', 'Timepoint']).agg({'Mouse ID': 'count', 'max': 'mean'})
data_count_max = data_count_max.rename(index = str, columns = {'Mouse ID' : 'count'})
data_count_max.head(50)

# generate a new column for percentage by dividing
# 'count' by max'
data_count_max['percentage'] = data_count_max['count'] / data_count_max['max'] * 100
data_count_max.head(50)

# %%
# make plot
ax = plt.subplot(111)
for i in drug:
    ax.plot(timepoint, data_count_max.loc[i, 'percentage'], '-o')
    # plt.plot(x = timepoint, y = data_count_max.loc[i, 'percentage'], lw=3)
ax.set_xlim(-3, 48)
ax.set_ylim(0, 105)
ax.legend(drug, loc=9, bbox_to_anchor=(0.5, -0.15), ncol = 2)
ax.grid(True)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.set_title('Survival During Treatment')
ax.set_xlabel('Timepoint (day)')
ax.set_ylabel('Servival Rate (%)')
plt.show()