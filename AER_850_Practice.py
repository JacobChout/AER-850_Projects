# AER 850 Practice

import pandas as pd

# Reading a CSV file
df = pd.read_csv("C:/Users/Student/Downloads/housing (1).csv")
 
print(df.columns)

x_columns = ['longitude', 'latitude', 'housing_median_age', 'total_rooms',
       'total_bedrooms', 'population', 'households', 'median_income',
       'median_house_value', 'ocean_proximity'] # Every other column apart from the dependent variables

y_column = ['median_house_value'] # Assign this to the dependent variable

x = df[x_columns] # Independent variable
y = df[y_column] # outcome measure, dependent variable



