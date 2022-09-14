""" Chapter 4 Correlation and Experimental Design"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

world_happiness = pd.read_csv('datasets/world_happiness.csv')

# -------------------------------------------------------------------------------------------- #
# In this exercise, you'll examine the relationship between a country's life expectancy
# (life_exp) and happiness score (happiness_score)
# Create a scatterplot of happiness_score vs. life_exp (without a trendline) using seaborn
# sns.scatterplot(x='life_exp', y='happiness_score', data=world_happiness)
plt.show()

# Create a scatterplot of happiness_score vs. life_exp with a linear trendline using seaborn,
# setting ci to None
# sns.scatterplot(x='life_exp', y='happiness_score', data=world_happiness)
plt.show()

# Calculate the correlation between life_exp and happiness_score. Save this as 'cor'
cor = world_happiness['life_exp'].corr(world_happiness['happiness_score'])
print(cor)

# -------------------------------------------------------------------------------------------- #
# Correlation coefficient
# Create a seaborn scatterplot (without a trendline) showing the relationship between gdp_per_cap
# (on the x-axis) and life_exp (on the y-axis)
sns.scatterplot(x='gdp_per_cap', y='life_exp', data=world_happiness)
plt.show()

# Calculate the correlation between gdp_per_cap and life_exp and store as cor
cor_ = world_happiness['gdp_per_cap'].corr(world_happiness['life_exp'])
print(cor_)

# -------------------------------------------------------------------------------------------- #
# When variables have skewed distributions, they often require a transformation in order to form
# a linear relationship with another variable so that correlation can be computed.
# In this exercise, you'll perform a transformation
# Scatterplot of happiness_score vs. gdp_per_cap
sns.scatterplot(x='gdp_per_cap', y = 'happiness_score', data=world_happiness)
plt.show()

# Calculate correlation
corr_ = world_happiness['happiness_score'].corr(world_happiness['gdp_per_cap'])
print(corr_)

# Create log_gdp_per_cap column that contains the log of gdp-per_cap
world_happiness['log_gdp_per_cap'] = np.log(world_happiness['gdp_per_cap'])

# Scatterplot of log_gdp_per_cap and happiness_score
sns.scatterplot(x='log_gdp_per_cap', y='happiness_score', data=world_happiness)
plt.show()

# Calculate correlation
core = world_happiness['log_gdp_per_cap'].corr(world_happiness['happiness_score'])
print(core)

# -------------------------------------------------------------------------------------------- #
