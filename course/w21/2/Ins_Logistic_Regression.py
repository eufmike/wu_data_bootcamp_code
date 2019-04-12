#%% [markdown]
# # Logistic Regression
# 
# Logistic Regression is a statistical method for predicting binary outcomes from data.
# 
# Examples of this are "yes" vs "no" or "young" vs "old". 
# 
# These are categories that translate to probability of being a 0 or a 1 
#%% [markdown]
# We can calculate logistic regression by adding an activation function as the final step to our linear model. 
# 
# This converts the linear regression output to a probability.

# %%
# get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt
import pandas as pd

# %% [markdown]
# Generate some data

# %%
from sklearn.datasets import make_blobs
X, y = make_blobs(centers=2, random_state=42)
print(f"Labels: {y[:10]}")
print(f"Data: {X[:10]}")


#%%
# Visualizing both classes
plt.scatter(X[:, 0], X[:, 1], c=y)

#%% [markdown]
# Split our data into training and testing

#%%
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1, stratify=y)

#%% [markdown]
# Create a Logistic Regression Model

#%%
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier

#%% [markdown]
# Fit (train) or model using the training data

#%%
classifier.fit(X_train, y_train)

#%% [markdown]
# Validate the model using the test data

#%%
print(f"Training Data Score: {classifier.score(X_train, y_train)}")
print(f"Testing Data Score: {classifier.score(X_test, y_test)}")

#%% [markdown]
# Make predictions

#%%
# Generate a new data point (the red circle)
import numpy as np
new_data = np.array([[-2, 6]])
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.scatter(new_data[0, 0], new_data[0, 1], c="r", marker="o", s=100)


#%%
# Predict the class (purple or yellow) of the new data point
predictions = classifier.predict(new_data)
print("Classes are either 0 (purple) or 1 (yellow)")
print(f"The new point was classified as: {predictions}")


#%%
predictions = classifier.predict(X_test)
pd.DataFrame({"Prediction": predictions, "Actual": y_test})


