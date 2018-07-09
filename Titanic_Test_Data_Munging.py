import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame, Series
import csv

#Reading the data from a CSV File
dataframe = pd.read_csv('test.csv')
features = dataframe.set_index("PassengerId")

#Deleting useless data
del features['Cabin']
del features['Ticket']
del features['Name']

#Representing female by 0 and male by 1
features['Sex'].replace('female',0,inplace = True) 
features['Sex'].replace('male',1,inplace = True)

#Fill unknowns with zero because NAN is not comparable 
features['Age'].fillna(0,inplace = True)

#Replacing the missing values using the dataframe.loc function
for index,row in features.iterrows():
    if row['Age']==0:                               
        if row['Sex']==0:                           
            features.loc[index,'Age']=26.5  #value from training set        
            
        if row['Sex']==1:
            features.loc[index,'Age']=29    #value from training set



#One missing Fare value is of a Southampton Male.
#We will replace it with the average of that category 
features['Fare'].fillna(-1,inplace = True)

avg_fare_Southampton_man = 0
southampton_man_count = 0
for ind, passenger in features.iterrows():
    if passenger['Embarked']=='S':
        if passenger['Sex']==1:
            if passenger['Fare']!= (-1):
                avg_fare_Southampton_man = avg_fare_Southampton_man + passenger['Fare']
                southampton_man_count = southampton_man_count + 1

#Finally we calculate and replace it
avg_fare_Southampton_man = avg_fare_Southampton_man/southampton_man_count
features['Fare'].replace(-1,avg_fare_Southampton_man,inplace=True)

#Replacing the letters of embarking stations by numbers
features['Embarked'].replace('S',1,inplace = True)
features['Embarked'].replace('C',2,inplace = True)
features['Embarked'].replace('Q',3,inplace = True)

#Feature normalisation using values of mean and standard deviation
#from the training set
features['Age'] = (features['Age'] - 29.65002244668911) / 13.035523676768243
features['Fare'] = (features['Fare'] - 32.204207968574636) / 49.6934285971809

#Writing Clean Data into a csv file
features.to_csv('CleanTestData.csv')

