
# %%
# get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np

# %% [markdown]
# # Multiple Linear Regression
# %% [markdown]
# Multiple Linear Regression simply means that you have 
# more than one feature variable.
# 
# For the Housing Price example, you may have features 
# like this:
# 
# $Y_i$ = $Bias_0$ + $Weight_1$ sq_feet + $Weight_2$ num_bedrooms + $Weight_3$ num_bathrooms
# 
# Note: The weights are how important each feature is to the equation. This is the part that the algorithm has to learn.
#%% [markdown]
# The generic formula is:
# 
# $Y_i = Bias_0 + Weight_1 Feature_1 + Weight_2 Feature_2 + \ldots + Weight_p Feature_p$
#%% [markdown]
# The equation is often written as:
# 
# $Y_i = \theta_0 + \theta_1 X_{i1} + \theta_2 X_{i2} + \ldots + \theta_p X_{ip}$
#%% [markdown]
# Generate a linear dataset with 3 features

#%%
from sklearn.datasets import make_regression

n_features = 3
X, y = make_regression(n_samples=30, n_features=n_features, 
                       n_informative=n_features, random_state=42, 
                       noise=0.5, bias=100.0)
print(X.shape)

#%% [markdown]
# With 3 or more dimensions, it becomes harder to visualize the linear trends in our data

#%%
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure(1, figsize=(5, 5))
axes = Axes3D(fig, elev=20, azim=45)
axes.scatter(X[:,0], X[:,1], X[:,2], c=y, cmap=plt.cm.get_cmap("Spectral"))
plt.show()

#%% [markdown]
# We can still visualize 3 features as a 3D plot, but what about n-dimensions? This becomes very difficult for the human brain to visualize. 
#%% [markdown]
# We could pick just one feature from X to fit our model, but what we really want it to find a line that best fits the data in n-dimensional space. To achieve this, Linear Regression can be solved using the analytical approach called [Ordinary Least Squares](https://en.wikipedia.org/wiki/Ordinary_least_squares) or a computational approach [Gradient Descent](https://en.wikipedia.org/wiki/Gradient_descent) for estimating the parameters. Note that there are [tradeoffs](https://stats.stackexchange.com/questions/23128/solving-for-regression-parameters-in-closed-form-vs-gradient-descent) between using either approach. The Linear Regression model in Sklearn uses the Ordinary Least Squares method.
#%% [markdown]
# Luckily, we can just supply our n-dimensional features and sklearn will fit the model using all of our features.

#%%
from sklearn.linear_model import LinearRegression
model = LinearRegression()

# Fitting our model with all of our features in X
model.fit(X, y)

score = model.score(X, y)
print(f"R2 Score: {score}")

#%% [markdown]
# ## Residuals
#%% [markdown]
# Because we can't easily plot our line in 3D space, we can use a residual plot to check our predictions.
#%% [markdown]
# Residuals are the difference between the true values of y and the predicted values of y.

#%%
predictions = model.predict(X)
# Plot Residuals
plt.scatter(predictions, predictions - y)
plt.hlines(y=0, xmin=predictions.min(), xmax=predictions.max())
plt.show()

#%% [markdown]
# We want our predictions to be close to zero on the y-axis in this plot.
#%% [markdown]
# ## Your Turn!

