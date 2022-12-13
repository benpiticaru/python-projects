import numpy as np
import pandas as pd

from pandas import DataFrame , Series

DF_obj=DataFrame({'column 1':[1,1,2,2,3,3,3] , 
                  'column 2':['a','a','b','b','c','c','c'],
                  'column 3':['A','A','B','B','B','B','B']})

DF_obj

DF_obj.drop_duplicates(['column 3'])