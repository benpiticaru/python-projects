import numpy as np
from numpy.random import randn
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from matplotlib import rcParams

x = range(1,10)
y = [1,2,3,4,0,4,3,2,1]

plt.plot(x,y)

address = "C:/Users/Benjamin Piticaru/Documents/python projects/Exercise Files/Data/mtcars.csv"

cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']
cars.head()
mpg = cars['mpg']

mpg.plot()

df = cars[['cyl','wt','mpg']]
df.plot()

plt.bar(x,y)

mpg.plot(kind='barh')

x = [1,2,3,4,0.5]
plt.pie(x)
##this saves the file
plt.savefig("pie_chart.png")
plt.show()
