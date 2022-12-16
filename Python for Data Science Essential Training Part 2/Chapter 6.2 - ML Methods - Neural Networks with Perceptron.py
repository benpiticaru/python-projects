import numpy as np
import pandas as pd
import sklearn

from pandas import Series, DataFrame
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

from sklearn.linear_model import Perceptron

iris = datasets.load_iris()

X = iris.data
y = iris.target

X[0:10,]

## Generating standardized test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
standardize = StandardScaler()
standardized_X_test = standardize.fit_transform(X_test)
standardized_X_train = standardize.fit_transform(X_train)

standardized_X_test[0:10,]

## Generating perceptron data
perceptron = Perceptron(max_iter=50, eta0=0.15, tol=1e-3, random_state=15)
perceptron.fit(standardized_X_train, y_train.ravel())

y_pred = perceptron.predict(standardized_X_test)

print(classification_report(y_test,y_pred))




