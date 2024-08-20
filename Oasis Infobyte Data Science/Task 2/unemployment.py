# -*- coding: utf-8 -*-
"""unemployment.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OIPHAdRCWqib4cVOWVL4lgNEsAuyReam

# **Unemployment Analysis with Python**
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""## *Extracting the dataset from csv files*"""

dataset = pd.read_csv('Unemployment in India.csv')
dataset_upto_11_2020 = pd.read_csv('Unemployment_Rate_upto_11_2020.csv')
dataset.head(10)
dataset_upto_11_2020.head(10)

"""## *Checking for null values and cleaning the data*"""

dataset.info()
dataset_upto_11_2020.info()
dataset.dropna(inplace = True)
dataset_upto_11_2020.columns = ["State", "Date", "Frequency", "Unemployment Rate",
                                "Employed", "Labour Participation Rate", "Region", "Latitude", "Longitude"]
dataset.columns = ["State", "Date", "Frequency", "Unemployment Rate", "Employed", "Labour Participation Rate", "Area"]
print("\n|| After updating column names and removing empty rows ||\n")
dataset.info()
dataset_upto_11_2020.info()
dataset.shape

"""## *Extracting features and target to show various statistical plots*

### Plotting pie chart on unemployment in major regions of India
"""

regions_based_percentage = []
for i in dataset_upto_11_2020['Region'].unique():
    regions_based_percentage.append(sum([1 for j in dataset_upto_11_2020[dataset_upto_11_2020['Region'] == i]['Unemployment Rate'] if j > dataset_upto_11_2020[dataset_upto_11_2020['Region'] == i]['Unemployment Rate'].mean()]))
plt.pie(regions_based_percentage, labels = dataset_upto_11_2020['Region'].unique(), autopct = '%.2f%%')
plt.show()

"""### Plotting bar graphs on unemployment in various states and UTs within each of the major regions"""

plt.figure(figsize=(20,30))
regions = dataset_upto_11_2020['Region'].unique()
for i in range(len(regions)):
    plt.subplot(5, 1, i+1)
    plt.title(regions[i], fontsize = 24)
    regionwise = dataset_upto_11_2020[dataset_upto_11_2020['Region'] == regions[i]]
    plt.bar(regionwise['State'], regionwise['Unemployment Rate'])
plt.show()

"""### Plotting pie chart on unemployment in rural and urban areas"""

rural_dataset = dataset[dataset['Area'] == "Rural"]
urban_dataset = dataset[dataset['Area'] == "Urban"]
area_based_percentage = [sum([1 for i in rural_dataset['Unemployment Rate'] if i > rural_dataset['Unemployment Rate'].mean()]),
sum([1 for i in urban_dataset['Unemployment Rate'] if i > urban_dataset['Unemployment Rate'].mean()])]
plt.pie(area_based_percentage, labels = ['Rural', 'Urban'], autopct = '%.2f%%')
plt.show()

"""### Plotting the data points with latitude and longitude, and labelling with respect to the mean unemployment rate"""

features = dataset_upto_11_2020[['Latitude', 'Longitude']]
target = dataset_upto_11_2020['Unemployment Rate']
plt.scatter(features['Longitude'], features['Latitude'], c = target)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
legend = target.quantile([0.25, 0.5, 0.75]).values
legend_string = map(str, legend)
plt.legend(list(legend_string))
plt.show()