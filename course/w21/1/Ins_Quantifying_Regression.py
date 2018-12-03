#%% [markdown]
# # Quantifying Linear Regression
#%% [markdown]
# Create a model to quantify

#%%
# Import dependencies
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression

# Generate some data
X, y = make_regression(n_samples=20, n_features=1, random_state=0, noise=4, bias=100.0)

# Create a linear model
model = LinearRegression()

# Fit (Train) our model to the data
model.fit(X, y)

#%% [markdown]
# ## Quantifying our Model
# 
# * Mean Squared Error (MSE)
# 
# * R2 Score
#%% [markdown]
# There are a variety of ways to quantify the model, but MSE and R2 are very common

#%%
from sklearn.metrics import mean_squared_error, r2_score

# Use our model to predict a value
predicted = model.predict(X)

# Score the prediction with mse and r2
mse = mean_squared_error(y, predicted)
r2 = r2_score(y, predicted)

print(f"Mean Squared Error (MSE): {mse}")
print(f"R-squared (R2 ): {r2}")

#%% [markdown]
# A "good" MSE score will be close to zero while a "good" [R2 Score](https://en.wikipedia.org/wiki/Coefficient_of_determination) will be close to 1.
#%% [markdown]
# R2 Score is the default scoring for many of the Sklearn models

#%%
# Overall Score for the model
model.score(X, y)

#%% [markdown]
# ## Validation
# 
# We also want to understand how well our model performs on new data. 
# 
# One approach for this is to split your data into a training and testing dataset.
# 
# You fit (train) the model using training data, and score and validate your model using the testing data.
# 
# This train/test splitting is so common that Sklearn provides a mechanism for doing this. 
#%% [markdown]
# ## Testing and Training Data
# 
# In order to quantify our model against new input values, we often split the data into training and testing data. The model is then fit to the training data and scored by the test data. Sklean pre-processing provides a library for automatically splitting up the data into training and testing

#%%
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

#%% [markdown]
# Train the model using the training data

#%%
model.fit(X_train, y_train)

#%% [markdown]
# And score the model using the unseen testing data

#%%
model.score(X_test, y_test)

#%% [markdown]
# ## Your Turn!

