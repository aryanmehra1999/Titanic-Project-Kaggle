# Titanic-Project-Kaggle

This is my code for the CodeFunDo++ Challenge using the Titanic Project on Kaggle ( https://www.kaggle.com/c/titanic )

It focuses more on the Data Munging aspect and thus simply uses a logistic regression from sklearn. It depicts how survival in human made disasters can be predicted using various factors. The project will and can be further extended to survival in disasters like floods, hurricanes and their dependance on altitude, residence etc.

The code is beginer friendly and gives extensive know how of the Data Munging and various functions in the code through comments etc. 

The description of each file is as followes:

1. test.csv and train.csv are the test data and training data respectively in their raw formats. They are to be cleaned thoroughly including the exclusion of useless factors and substitution of missing values. 

2. Titanic_Test_Data_Munging and Titanic_Train_Data_Munging are python files to clean the data, replace missing values and create csv files for the Clean Data.

3. CleanTrainData.csv and CleanTestData.csv are clean files with features.

4. LogisticRegression is the file that executed the algo and calculated how well the model does on the training set itself. It also creates a csv file for the predictions on the test set.

5. TestPredictions_Submission has the results with 76% accuracy on the test set.
