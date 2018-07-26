# %%
from random import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import sem # Calculates Standard Error of Mean (SEM)

# %%
# regression
sample_size = 100
samples = [[True if random() < 0.5 else False for x in range(0, sample_size)] for y in range(0, 10)]
x_axis = np.arange(0, len(samples))

means = [np.mean(s) for s in samples]
standard_errors = [sem(s) for s in samples]

# %%
# Setting up the plot
fig, ax = plt.subplots()
ax.errorbar(x_axis, means, standard_errors, fmt="o")
ax.set_xlim(-1, len(samples) + 1)
ax.set_title("Will you vote Republican?")
ax.set_xlabel("Sample Number")
ax.set_ylabel("Proportion of People Voting Republican")

plt.show()

# %%
from scipy.stats import linregress

# Set data
x_axis = np.arange(0, 10, 1)
fake = [1, 2.5, 2.75, 4.25, 5.5, 6, 7.25, 8, 8.75, 9.8]

# Set line
(slope, intercept, _, _, _) = linregress(x_axis, fake) #eturns: slope, Intercept, rvalue, pvalue, stderr 
fit = slope * x_axis + intercept

# Plot data
fig, ax = plt.subplots()

fig.suptitle("Fake Banana Data!", fontsize=16, fontweight="bold")

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

ax.set_xlabel("Fake Banana Ages (in days)")
ax.set_ylabel("Fake Banana Weights (in Hundres of Kilograms)")

ax.plot(x_axis, fake, linewidth=0, marker='o')
ax.plot(x_axis, fit, 'b--')

plt.show()


# %%
# T-test
# Dependencies
from random import randint
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import sem

# Generate
high_prices = [randint(1, 5) * 1000 for x in range(1, 10)]
high_means = np.mean(high_prices)
high_sem = sem(high_prices)

low_prices = [randint(1, 5) * 200 for x in range(1, 10)]
low_means = np.mean(low_prices)
low_sem = sem(low_prices)

means = [high_means, low_means]
sems = [high_sem, low_sem]
labels = ["High Prices", "Low Prices"]

# Plot
fig, ax = plt.subplots()

ax.errorbar(np.arange(0, len(means)), means, yerr=sems, fmt="o")

ax.set_xlim(-0.5, 2.5)
ax.set_xticklabels(labels)
ax.set_xticks([0, 1, 2])

ax.set_ylabel("Mean House Price")

plt.show()

#%%
from scipy.stats import sem, ttest_ind # Calculates the T-test for the means of two independent samples of scores.

# t-test
(t_stat, p) = ttest_ind(high_prices, low_prices, equal_var=False)

if p < 0.05:
    print("The differences between the high and low prices are significant.")
else:
    print("The differences between high and low prices are due to chance.")

# %%
# Z score
# Dependencies
from spread import variance, standard_deviation, zipped_z_scores
from stats import mean

a = [30, 31, 31, 32, 32, 40, 41, 41, 141, 1000] 
# b = [-1525, -200, 5, 745, 1000]

print(f'Mean of A: {mean(a)}')
print(f'Variance of A: {variance(a)}')
print(f'Standard Dev A: {standard_deviation(a)}')
print(f'Z-Score of A: {zipped_z_scores(a)}')

def summarize(title, arr):
    print(f"Summarizing {title}")
    print(f"Variance: {variance(arr)}")
    print(f"Standard Deviation: {standard_deviation(arr)}")
    print("Z-Scores: {zipped_z_scores(arr)}")
    print("======")


prices = [4, 425, 984, 2932, 49]
summarize("Prices", prices)