import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import pylab as plt
import seaborn as sb
from IPython.display import Image
from IPython.core.display import HTML 
from pylab import rcParams

import sklearn
from sklearn import datasets

from sklearn import decomposition
from sklearn.decomposition import PCA

rcParams['figure.figsize'] = 5, 4
sb.set_style('whitegrid')

## PCA on the iris dataset
iris = datasets.load_iris()
X = iris.data
variable_names = iris.feature_names

X[0:10,]

pca = decomposition.PCA()
iris_pca = pca.fit_transform(X)

pca.explained_variance_ratio_
pca.explained_variance_ratio_.sum()
## How much information is compressed into the first few components
## need to keep at least 70% of the datasets original information



comps = pd.DataFrame(pca.components_, columns=variable_names)
comps

sb.heatmap(comps, cmap="Blues", annot=True)