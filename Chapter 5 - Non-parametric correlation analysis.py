import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sb
from pylab import rcParams

import scipy
from scipy.stats import spearmanr

## matplotlib inline

rcParams['figure.figsize'] = 14,7
plt.style.use('seaborn-whitegrid')

address = "C:/Users/Benjamin Piticaru/Documents/python projects/Exercise Files/Data/mtcars.csv"
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']

## Spearman's Rank Correlation
x = cars[['cyl','vs','am','gear']]

cyl = cars['cyl']
vs = cars['vs']
am = cars['am']
gear = cars['gear']

spearmanr_coefficient, p_value = spearmanr(cyl,vs)
print('Spearman Rank Correlation %0.3f' % (spearmanr_coefficient))

spearmanr_coefficient, p_value = spearmanr(cyl,am)
print('Spearman Rank Correlation %0.3f' % (spearmanr_coefficient))

spearmanr_coefficient, p_value = spearmanr(cyl,gear)
print('Spearman Rank Correlation %0.3f' % (spearmanr_coefficient))

## Chi-square test for independence
from scipy.stats import chi2_contingency

table = pd.crosstab(cyl,am)
chi2, p, dof, expected = chi2_contingency(table.values)
print('Chi-square statistic %0.3f p_value %0.3f' % (chi2, p))

table = pd.crosstab(cyl,vs)
chi2, p, dof, expected = chi2_contingency(table.values)
print('Chi-square statistic %0.3f p_value %0.3f' % (chi2, p))

table = pd.crosstab(cyl,gear)
chi2, p, dof, expected = chi2_contingency(table.values)
print('Chi-square statistic %0.3f p_value %0.3f' % (chi2, p))

