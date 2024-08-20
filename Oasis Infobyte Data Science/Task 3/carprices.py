# -*- coding: utf-8 -*-
"""carprices.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Mj6AASpZMUwjJ21twqwE5o789h2QZYQV

# **Car Price Prediction**
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler, LabelEncoder

"""## *Extracting the dataset from csv file*"""

car_dataset = pd.read_csv('car data.csv')
car_dataset.head(15)

"""## *Checking for null values and encoding data*"""

car_dataset.info()
car_dataset.describe()
car_dataset.shape
cols = car_dataset.columns
for col in cols:
    print(col, len(car_dataset[col].unique()), "unique values")
encoder = LabelEncoder()
car_dataset['Fuel_Type'] = encoder.fit_transform(car_dataset['Fuel_Type'])
car_dataset['Selling_type'] = encoder.fit_transform(car_dataset['Selling_type'])
car_dataset['Transmission'] = encoder.fit_transform(car_dataset['Transmission'])
car_dataset['Year'] = car_dataset['Year'].apply(lambda x: 2024 - x)
car_dataset

"""## *Extracting essential features and target value*"""

features = car_dataset.drop(['Car_Name', 'Selling_Price'], axis=1)
target = car_dataset['Selling_Price']
features.info()
target.info()

"""## *Splitting into training data & testing data and training the linear regression model*"""

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

"""## *Calculating the error metrics and plotting predicted prices against actual prices*"""

mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error :", mse)
r2 = r2_score(y_test, y_pred)
print("R-squared :", r2)
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual Prices vs Predicted Prices")
plt.show()

"""## *Predicting prices based on user inputs for the features*"""

year = 2024 - int(input("Enter the year of purchase : "))
present_price = float(input("Enter the present price of the car (in lakhs) : "))
km_driven = int(input("Enter the number of kilometers driven : "))
fuel_type = input("Enter the fuel type (Petrol, Diesel, or CNG) : ")
selling_type = input("Enter the selling type (Individual or Dealer) : ")
transmission = input("Enter the transmission type (Manual or Automatic) : ")
owner = int(input("Enter the number of previous owners : (0, 1 or 3) "))
if fuel_type == "CNG":
    fuel_type_int = 0
elif fuel_type == "Diesel":
    fuel_type_int = 1
elif fuel_type == "Petrol":
    fuel_type_int = 2
if selling_type == "Dealer":
    selling_type_int = 0
elif selling_type == "Individual":
    selling_type_int = 1
if transmission == "Manual":
    transmission_int = 1
elif transmission == "Automatic":
    transmission_int = 0
inp_dataframe = pd.DataFrame({ 'Year' : [year], 'Present_Price' : [present_price], 'Driven_kms' : [km_driven],
'Fuel_Type' : [fuel_type_int], 'Selling_type' : [selling_type_int], 'Transmission' : [transmission_int], 'Owner' : [owner]})
pred_price = model.predict(inp_dataframe)
print(f"The predicted selling price of the car is {pred_price[0]:.3f} lakhs.")