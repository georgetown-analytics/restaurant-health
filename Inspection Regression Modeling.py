#=============================================================================#
#Imports
#=============================================================================#
import os
import requests
import pandas as pd
import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix
from sklearn import cross_validation as cv
from sklearn.cross_validation import train_test_split as tts
from sklearn.linear_model import Ridge
from sklearn.linear_model import RandomizedLasso
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Lasso
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error as mse
#=============================================================================#
#Data & Descriptives
#=============================================================================#

df = pd.read_csv('D:\\yelp\\restaurant-health\\data2\\the_final_countdown3\\the_final_countdown.csv')

df.shape

df.describe()
#=============================================================================#
#Basic Plots
#=============================================================================#

x = df['stars']
y = df['review_count']
plt.ylabel('review_count')
plt.scatter(x,y)

x = df['review_count']
plt.xlabel= ('review_count')
plt.hist(x, bins= 1000)

#=============================================================================#
#Create dataframe
#=============================================================================#

# data   = df.ix[:, df.columns != 'violations']
data = df[['stars', 'review_count', 'ChangeInViolations', 'IsFastFood', 'IsAsian', 'IsSeafood', 'Pizza', 'IsFrench']]
target = df.violations
data.head()
target.head()

#=============================================================================#
#Cross validation Split
#=============================================================================#

splits = cv.train_test_split(data, target, test_size=0.2)
X_train, X_test, y_train, y_test = splits

#=============================================================================#
#Ridge Regression
#=============================================================================#
model = Ridge(alpha=0.1)
model.fit(X_train, y_train)

expected = y_test
predicted = model.predict(X_test)

print("Ridge Regression model")
print("Mean Squared Error: %0.3f" % mse(expected, predicted))
print("Coefficient of Determination: %0.3f" % r2_score(expected, predicted))

#=============================================================================#
#Normal OLS Regression
#=============================================================================#

model = LinearRegression()
model.fit(X_train, y_train)

expected = y_test
predicted = model.predict(X_test)

print("Linear Regression model")
print("Mean Squared Error: %0.3f" % mse(expected, predicted))
print("Coefficient of Determination: %0.3f" % r2_score(expected, predicted))

#=============================================================================#
#Basic Plots
#=============================================================================#


#=============================================================================#
#Random Forest Regression
#=============================================================================#

model = RandomForestRegressor()
model.fit(X_train, y_train)

expected = y_test
predicted = model.predict(X_test)

print("Random Forest model")
print("Mean squared error = %0.3f" % mse(expected, predicted))
print("R2 score = %0.3f" % r2_score(expected, predicted))

#=============================================================================#
#Lasso Regression
#=============================================================================#

model = Lasso(alpha=0.1)
model.fit(X_train, y_train)

expected  = y_test
predicted = model.predict(X_test)

# Evaluate fit of the model
print("Mean Squared Error: %0.3f" % mse(expected, predicted))
print("Coefficient of Determination: %0.3f" % r2_score(expected, predicted))
