import numpy as np
import pandas as pd
from pandas import DataFrame , Series

address = "C:/Users/Benjamin Piticaru/Documents/python projects/Exercise Files/Data/mtcars.csv"

cars = pd.read_csv(address)

cars.columns = ['car_names','mpg','cyl','disp','hp','qsec','vs','am','gear','carb']
cars.head()

## This takes the average value from each of the columns for each group of cylenders.
cars_groups = cars.groupby(cars['am'])
cars_groups.mean()


## this creates a subset of the dataframe cars with only specific columns.
subset = cars[['disp','mpg','cyl']]
subset.head()

