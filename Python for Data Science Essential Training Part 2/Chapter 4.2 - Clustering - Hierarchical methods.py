import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb
import sklearn
import sklearn.metrics as sm

from sklearn.cluster import AgglomerativeClustering

import scipy
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster.hierarchy import fcluster
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist

np.set_printoptions(precision=4, suppress=True)
plt.figure(figsize=(10,3))
plt.style.use('seaborn-whitegrid')

address = 'C:/Users/Benjamin Piticaru/Documents/python projects/Python for Data Science Essential Training Part 2/Exercise Files/Data/mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

x = cars[['mpg','disp','hp', 'wt']].values

y = cars.iloc[:,(9)].values

## Using scipy to generate dendrogram
Z = linkage(x, 'ward')
dendrogram(Z, truncate_mode='lastp', p=12, leaf_rotation=45., leaf_font_size=15, show_contracted=True)
plt.title('Truncated Hierarchial Clustering Diagram')
plt.xlabel('Cluster Size')
plt.ylabel('Distance')

plt.axhline(y = 500)
plt.axhline(y = 150)
plt.show()

## Generating hierarchical clusters
k = 2
Hclustering = AgglomerativeClustering(n_clusters=k, affinity='euclidean', linkage='ward')
Hclustering.fit(x)
sm.accuracy_score(y, Hclustering.labels_)

k = 2
Hclustering = AgglomerativeClustering(n_clusters=k, affinity='euclidean', linkage='average')
Hclustering.fit(x)
sm.accuracy_score(y, Hclustering.labels_)

k = 2
Hclustering = AgglomerativeClustering(n_clusters=k, affinity='manhattan', linkage='average')
Hclustering.fit(x)
sm.accuracy_score(y, Hclustering.labels_)

## basically tried different combinations of affinity and linkage till you get the best score.

##DBSCAN for outlier detection
