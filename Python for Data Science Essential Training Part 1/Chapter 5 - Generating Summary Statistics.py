import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import scipy
from scipy import stats

address = "C:/Users/Benjamin Piticaru/Documents/python projects/Exercise Files/Data/mtcars.csv"
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']

##mLooking at summary statistics that describe a variables numeric values
##  cars.sum()
##  cars.std()
## this shows you the counts for unique values in the gear column
gear = cars.gear 
gear.value_counts()
## This shows you a lot of the stats you would need to use.
cars.describe()
