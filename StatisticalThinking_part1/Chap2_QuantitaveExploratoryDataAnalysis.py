import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

iris_versicolor = pd.read_csv('datasets/iris.csv')
versicolor_petal_length = iris_versicolor['petal.length']
versicolor_petal_width = iris_versicolor['petal.width']
print(iris_versicolor.head())

# ------------------------------------------------------------------------------- #
# Mean
# compute the 'mean_length_vers'
mean_length_vers = np.mean(versicolor_petal_length)
print('I. versicolor:', mean_length_vers, 'cm')

# ------------------------------------------------------------------------------- #
# Percentiles, outliers, and box plots
# Compute percentiles
# Specify array of percentiles: percentiles
percentiles = np.array([2.5, 25, 50, 75, 97.5])

# Compute percentiles: ptiles_vers
ptiles_vers = np.percentile(versicolor_petal_length, [2.5, 25, 50, 75, 97.5])

# Print the result
print(ptiles_vers)
from StatisticalThinking_part1.Chap1_GraphicalExploratoryDataAnalysis import ecdf

# x_vers, y_vers = ecdf(versicolor_petal_length)

# Plot the ECDF
# _ = plt.plot(x_vers, y_vers, '.')
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('ECDF')

# Overlay percentiles as red diamonds.
# _ = plt.plot(ptiles_vers, percentiles/100, marker='D', color='red', linestyle='none')

# Show the plot
# plt.show()

# ------------------------------------------------------------------------------- #
# Box-and-whisker plot
# Create box plot with Seaborn's default settings
_ = sns.boxplot(x='variety', y='petal.length', data=iris_versicolor)

# Label the axes
_ = plt.xlabel('variety')
_ = plt.ylabel('petal length (cm)')

# Show the plot
# plt.show()

# ------------------------------------------------------------------------------- #
# Variance and standard deviation

# Computing the variance
# Array of differences to mean: differences
differences = versicolor_petal_length - np.mean(versicolor_petal_length)

# Square the differences: diff_sq
diff_sq = differences ** 2

# Compute the mean square difference: variance_explicit
variance_explicit = np.mean(diff_sq)

# Compute the variance using NumPy: variance_np
variance_np = np.var(versicolor_petal_length)

# Print the results
print(variance_explicit, variance_np)

# ------------------------------------------------------------------------------- #
# The standard deviation and the variance
# Compute the variance: variance
variance = np.var(versicolor_petal_length)

# Print the square root of the variance
print(np.sqrt(variance))

# Print the standard deviation
print(np.std(versicolor_petal_length))

# ------------------------------------------------------------------------------- #
# Scatter plots
# Make a scatter plot
_ = plt.plot(versicolor_petal_length, versicolor_petal_width, marker='.', linestyle='none')

# Label the axes
_ = plt.xlabel('versicolor_petal_length')
_ = plt.ylabel('versicolor_petal_width')

# Show the result
plt.show()

# ------------------------------------------------------------------------------- #
# Computing the covariance
# Compute the covariance matrix: covariance_matrix
covariance_matrix = np.cov(versicolor_petal_length, versicolor_petal_width)
print(covariance_matrix)

# Extract covariance of length and width of petals
petal_covariance = covariance_matrix[1, 0]
print(petal_covariance)


# ------------------------------------------------------------------------------- #
# Computing the Pearson correlation coefficient
def pearson_r(x, y):
    """compute Pearson correlation coefficient between two arrays"""
    # compute correlation matrix
    corr_mat = np.corrcoef(x, y)

    return corr_mat


# Compute Pearson correlation coefficient for I. versicolor: r
r = pearson_r(versicolor_petal_length, versicolor_petal_width)
print(r)

# ------------------------------------------------------------------------------- #
