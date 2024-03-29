import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['figure.figsize'] = 5,4

## Adds sample_1 and sample_2 together into one dataframe
##   based on the contig column
def make_plot(sample_1, sample_2):
    df = pd.merge(sample_1, sample_2, on='contig')
    df = df[['contig','avg_x','avg_y']]
    df.drop(df[(df['avg_x'] <= 0) | (df['avg_y'] <= 0)].index, inplace=True)

    ## Creates and determines the trendline column
    z = np.polyfit(x=df.loc[:,'avg_x'], y=df.loc[:,'avg_y'], deg=1)
    p = np.poly1d(z)
    df['trendline'] = p(df.loc[:,'avg_x'])

    ## Builds a scatterplot with trendline
    ax = df.plot.scatter(x='avg_x',y='avg_y',color='black')
    df.set_index('avg_x', inplace=True)
    df.trendline.sort_index(ascending=False).plot(ax=ax,color='black')
    plt.xlabel('Sample 1 Poly(A) Average Length') 
    plt.ylabel('Sample 2 Poly(A) Average Length')
    plt.title('Scatterplot of Unique Gene Average Poly(A)')
    plt.gca()
    plt.savefig("Poly(a) Scatterplot")



