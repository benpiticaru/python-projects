import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib import rcParams

## matplotlib inline

rcParams['figure.figsize'] = 5,4

address = "C:/Users/Benjamin Piticaru/Documents/python projects/Exercise Files/Data/iris.data.csv"
df = pd.read_csv(filepath_or_buffer=address, header=None, sep=',')
df.columns=['Sepal Length','Sepal Width','Petal Length','Petal Width','Species',]

x = df.iloc[:, 0:4].values
y = df.iloc[:,4].values

## Visually inspecting boxplots
##sb.boxplot(x='Species', y = 'Sepal Length', data=df, palette='hls')

sb.pairplot(df, hue='Species', palette='hls')
