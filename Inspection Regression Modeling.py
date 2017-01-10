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

df = pd.read_csv('D:\\yelp\\restaurant-health\\data2\\the_final_countdown3\\the_final_countdown.csv')
