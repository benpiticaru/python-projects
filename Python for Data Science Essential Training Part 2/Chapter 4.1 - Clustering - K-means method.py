import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

import sklearn
from sklearn.preprocessing import scale
import sklearn.metrics as sm
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import axes3d
from sklearn import datasets

plt.figure(figsize=(7,4))

iris = datasets.load_iris()
x = scale(iris.data)
y = pd.DataFrame(iris.target)
variable_names = iris.feature_names


## Building and running your model
clustering = KMeans(n_clusters=3, random_state=5)
clustering.fit(x)

iris_df = pd.DataFrame(iris.data)
iris_df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
y.columns = ['Targets']

color_theme = np.array(['darkgray','lightsalmon','powderblue'])
plt.subplot(1,2,1)
plt.scatter(x=iris_df.petal_length, y=iris_df.petal_width, c=color_theme[iris.target], s=50)
plt.title('Ground Truth Classification')

plt.subplot(1,2,1)
plt.scatter(x=iris_df.petal_length, y=iris_df.petal_width, c=color_theme[clustering.labels_], s=50)
plt.title('K means Classification')

## relabeling for colours to match
relabel = np.choose(clustering.labels_, [2,0,1]).astype(np.int64)

plt.subplot(1,2,1)
plt.scatter(x=iris_df.petal_length, y=iris_df.petal_width, c=color_theme[iris.target], s=50)
plt.title('Ground Truth Classification')

plt.subplot(1,2,1)
plt.scatter(x=iris_df.petal_length, y=iris_df.petal_width, c=color_theme[relabel], s=50)
plt.title('K means Classification')

## Evaluating your cluster results
##   Want to see a high percision and recall for the model to be relavent
print(classification_report(y, relabel))


