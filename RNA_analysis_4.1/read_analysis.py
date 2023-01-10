import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['figure.figsize'] = 5,4

## format(str) takes the string of an address to a tsv or csv and returns a dataframe that
##  is formatted for polya tail length analysis.
def format_df(location):
    data = pd.read_csv(location, sep='\t')
    data.columns = ['contig','read_length']

    ## Removing values that are less than 0.
    data = data.loc[data['read_length'] >= 80]
    print(len(data))

    ## Group by Contig and calculate average and standard deviation.
    data = data.groupby(data['contig']).agg(
        avg=('read_length','mean'),SD=('read_length','std'))

    ## Produces a csv of data.
    return data

## Adds sample_1 and sample_2 together into one dataframe
##   based on the contig column
def make_plot(sample_1, sample_2):
    df = pd.merge(sample_1, sample_2, on='contig')
    df.drop(df[(df['avg_x'] <= 0) | (df['avg_y'] <= 0)].index, inplace=True)

    ## Creates and determines the trendline column
    z = np.polyfit(x=df.loc[:,'avg_x'], y=df.loc[:,'avg_y'], deg=1)
    p = np.poly1d(z)
    df['trendline'] = p(df.loc[:,'avg_x'])
    print(len(df))
    ## Builds a scatterplot with trendline
    ax = df.plot.scatter(x='avg_x',y='avg_y',color='black')
    df.set_index('avg_x', inplace=True)
    df.trendline.sort_index(ascending=False).plot(ax=ax,color='black')
    plt.xlabel('Sample 1 Average Read Length') 
    plt.ylabel('Sample 2 Average Read Length')
    plt.title('Scatterplot of Unique Gene Average Read Length')
    plt.gca()
    plt.savefig("Read Length Scatterplot")