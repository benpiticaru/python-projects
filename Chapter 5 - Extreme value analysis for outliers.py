import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib import rcParams

## matplotlib inline

rcParams['figure.figsize'] = 5,4

address = "C:/Users/Benjamin Piticaru/Documents/python projects/Exercise Files/Data/iris.data.csv"
df = pd.read_csv(filepath_or_buffer=address, header=None, sep=',')
df.columns=['Sepal Length','Sepal Width','Petal Length','Petal Width','Species',]

x = df.iloc[:, 0:4].values
y = df.iloc[:,4].values
## df[:5]

## Identifying Outliers from Tukey boxplot
df.boxplot(return_type='dict')
plt.plot()

Sepal_width = x[:,1]
iris_outliers = (Sepal_width < 2.05)
df[iris_outliers]

## Applying Tukey outlier labeling
pd.options.display.float_format = '{:.1f}'.format
x_df = pd.DataFrame(x)
print(x_df.describe())

