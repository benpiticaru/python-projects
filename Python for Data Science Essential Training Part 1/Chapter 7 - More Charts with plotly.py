import numpy as np
import pandas as pd
import cufflinks as cf
import chart_studio.plotly as py
import chart_studio.tools as tls
import plotly.graph_objs as go

import sklearn
from sklearn.preprocessing import StandardScaler

tls.set_credentials_file(username='benpiticaru', api_key='On0XPnuMx3AD1l05alXb')

address = "C:/Users/Benjamin Piticaru/Documents/python projects/Exercise Files/Data/mtcars.csv"
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']
mpg = cars.mpg

## how to make a simple histogram in plotly
mpg.iplot(kind='histogram', filename='simple-histogram-chart')

## making multiple histogram chart
cars_subset = cars[['mpg', 'disp', 'hp']]

cars_data_std = StandardScaler().fit_transform(cars_subset)

cars_select = pd.DataFrame(cars_data_std)
cars_select.columns = ['mpg', 'disp', 'hp']

cars_select.iplot(kind='histogram', filename='multiple-histogram-chart')
cars_select.iplot(kind='histogram', subplots=True, filename='subplot-histogram-chart')
cars_select.iplot(kind='histogram', subplots=True, shape=(3,1), filename='subplot-histogram-chart')

## Creating boxplots in plotly
cars_select.iplot(kind='box', filename= 'box-plot')

## Creating a scatterplot in plotly
fig = {'data':[{'x': cars_select.mpg, 'y':cars_select.disp, 'mode':'markers', 'name':'mpg'},
                {'x': cars_select.hp, 'y':cars_select.disp, 'mode':'markers', 'name':'hp'}],
        'layout': {'xaxis':{'title':''}, 'yaxis':{'title':'Standardized Displacement'}}}
py.iplot(fig, filename='grouped-scatterplot')

