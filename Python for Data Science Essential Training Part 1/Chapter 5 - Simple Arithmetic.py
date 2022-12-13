import numpy as np
from numpy.random import randn
import pandas as pd

## This determines the number of decimal places (set to 2)
np.set_printoptions(precision=2)

##Create arrays

a = np.array([1,2,3,4,5,6])
b = np.array([[10,20,30],[40,50,60]])

## Create arays via assignment
np.random.seed(25)
c = 36*np.random.rand(6)
d = np.arange(1,35)

## Can use arithmatic with arrays against eachother