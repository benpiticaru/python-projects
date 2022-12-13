import pandas as pd

import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb

import sklearn
from sklearn.cluster import DBSCAN
from collections import Counter

rcParams['figure.figsize'] = 5, 4
sb.set_style('whitegrid')

# with this example, we're going to use the same data that we used for the rest of this chapter. So we're going to copy and 
# paste in the code. 
address = 'C:/Users/Benjamin Piticaru/Documents/python projects/Python for Data Science Essential Training Part 2/Exercise Files/Data/iris.data.csv'
df = pd.read_csv(address, header=None, sep=',')

df.columns=['Sepal Length','Sepal Width','Petal Length','Petal Width', 'Species']

data = df.iloc[:,0:4].values
target = df.iloc[:,4].values

## Train your model to identify outliers
## eps is maximum distance between 2 samples for them to still be considered in the same neighborhood
model = DBSCAN(eps=0.8,  min_samples=19).fit(data)
print(model)

## Visualize your results
outliers_df= pd.DataFrame(data)

print(Counter(model.labels_))
print(outliers_df[model.labels_ == -1])

fig = plt.figure()
ax = fig.add_axes([.1,.1,1,1])
colors = model.labels_
ax.scatter(data[:,2], data[:,1], c=colors, s=120)
ax.set_xlabel('Petal Length')
ax.set_ylabel('Sepal Width')
plt.title('DBSCAN for Outlier Detection')




