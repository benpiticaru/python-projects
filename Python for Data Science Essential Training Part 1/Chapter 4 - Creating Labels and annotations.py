import numpy as np
from numpy.random import randn
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['figure.figsize'] = 8,4

x = range(1,10)
y = [1,2,3,4,.5,4,3,2,1]
plt.bar(x,y)
plt.xlabel('your x-axis label')
plt.ylabel('your y-axis label')

z = [1,2,3,4,.5]
veh_type = ['bycicle','motorbike','car','van','stroller']

plt.pie(z, labels=veh_type)
plt.show()

address = "C:/Users/Benjamin Piticaru/Documents/python projects/Exercise Files/Data/mtcars.csv"
cars = pd.read_csv(address)

cars.columns = ['car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']

mpg = cars.mpg
fig = plt.figure()
ax = fig.add_axes([.1,.1,1,1])

mpg.plot()
ax.set_xticks(range(32))
ax.set_xticklabels(cars.car_names, rotation=60, fontsize='medium')
ax.set_title(' Miles per gallon of Cars in mtcars Dataset')
ax.set_xlabel('car names')
ax.set_ylabel('miles per gallon')
ax.legend(loc='best')
ax.set_ylim([0,45])
ax.annotate('Toyota Corolla', xy=(19,33.9), xytext=(21,35),
            arrowprops=dict(facecolor='black', shrink=0.05))

plt.pie(z)
plt.legend(veh_type, loc='best')
plt.show()