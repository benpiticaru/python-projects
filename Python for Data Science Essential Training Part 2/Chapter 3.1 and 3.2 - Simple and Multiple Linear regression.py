import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import seaborn as sb

from pylab import rcParams
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, scale
from sklearn.pipeline import make_pipeline

rcParams['figure.figsize'] = 10,8

## Simple linear regression

rooms = 2*np.random.rand(100,1)+3
price = 265 + 6*rooms + abs(np.random.randn(100,1))

##plt.plot(rooms, price, 'r^')
##plt.xlabel("# of rooms, 2019, Average")
##plt.ylabel("2019 Average Home, 1000s USD")
##plt.show

x = rooms
y = price
LinReg = LinearRegression()
LinReg.fit(x,y)
print(LinReg.intercept_,LinReg.coef_)
##print(LinReg.score(x,y))
## the code above will print out the intercept (b in mx+b) and
##   the estimated coefficients.
## score returns the score of the linear regression function (r^2 of the prediction)
##   r^2 value close to 1 is really good.

## (Multiple) Linear regression on the enrolment data
address = 'C:/Users/Benjamin Piticaru/Documents/python projects/Python for Data Science Essential Training Part 2/Exercise Files/Data/enrollment_forecast.csv'

enroll = pd.read_csv(address)
enroll.column = ['year','roll','unem','hgrad','inc']

##sb.pairplot(enroll)

##print(enroll.corr())

enroll_data = enroll[['unem','hgrad']].values

enroll_target = enroll[['roll']].values

enroll_data_names = ['unem','hgrad']

x,y = scale(enroll_data), enroll_target

## Check for missing values
missing_values = x==np.NAN
##x[missing_values==True]

model = make_pipeline(StandardScaler(with_mean=False), LinearRegression())
LinReg = LinearRegression(normalize=True)

model.fit(x,y)
## how well the regression line that was predicted by the model actually matches the real values.
##   how well the model does at predicting. 
print(model.score(x,y))

 
