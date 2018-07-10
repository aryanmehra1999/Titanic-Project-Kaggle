#This code is written by: Aryan Mehra, BE Computer Science BITS Pilani

import pandas as pd
import numpy as np
from pandas import DataFrame, Series
import csv

import sklearn
from sklearn.linear_model import LogisticRegression

#Reading the Clean training and test features data from a CSV File
train_features = pd.read_csv('CleanTrainData.csv')
test_features = pd.read_csv('CleanTestData.csv')


#Passenger ID is not a predictive feature
del train_features['PassengerId']
del test_features['PassengerId']

#We have gone through the data to make sure that the features we are using are
#independent, have no corelation whatsoever and our output is binary.


#Take the survival from training data and remove it from features
y_train_actual = train_features['Survived']
del train_features['Survived']

#Define the callable function and object name
LogReg = LogisticRegression()

#Train your model and parameters on the trainig data and its solution
LogReg.fit(train_features,y_train_actual)

#Score will calculate how much the prediction fits the taining data itself
score = LogReg.score(train_features,y_train_actual)

#Using our calculated parameters to calculate the test set predictions
y_test_prediction = LogReg.predict(test_features)

#Writing the numpy array to a organised temporary dataframe
temp = pd.DataFrame()
temp['PassengerId'] = range(892,1310,1)
temp['Survived'] = y_test_prediction
temp.set_index('PassengerId',inplace=True)

#Writing the dataframe into a csv file
temp.to_csv('TestPredictions.csv')


