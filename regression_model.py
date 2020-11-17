# -*- coding: utf-8 -*-
"""Regression model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jOWzsg6lHSaVja6LvyDP8UT3h2kb3K21
"""

from google.colab import drive
drive.mount("/content/gdrive")

# Simple Linear Regression

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Importing the data
data = pd.read_csv('/content/gdrive/My Drive/Colab Notebooks/Salary_Data.csv')

X = data.iloc[:, :-1].values
Y = data.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, Y, test_size = 1/3, random_state = 0)

# Fitting Simple Linear Regression to the training set
regressor = LinearRegression()
regressor.fit(X_Train, Y_Train)

# Predicting the Test set result ￼
Y_Pred = regressor.predict(X_Test)
#print(Y_Test.shape)
#print(Y_Pred.shape)

#Calculating metric
m=mean_absolute_error(Y_Pred, Y_Test)
print(m)


# Visualising the Training set results

plt.scatter(X_Train, Y_Train, color = 'black')
plt.plot(X_Train, regressor.predict(X_Train), color = 'blue', label = "training")
plt.scatter(X_Test, Y_Test, color = 'green')
plt.plot(X_Train, regressor.predict(X_Train), color = 'red', label = "testing")
plt.title('Salary vs Experience  (Training Set)')
plt.xlabel('Years')
plt.ylabel('Salary')
plt.legend()
plt.show()

# Visualising the Test set results

#plt.scatter(X_Test, Y_Test, color = 'black')
#plt.plot(X_Train, regressor.predict(X_Train), color = 'blue')
#plt.title('Salary vs Experience  (Training Set)')
#plt.xlabel('Years')
#plt.ylabel('Salary')
#plt.show()