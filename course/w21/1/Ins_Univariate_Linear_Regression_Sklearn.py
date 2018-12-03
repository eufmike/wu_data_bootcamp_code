
#%%
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#%% [markdown]
# # Linear Regression
#%% [markdown]
# Linear Regression is a fundamental algorithm in machine learning
#%% [markdown]
# It is used as a building block for other ML models
#%% [markdown]
# LR is easy to understand, calculate, and interpret
#%% [markdown]
# LR is fast!
#%% [markdown]
# Often good enough. Don't over-engineer your solution. If your data is linear then use a linear model.
#%% [markdown]
# What is linear data?

#%%
from sklearn.datasets import make_regression

X, y = make_regression(n_samples=20, n_features=1, random_state=0, noise=4, bias=100.0)


#%%
plt.scatter(X, y)

#%% [markdown]
# The response or output is directly proportional to the input
#%% [markdown]
# We can see from the data that we have a linear trend in our model. (The response or output is directly proportional to the input)
#%% [markdown]
# We can use Linear Regression to fit a line through the data.
#%% [markdown]
# ![lr](../Images/linear_regression.jpg)
#%% [markdown]
# Using a trained model allows us to make predictions of the output value (Home Selling Price) given a new input (Number of Bathrooms).
#%% [markdown]
# ![pre-prices1](../Images/predict_prices_1.png)
#%% [markdown]
# New House on the Market
# ![pre-prices2](../Images/predict_prices_2.png)
#%% [markdown]
# We can use our linear model to predict the price of that house
# ![pre-prices3](../Images/predict_prices_3.png)
#%% [markdown]
# What about non-linear data?

#%%
from sklearn.datasets import make_s_curve

data, color = make_s_curve(100, random_state=0)
plt.scatter(data[:,0], color)

#%% [markdown]
# ![happy](../Images/happy.gif)
#%% [markdown]
# ## Linear Regression 
# 
# A regression line is simply calculating a line that best fits the data. This is typically done through the least squares method where the line is chosen to have the smallest overall distance to the points.
# 
# $y = \theta_0 + \theta_1 x$
# 
# * $y$ is the output response
# * $x$ is the input feature
# * $\theta_0$ is the y-axis intercept
# * $\theta_1$ is weight coefficient (slope)
# 
#%% [markdown]
# ## Sklearn
# 
# The Sklearn library provides us with a Linear Regression model that will fit a line to our data. Sklearn follows a consistent API where you define a model object, fit the model to the data, and then make predictions with the model.
# ![sklearn](../Images/sklearn_api.png)
#%% [markdown]
# First, we create the model using the Sklearn LinearRegression model.

#%%
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model

#%% [markdown]
# Next, we fit the model to our data using the fit method. 

#%%
model.fit(X, y)
print(model)

#%% [markdown]
# We can view the coefficients and intercept of the line from the `coef_` and `intercept_` attributes. Note that the `_` suffix indicates that the attribute is available after model is fit to the data (trained).

#%%
print('Weight coefficients: ', model.coef_)
print('y-axis intercept: ', model.intercept_) 

#%% [markdown]
# Our linear model now looks like this: 
# 
# $y = 101.896225057 + 12.44002424 x$
# 
#%% [markdown]
# We can use our model to make predictions.

#%%
predictions = model.predict(X)
print(f"True output: {y[0]}")
print(f"Predicted output: {predictions[0]}")
print(f"Prediction Error: {predictions[0]-y[0]}")


#%%
pd.DataFrame({"Predicted": predictions, "Actual": y, "Error": predictions - y})[["Predicted", "Actual", "Error"]]

#%% [markdown]
# We can calculate the output response for the minimum and maximum input values. Note: This is useful later when we want to plot the fit line.

#%%
x_min = X.min()
x_max = X.max()


#%%
y_min_actual = y.min()
y_max_actual = y.max()


#%%
y_min = 101.896225057 + 12.44002424 * x_min
y_max = 101.896225057 + 12.44002424 * x_max
print(f"Actual Min Value: {y_min_actual}")
print(f"Calculated Min Value: {y_min}")
print(f"Actual Max Value: {y_max_actual}")
print(f"Calculated Max Value: {y_max}")

#%% [markdown]
# We can also use the predict function to calculate predicted values

#%%
y_min_predicted = model.predict(x_min)
y_max_predicted = model.predict(x_max)
print(f"Actual Min Value: {y_min_actual}")
print(f"Predicted Min Value: {y_min_predicted}")
print(f"Actual Max Value: {y_max_actual}")
print(f"Predicted Max Value: {y_max_predicted}")

#%% [markdown]
# We can show the model fit by plotting the predicted values against the original data

#%%
plt.scatter(X, y, c='blue')
plt.plot([x_min, x_max], [y_min, y_max], c='red')

#%% [markdown]
# ## Your Turn!

