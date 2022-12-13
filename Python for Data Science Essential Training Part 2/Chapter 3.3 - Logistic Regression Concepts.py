import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import sklearn

from pandas import Series,DataFrame
from pylab import rcParams
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_predict
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score

rcParams['figure.figsize'] = 5,4
sb.set_style('whitegrid')

address = ('C:/Users/Benjamin Piticaru/Documents/python projects/Python for Data Science Essential Training Part 2/Exercise Files/Data/titanic-training-data.csv')
titanic_training = pd.read_csv(address)
titanic_training.columns = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']

print(titanic_training.info)

## 1. Check that your target variable is binary
#sb.countplot(x='Survived', data=titanic_training, palette='hls')

## 2. Checking for missing values
#titanic_training.isnull().sum()
#titanic_training.describe()

## 3. Taking care of missing variables
#       Need to determine if getting rid of the column
#       is the best course of action
#       Does the variable you are dropping affect the analysis you are 
#       trying to do?

titanic_data = titanic_training.drop(['Name','Ticket','Cabin'], axis=1)

## 4. Imputing missing values
sb.boxplot(x='Parch',y='Age', data=titanic_data, palette='hls')

Parch_groups = titanic_data.groupby(titanic_data['Parch'])
Parch_groups.mean()

def age_approx(cols):
    age = cols[0]
    Parch = cols[1]

    if pd.isnull(age):
        if Parch == 0:
            return 32
        elif Parch == 1:
            return 24
        elif Parch == 2:
            return 17
        elif Parch == 3:
            return 33
        elif Parch == 4:
            return 45
        else:
            return 30
    else: 
        return age

titanic_data['Age']=titanic_data[['Age', 'Parch']].apply(age_approx, axis=1)

titanic_data.dropna(inplace=True)
titanic_data.reset_index(inplace=True, drop=True)

## 5. Converting categorical varaibles to a dummy indicator

## The first part of this code changes male, female to 1,0 respectively
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
gender_cat = titanic_data['Sex']
gender_encoded = label_encoder.fit_transform(gender_cat)

gender_df = pd.DataFrame(gender_encoded, columns=['male_gender'])
#gender_df.head()

## Changes to numbers 0,1,2
embarked_cat = titanic_data['Embarked']
embarked_encoded = label_encoder.fit_transform(embarked_cat)

from sklearn.preprocessing import OneHotEncoder
binary_encoder = OneHotEncoder(categories='auto')
embarked_1hot = binary_encoder.fit_transform(embarked_encoded.reshape(-1,1))
embarked_1hot_mat = embarked_1hot.toarray()
embarked_DF = pd.DataFrame(embarked_1hot_mat, columns = ['C','Q','S'])
## We now have a binary variable of when people got on the boat

## droping variabels we dont need anymore
titanic_data.drop(['Sex','Embarked'], axis=1, inplace=True)

##adding new variables
titanic_dmy = pd.concat([titanic_data, gender_df, embarked_DF], axis=1, verify_integrity=True).astype(float)
titanic_dmy.head()

## Checking for independence between features
sb.heatmap(titanic_dmy.corr())

titanic_dmy.drop(['Fare','Pclass'], axis=1, inplace=True)

## CHecking that your dataset size is sufficient
##   should have at least 50 per variable
titanic_dmy.info()

x_train, x_test, y_train, y_test = train_test_split(titanic_dmy.drop('Survived', axis=1),
                                                    titanic_dmy['Survived'], test_size=0.2,
                                                    random_state=200)

print(x_train.shape)
print(y_train.shape)

x_train[0:5]

## Developing and evaluating the model
LogReg = LogisticRegression(solver='liblinear')
LogReg.fit(x_train,y_train)

y_pred = LogReg.predict(x_test)

## Classification report without cross-validation
print(classification_report(y_test,y_pred))

## K-fold cross-validation and confusion matrices
y_train_pred = cross_val_predict(LogReg, x_train, y_train, cv=5)
confusion_matrix(y_train, y_train_pred)
precision_score(y_train, y_train_pred)

## Make a test prediction
titanic_dmy[863:864]
test_passenger = np.array([866,40,0,0,0,0,0,1]).reshape(1,-1)

print(LogReg.predict(test_passenger))
print(LogReg.predict_proba(test_passenger))


