## This section of code imports the needed modules for working with dataframes
import numpy as np
import pandas as pd

from pandas import DataFrame , Series

## This line of code gets you a series that have 2 columns
series_obj = Series(np.arange(8), index=['row 1','row 2','row 3','row 4','row 5','row 6','row 7', 'row 8'])


## This line of code gets you a dataframe (chart).
np.random.seed(25)
DF_obj = DataFrame(np.random.rand(36).reshape((6,6)),
                   index=['row 1','row 2','row 3','row 4','row 5','row 6'],
                   columns=['column 1','column 2','column 3','column 4','column 5','column 6'])