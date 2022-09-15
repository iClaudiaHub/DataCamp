""" Chapter1 Graphical Exploratory Data Analysis"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

iris_versicolor = pd.read_csv('datasets/iris.csv')
# print(iris_versicolor.head())
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
# plt.show()


# --------------------------------------------------------------------------- #
# Computing the ECDF
# Define a function with the signature ecdf(data). Within the function definition,
# Compute the number of data points, n, using the len() function.

def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    # Number of data points: n
    n = len(data)
    # x-data for the ECDF: x
    x = np.sort(data)
    # y-data for the ECDF: y
    y = np.arange(1, len(x) + 1 / n)

    return x, y


# --------------------------------------------------------------------------- #
# Use ecdf() to compute the ECDF of versicolor_petal_length. Unpack the output
# into x_vers and y_vers
x_vers, y_vers = ecdf(versicolor_petal_length)

# Generate plot
_ = plt.plot(x_vers, y_vers, marker='.', linestyle='none')

# Label the axes
_ = plt.xlabel('petal length')
_ = plt.ylabel('ECDF')

# Display the plot
plt.margins(0.02)
# plt.show()

# --------------------------------------------------------------------------- #
# ECDFs also allow you to compare two or more distributions (though plots get cluttered if you have too many).
# Here, you will plot ECDFs for the petal lengths of all three iris species.
# Compute ECDFs
x_set, y_set = ecdf(versicolor_petal_length)
x_vers, y_vers = ecdf(versicolor_petal_length)
x_virg, y_virg = ecdf(versicolor_petal_length)

# Plot all ECDFs on the same plot
_ = plt.plot(x_set, y_set, marker='.', linestyle='none')
_ = plt.plot(x_vers, y_vers, marker='.', linestyle='none')
_ = plt.plot(x_virg, y_virg, marker='.', linestyle='none')

# Annotate the plot
plt.legend(('setosa', 'versicolor', 'virginica'), loc='lower right')
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('ECDF')

# Display plot
plt.show()

# --------------------------------------------------------------------------- #

