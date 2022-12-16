import numpy as np
import pandas as pd
import scipy
import urllib
import sklearn

import matplotlib.pyplot as plt
from pylab import rcParams

from sklearn import neighbors
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import metrics

from sklearn.neighbors import KNeighborsClassifier

np.set_printoptions(precision=4, suppress=True) 
rcParams['figure.figsize'] = 7, 4
plt.style.use('seaborn-whitegrid')

## Importing Data
address = 'Exercise Files/Data/mtcars.csv'

cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

X_prime = cars[['mpg', 'disp', 'hp', 'wt']].values
y = cars.iloc[:,9].values
X = preprocessing.scale(X_prime)
X_train, X_test, y_train, y_test =train_test_split(X, y, test_size=.2, random_state=17)

## Building and training your model with training data
clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)

## Evaluating your model's Predictions
y_pred = clf.predict(X_test)
y_expect = y_test

print(metrics.classification_report(y_expect, y_pred))

