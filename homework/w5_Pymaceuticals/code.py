# %%
import os, sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from cycler import cycler
import time

path = '/Users/michaelshih/Documents/code/education/wu_data_bootcamp_code/homework/w5_Pymaceuticals'
subfolder = 'data'
filename_1 = 'clinicaltrial_data.csv'
filepath_1 = os.path.join(path, subfolder, filename_1)
filename_2 = 'mouse_drug_data.csv'
filepath_2 = os.path.join(path, subfolder, filename_2)

ClinicalTrialData = pd.DataFrame(pd.read_csv(filepath_1))
MouseDrugData = pd.DataFrame(pd.read_csv(filepath_2))

# %%
data = ClinicalTrialData.merge(MouseDrugData, left_on = 'Mouse ID', right_on = 'Mouse ID', how = 'outer')
data.head(100)

# %%
data.dtypes

# %%
data_avg = data.groupby(['Drug', 'Timepoint'])['Metastatic Sites', 'Tumor Volume (mm3)'].mean()
data_sem = data.groupby(['Drug', 'Timepoint'])['Metastatic Sites', 'Tumor Volume (mm3)'].sem()


# %%
list(data_avg.index.levels[0])
list(data_avg.index.levels[1])
# %%
data_avg['Drug']

# %%
fig, ax = plt.subplots()
fig.figure(figsize = (10, 10))


# %%
plt.show()

# Metastatic Spread During Treatment
