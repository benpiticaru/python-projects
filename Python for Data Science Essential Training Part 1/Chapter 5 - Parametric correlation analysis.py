import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sb
from pylab import rcParams

import scipy
from scipy.stats.stats import pearsonr

## matplotlib inline

rcParams['figure.figsize'] = 8,4
plt.style.use('seaborn-whitegrid')

address = "C:/Users/Benjamin Piticaru/Documents/python projects/Exercise Files/Data/mtcars.csv"
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']


## The Pearson Correlation
x = cars[['mpg','hp','qsec','wt']]
## sb.pairplot(x)

mpg = cars['mpg']
hp = cars['hp']
qsec = cars['qsec']
wt = cars['wt']

pearsonr_coefficient, p_value = pearsonr(mpg,hp)
print("PeasonR Correlation Coefficient %0.3f" % (pearsonr_coefficient))

pearsonr_coefficient, p_value = pearsonr(mpg,qsec)
print("PeasonR Correlation Coefficient %0.3f" % (pearsonr_coefficient))

pearsonr_coefficient, p_value = pearsonr(mpg,wt)
print("PeasonR Correlation Coefficient %0.3f" % (pearsonr_coefficient))

## Using Pandas to calclate the Pearson correlation coefficient

corr =x.corr()
corr

## heatmap
sb.heatmap(corr, xticklabels=corr.columns.values, yticklabels=corr.columns.values)


