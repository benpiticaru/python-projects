import numpy as np
import pandas as pd
from numpy.random import randn

np.set_printoptions(precision=2)

aa = np.array([[2.,4.,6.],[1.,3.,5],[10.,20.,30.]])
bb = np.array([[0.,1.,2.],[3.,4.,5],[6.,7.,8.]])

## getting the dot product of an array
np.dot(aa,bb)

x=np.array([1,2,7])
y=np.array([3,8,9])
np.dot(x,y)

xx=np.array([[7.,9.],[5.,12.]])
yy=np.array([[2.,8.],[7.,4.]])
#print(np.dot(xx,yy))

dd=np.array([[1.,2.,3.],[4.,5.,6.]])
cc=np.array([[10.,11.],[20.,21.],[30.,31.]])
#print(np.dot(dd,cc))

a=np.array([1,8,2,6,3,8,5,5,5,5])
b=np.array([17,16,20,18,22,15,21,15,17,22])
(a+b)/10

a=np.array([10, 15, 20])
b=([5, 7, 9])
(a-b)*7
