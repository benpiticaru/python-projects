import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sb

import sklearn
from sklearn import preprocessing
from sklearn.preprocessing import scale

## matplotlib inline

rcParams['figure.figsize'] = 5,4
plt.style.use('seaborn-whitegrid')

address = "C:/Users/Benjamin Piticaru/Documents/python projects/Exercise Files/Data/mtcars.csv"
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']

## Normalizing and transforming features with MinMaxScalar() and fit_transform()

## This scales the data to be between -1 and 1
mpg = cars.mpg
cars[['mpg']].describe()
mpg_matrix = mpg.values.reshape(-1,1)
scaled = preprocessing.MinMaxScaler(feature_range=(0,10))
scaled_mpg = scaled.fit_transform(mpg_matrix)
plt.plot(scaled_mpg)

## Using scale() to scale your features

standardize_mpg = scale(mpg, axis=0, with_mean=False, with_std=False)
plt.plot(standardize_mpg)

standardize_mpg = scale(mpg)