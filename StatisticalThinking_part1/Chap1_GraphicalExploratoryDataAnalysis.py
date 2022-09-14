""" Chapter1 Graphical Exploratory Data Analysis"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


iris_versicolor = pd.read_csv('datasets/iris.csv')
print(iris_versicolor.head())
versicolor_petal_length = iris_versicolor['petal.length']

# --------------------------------------------------------------------------- #
# Set default Seaborn style
sns.set()

# Plot histogram of versicolor petal lengths
_ = plt.hist(versicolor_petal_length)
# plt.show()

# --------------------------------------------------------------------------- #
# Label the axes. Don't forget that you should always include units in your axis labels.
# Your x-axis label is just 'count'. Your y-axis label is 'petal length (cm)'. The units are essential!
_ = plt.hist(versicolor_petal_length)
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('count')
# plt.show()

# --------------------------------------------------------------------------- #
# Adjusting the number of bins in a histogram
# choose the number of bins to be the square root of the number of samples

# Compute number of data points: n_data
n_data = len(versicolor_petal_length)

# Number of bins is the square root of number of data points: n_bins
n_bins = np.sqrt(n_data)

# Convert number of bins to integer: n_bins
n_bins = int(n_bins)
# Plot the histogram
plt.hist(versicolor_petal_length, bins=n_bins)

# Label axes
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('count')
# plt.show()

# --------------------------------------------------------------------------- #
# Plot all of your data: Bee swarm plots
# Create bee swarm plot with Seaborn's default settings
_ = sns.swarmplot(x='variety', y='petal.length', data=iris_versicolor)

# Label the axes
_ = plt.xlabel('variety')
_ = plt.ylabel('petal length (cm)')
plt.show()

# --------------------------------------------------------------------------- #
# Computing the ECDF


# --------------------------------------------------------------------------- #
# --------------------------------------------------------------------------- #
# --------------------------------------------------------------------------- #
# --------------------------------------------------------------------------- #
# --------------------------------------------------------------------------- #
