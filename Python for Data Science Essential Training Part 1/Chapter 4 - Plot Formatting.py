import numpy as np
from numpy.random import randn
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['figure.figsize'] = 5,4

address = "C:/Users/Benjamin Piticaru/Documents/python projects/Exercise Files/Data/mtcars.csv"

x = range(1,10)
y = [1,2,3,4,0.5,4,3,2,1]

##plt.bar(x,y)

wide = [.5,.5,.5,.9,.9,.9,.5,.5,.5]
colour = ['salmon']
plt.bar(x,y, width=wide, color=colour, align='center')

cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']

df = cars[['cyl','mpg','wt']]
df.plot()

color_theme = ['darkgray','lightsalmon','powderblue']
df.plot(color=color_theme)

x1 = range(0,10)
y1 = [10,9,8,7,6,5,4,3,2,1]

plt.plot(x,y, ds='steps', lw=5 )
plt.plot(x1,y1, ls='--',lw=10)

plt.plot(x,y, marker='1', mew=20)
plt.plot(x1,y1, marker='+',mew=15)

