import numpy as np
from numpy.random import randn
import pandas as pd
from pandas import Series, DataFrame
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from pylab import rcParams

rcParams['figure.figsize'] = 5,4

import seaborn as sb
sb.set_style('whitegrid')

address = "C:/Users/Benjamin Piticaru/Documents/python projects/Exercise Files/Data/mtcars.csv"
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']

cars.index = cars.car_names

mpg = cars['mpg']

mpg.plot(kind='hist')

#This is another wat to call the plot
plt.hist(mpg)
plt.plot()

sb.distplot(mpg)

cars.plot(kind='scatter',x='hp',y='mpg', c=['darkgray'], s=150)

sb.regplot(x='hp',y='mpg', data=cars, scatter=True)

sb.pairplot(cars)

cars_subset=cars[['mpg','hp','wt']]
sb.pairplot(cars_subset)
plt.show

cars.boxplot(column='mpg', by='am')
cars.boxplot(column='wt', by='am')

sb.boxplot(x='am', y='mpg', data=cars, palette='hls')