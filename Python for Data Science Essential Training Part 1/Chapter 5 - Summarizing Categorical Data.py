import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import scipy
from scipy import stats

address = "C:/Users/Benjamin Piticaru/Documents/python projects/Exercise Files/Data/mtcars.csv"
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']
## how to index
cars.index = cars.car_names

carb = cars.carb
carb.value_counts()

## groupby function and then get stats on those groups
cars_cat = cars[['cyl','vs','am','gear','carb']]
gears_group = cars_cat.groupby('gear')
gears_group.describe()

## Transforming Variables to categorical data type
cars['group'] = pd.Series(cars.gear, dtype='category')
cars['group'].dtypes

cars['group'].value_counts()

## Describing a categorical data with crosstabs
pd.crosstab(cars['am'], cars['gear'])

df = cars[['vs','cyl']]
pd.crosstab(cars['vs'],cars['cyl'])

## type.value_counts()
## This code returns a count of the unique values for each 
##    category present in the type variable.

## The idxmax function generates the row index value 
##   where the maximum value is located for a variable within 
##   a dataset.