## This section of code imports the needed modules for working with dataframes
import numpy as np
import pandas as pd

from pandas import DataFrame , Series

missing = np.nan

series_obj = Series(['row 1', 'row 2', missing, 'row 4','row 5','row 6',missing, 'row 8'])

series_obj

series_obj.isnull()

np.random.seed(25)
DF_obj = DataFrame(np.random.rand(36).reshape(6,6))

DF_obj.loc[3:5, 0] = missing
DF_obj.loc[1:4, 5] = missing

DF_obj

filled_DF = DF_obj.fillna(0)
filled_DF

filled_DF = DF_obj.fillna({0: 0.1, 5: 1.25})
filled_DF

fill_DF = DF_obj.fillna(method = 'ffill')
fill_DF

np.random.seed(25)
DF_obj = DataFrame(np.random.rand(36).reshape(6,6))

DF_obj.loc[3:5, 0] = missing
DF_obj.loc[1:4, 5] = missing

DF_obj

DF_obj.isnull().sum()

DF_no_NAN = DF_obj.dropna()
DF_no_NAN

DF_no_NAN = DF_obj.dropna(axis=1)
DF_no_NAN