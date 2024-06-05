import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# load and investigate the data here:
tennis = pd.read_csv('./tennis_stats.csv')
x = tennis['ServiceGamesPlayed']
y = tennis['ReturnGamesPlayed']

## perform single feature linear regressions here:
train_x, test_x, train_y, test_y = train_test_split(x, y, train_size=0.8, test_size=0.2)

## perform two feature linear regressions here:

## perform multiple feature linear regressions here:
