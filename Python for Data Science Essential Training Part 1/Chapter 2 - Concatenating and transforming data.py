import numpy as np
import pandas as pd

from pandas import DataFrame , Series

DF_obj = pd.DataFrame(np.arange(36).reshape(6,6))
DF_obj

DF_obj_2 = pd.DataFrame(np.arange(15).reshape(5,3))
DF_obj_2

##Concatenating Data

pd.concat([DF_obj, DF_obj_2])

##Transforming Data

##Dropping Data

DF_obj.drop([0,2], axis=1)

##by typing axis=1, it changes the focus from rows to columns. The code above drops columns 0 and 2.

##Adding Data

series_obj = Series(np.arange(6))
series_obj.name = "added variable"
series_obj

variable_added = DataFrame.join(DF_obj, series_obj)
variable_added

added_datatable = variable_added.append(variable_added, ignore_index=False)
added_datatable

added_datatable = variable_added.append(variable_added, ignore_index=True)
added_datatable

##Sorting Data

DF_sorted = DF_obj.sort_values(by=(5), ascending=False)
DF_sorted