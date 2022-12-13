#! pip install plotly
#! pip install cufflinks
import numpy as np
import pandas as pd
import cufflinks as cf
import chart_studio.plotly as py
import chart_studio.tools as tls
import plotly.graph_objs as go

tls.set_credentials_file(username='benpiticaru', api_key='On0XPnuMx3AD1l05alXb')

a = np.linspace(start=0,stop=36,num=36)
np.random.seed(25)
b=np.random.uniform(low=0.0 , high=1.0 , size=26)

trace = go.Scatter(x=a , y=b)
data = [trace]

py.iplot(data, filename='basic_line_chart')

address = "C:/Users/Benjamin Piticaru/Documents/python projects/Exercise Files/Data/mtcars.csv"
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']
df = cars[['cyl','wt','mpg']]

layout = dict(title='Chart from Pandas Dataframe', xaxis=dict(title='x-axis'), yaxis=dict(title='yaxis'))
df.iplot(filename='cf-simple-line-chart', layout=layout)

##Creating bar Charts
data = [go.Bar(x=[1,2,3,4,5,6,7,8,9,10], y=[1,2,3,4,0.5,4,3,2,1])]
layout = dict(title='Simple Bar Chart',
            xaxis=dict(title='x-axis'),
            yaxis=dict(title='y-axis'))
py.iplot(data, filename='basic-bar-chart', layout=layout)


## Creating a pie chart
fig = {'data':[{'labels': ['bicycle', 'motorcycle', 'car', 'van', 'stroller'],
                'values':[1,2,3,4,0,5],
                'type':'pie'}],
                'layout': {'title': 'Simple Pie Chart'}}
py.iplot(fig)
