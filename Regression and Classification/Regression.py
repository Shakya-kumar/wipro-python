# Q1. Implement Multiple Linear Regression to predict Car Price from a dataset (cars.csv).

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data1 = pd.read_csv("cars.csv")
X1 = data1.drop("Price", axis=1)
y1 = data1["Price"]
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=42)
model1 = LinearRegression()
model1.fit(X1_train, y1_train)
y1_pred = model1.predict(X1_test)
print("Car Price Prediction")
print("MSE:", mean_squared_error(y1_test, y1_pred))
print("R2:", r2_score(y1_test, y1_pred))

# Q2. Implement Multiple Linear Regression to predict Profit from the 50_Startups dataset.

data2 = pd.read_csv("50_Startups.csv")
X2 = data2.drop("Profit", axis=1)
y2 = data2["Profit"]
X2 = pd.get_dummies(X2, drop_first=True)
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=42)
model2 = LinearRegression()
model2.fit(X2_train, y2_train)
y2_pred = model2.predict(X2_test)
print("\nProfit Prediction (50_Startups)")
print("MSE:", mean_squared_error(y2_test, y2_pred))
print("R2:", r2_score(y2_test, y2_pred))

# Q3. Implement Multiple Linear Regression to predict Salary from the Salary_Data dataset.

data3 = pd.read_csv("Salary_Data.csv")
X3 = data3.drop("Salary", axis=1)
y3 = data3["Salary"]
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=42)
model3 = LinearRegression()
model3.fit(X3_train, y3_train)
y3_pred = model3.predict(X3_test)
print("\nSalary Prediction")
print("MSE:", mean_squared_error(y3_test, y3_pred))
print("R2:", r2_score(y3_test, y3_pred))

