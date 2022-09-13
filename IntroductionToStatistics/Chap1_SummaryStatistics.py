""" Chapter 1 Summary Statistics"""

import pandas as pd
import numpy as np

food_consumption = pd.read_csv('datasets/food_consumption.csv')

# ------------------------------------------------------------------------------------#
# Mean and median

# Create two DataFrames: one that holds the rows of food_consumption for 'Belgium'
# and another that holds rows for 'USA'. Call these be_consumption and usa_consumption

# Filter for Belgium
be_consumption = food_consumption[food_consumption['country'] == 'Belgium']

# Filter for USA
usa_consumption = food_consumption[food_consumption['country'] == 'USA']

# Calculate mean and median consumption in Belgium
print(np.mean(be_consumption['consumption']))
print(np.median(be_consumption['consumption']))

# Calculate mean and median consumption in USA
print(np.mean(usa_consumption['consumption']))
print(np.median(usa_consumption['consumption']))

# ------------------------------------------------------------------------------------#
# Measures of spread
# Quartiles, quantiles, and quintiles

# Calculate and print the quartiles of co2_emission
print(np.quantile(food_consumption['co2_emission'], [0, 0.25, 0.5, 0.75, 1]))

# Calculate and print the six quantiles that split up the data into 5 pieces (quintiles)
print(np.quantile(food_consumption['co2_emission'], [0, 0.2, 0.4, 0.6, 0.8, 1]))

# Calculate and print the eleven deciles of co2_emission
print(np.quantile(food_consumption['co2_emission'], np.linspace(0, 1, 11)))

# ------------------------------------------------------------------------------------#
# Variance and standard deviation
# Calculate the variance and standard deviation of co2_emission
# for each food_category by grouping and aggregating
print(food_consumption.groupby('food_category')['co2_emission'].agg([np.std, np.var]))

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Create histogram of co2_emission for food_category 'beef'
#food_consumption[food_consumption['food_category'] == 'beef']['co2_emission'].hist()
#plt.show()

# Create histogram of co2_emission for food_category 'eggs'
#food_consumption[food_consumption['food_category'] == 'eggs']['co2_emission'].hist()
#plt.show()

# ------------------------------------------------------------------------------------#
# Finding outliers using IQR

# Calculate the total co2_emission per country by grouping by country and taking the sum
# of co2_emission. Store the resulting DataFrame as emissions_by_country
emissions_by_country = food_consumption.groupby('country')['co2_emission'].sum()
print(emissions_by_country)

# Compute the first and third quartiles of emissions_by_country and store these as q1 and q3
q1 = np.quantile(emissions_by_country, 0.25)
q3 = np.quantile(emissions_by_country, 0.75)

# Calculate the interquartile range of emissions_by_country and store it as iqr
iqr = q3 - q1

# Calculate the lower and upper cutoffs for outliers of emissions_by_country,
# and store these as lower and upper
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

# Subset emissions_by_country to get countries with a total emission
# greater than the upper cutoff or a total emission less than the lower cutoff
outliers = emissions_by_country[(emissions_by_country < lower) | (emissions_by_country > upper)]
print(outliers)

# ------------------------------------------------------------------------------------#
