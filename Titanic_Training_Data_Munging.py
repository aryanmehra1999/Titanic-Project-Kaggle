#This code is written by: Aryan Mehra, BE Computer Science BITS Pilani

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame, Series
import csv

#Reading the data from a CSV File
dataframe = pd.read_csv('train.csv')
features = dataframe.set_index("PassengerId")

#Deleting useless data
del features['Cabin']
del features['Ticket']
del features['Name']

#Storing the actual output and removing from features
survival = features['Survived']
del features['Survived']

#Representing female by 0 and male by 1
features['Sex'].replace('female',0,inplace = True) 
features['Sex'].replace('male',1,inplace = True)

#dealing with 2 missing values of Emabarked
#(S assigned because of fare and survival)
features['Embarked'].replace(np.NaN,'S',inplace = True)

#Replacing the letters of embarking stations by numbers
features['Embarked'].replace('S',1,inplace = True)
features['Embarked'].replace('C',2,inplace = True)
features['Embarked'].replace('Q',3,inplace = True)


#Data wrangling of ages (missing values)

#Creating separate lists for ages 
women_survived = []
women_died = []
men_survived = []
men_died = []

#Fill unknowns with zero because NAN is not comparable 
features['Age'].fillna(0,inplace = True)

for index,row in features.iterrows():
    if row['Age']!=0:                               #Checking missing value
        if row['Sex']==0:                           #appropraite gender check
            if survival[index]==0:
                women_died.append(row['Age'])
            if survival[index]==1:
                women_survived.append(row['Age'])

        if row['Sex']==1:
            if survival[index]==0:
                men_died.append(row['Age'])
            if survival[index]==1:
                men_survived.append(row['Age'])

#calculating average of each category
avg_men_died = sum(men_died)//len(men_died)
avg_women_died = sum(women_died)//len(women_died)
avg_women_survived = sum(women_survived)//len(women_survived)
avg_men_survived = sum(men_survived)//len(men_survived)

#Replacing the missing values using the dataframe.loc function
for index,row in features.iterrows():
    if row['Age']==0:                               
        if row['Sex']==0:                           
            if survival[index]==0:
                features.loc[index,'Age']=avg_women_died        
            if survival[index]==1:
                features.loc[index,'Age']=avg_women_survived

        if row['Sex']==1:
            if survival[index]==0:
                features.loc[index,'Age']=avg_men_died
            if survival[index]==1:
                features.loc[index,'Age']=avg_men_survived

#Used only on training data(larger) to find average age of men and women
#and standard deviations etc of age and fare also used from training set
#even while normalising test set                
#These values will be for our reference to be used in test data

((avg_women_died+avg_women_survived)/2)    #answer is 26.5
((avg_men_died+avg_men_survived)/2)        #answer is 29
(features['Age'].mean())                   #answer is 29.65002244668911
(features['Age'].std())                    #answer is 13.035523676768243
(features['Fare'].mean())                  #answer is 32.204207968574636
(features['Fare'].std())                   #answer is 49.6934285971809


#Feature Normalisation
features['Age'] = (features['Age'] - features['Age'].mean())/(features['Age'].std())
features['Fare'] = (features['Fare'] - features['Fare'].mean())/(features['Fare'].std())

#Adding survival back into the file because we need it while prediction and
#parameter determination in logistic regression. We must remember that they
#are not a part of features as such
features['Survived'] = survival

#Writing Clean Data into a csv file
features.to_csv('CleanTrainData.csv')









    
    

