import pandas as pd
import numpy as np
import sklearn
from sklearn.decomposition import FactorAnalysis
from sklearn import datasets

## Getting dataset
iris =  datasets.load_iris()
X = iris.data
variable_names = iris.feature_names

X[0:10,]

## Factor analysis on iris dataset

factor = FactorAnalysis().fit(X)

DF = pd.DataFrame(factor.components_, columns=variable_names)
print(DF)

## assumes features are metric, continuous or ordinal, is r > 0.3 correlation between your features
## factor 1 is highly influencial, factor 2 and 3 should be dropped
