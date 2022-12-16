import os
os.environ["path"]

os.environ["path"]=os.environ["path"]+";C:\\Program Files (x86)\\Graphviz2.38\\bin"

os.environ["path"]

import sklearn.datasets as datasets
import pandas as pd
from sklearn import metrics

iris=datasets.load_iris()

df = pd.DataFrame(iris.data, columns= iris.feature_names)

y = pd.DataFrame(iris.target)

y.columns = ['labels']

df.head()

y.labels.value_counts()

from sklearn.tree import DecisionTreeClassifier

dtree = DecisionTreeClassifier()

dtree.fit(df, y)

from sklearn.externals.six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus

dot_data = StringIO()

export_graphviz(dtree, out_file=dot_data, filled=True, rounded=True, special_characters=True)

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())

Image(graph.create_png())