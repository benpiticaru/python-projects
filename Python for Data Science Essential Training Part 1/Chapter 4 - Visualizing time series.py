import numpy as np
from numpy.random import randn
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from matplotlib import rcParams

address = 'C:/Users/Benjamin Piticaru/Documents/python projects/Exercise Files/Data/Superstore-Sales.csv'

df = pd.read_csv(address, index_col='Order Date', encoding='cp1252',parse_dates=True)

df['Order Quantity'].plot()

df2 = df.sample(n=100, random_state=25, axis=0)

plt.xlabel('Order Date')
plt.ylabel('Order Quantity')
plt.title('Superstore Sales')

df2['Order Quantity'].plot()
