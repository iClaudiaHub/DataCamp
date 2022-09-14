"""Chapter 3 More Distributions... """

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

amir_deals = pd.read_csv('datasets/amir_deals.csv')

# ---------------------------------------------------------------------------- #
# Normal Distribution
# Create a histogram with 10 bins to visualize the distribution of the 'amount'.
# Show the plot.
# amir_deals['amount'].hist(bins=10)
plt.show()

# ---------------------------------------------------------------------------- #
# Probabilities from the normal distribution
# mean = $5000
# standard deviation = $ 2000
# What's the probability of Amir closing a deal worth less than $7500?
prob_less_7500 = norm.cdf(7500, 5000, 2000)
print(prob_less_7500)

# What's the probability of Amir closing a deal worth more than $1000?
prob_over_1000 = 1 - norm.cdf(1000, 5000, 2000)
print(prob_over_1000)

# What's the probability of Amir closing a deal worth between $3000 and $7000?
prob_3000_to_7000 = norm.cdf(7000, 5000, 2000) - norm.cdf(3000, 5000, 2000)
print(prob_3000_to_7000)

# What amount will 25% of Amir's sales be less than?
pct_25 = norm.ppf(0.25, 5000, 2000)
print(pct_25)

# ---------------------------------------------------------------------------- #
# Simulating sales under new market conditions
# Currently, Amir's average sale amount is $5000.
# Calculate what his new average amount will be if it increases by 20% and store this in 'new_mean'
new_mean = 5000 * 1.2

# Amir's current standard deviation is $2000.
# Calculate what his new standard deviation will be if it increases by 30% and store this in 'new_sd'
new_sd = 2000 * 1.3

# Create a variable called 'new_sales', which contains 36 simulated amounts from a normal distribution
# with a mean of new_mean and a standard deviation of new_sd
new_sales = norm.rvs(new_mean, new_sd, size=36)

# Plot the distribution of the new_sales amounts using a histogram and show the plot
# plt.hist(new_sales)
plt.show()

# ---------------------------------------------------------------------------- #
# The central limit
# The central limit theorem states that a sampling distribution of a sample statistic approaches
# the normal distribution as you take more samples, no matter the original distribution being sampled from.
# Create a histogram of the num_users column of amir_deals and show the plot
# amir_deals['num_users'].hist()
plt.show()

# Set the seed to 104.
# Take a sample of size 20 with replacement from the num_users column of amir_deals, and take the mean
np.random.seed(104)
samp_20 = amir_deals['num_users'].sample(20, replace=True)
print(np.mean(samp_20))

# Repeat this 100 times using a for loop and store as 'sample_means'.
# This will take 100 different samples and calculate the mean of each.
sample_means = []

for i in range(100):
    samp_20 = amir_deals['num_users'].sample(20, replace=True)
    samp_20_mean = np.mean(samp_20)
    sample_means.append(samp_20)

print(sample_means)

# Convert to Series and plot histogram
sample_means_series = pd.Series(sample_means)
# sample_means_series.hist()
plt.show()

# ---------------------------------------------------------------------------- #
# The mean of means
# Set the random sees to 321
np.random.seed(321)

# Take 30 samples (with replacement) of size 20 from amir_deals['num_users']
# and take the mean of each sample. Store the sample means in 'sample_meanss'
sample_meanss = []
for i in range(30):
    cur_sample = amir_deals['num_users'].sample(20, replace=True)
    cur_sample = np.mean(cur_sample)
    sample_meanss.append(cur_sample)

# Print mean of sample_means
print(np.mean(sample_means))

# Print mean of num_users in amir_deals
print(np.mean(amir_deals['num_users']))

# ---------------------------------------------------------------------------- #
# Poisson Distribution
# Import poisson from scipy.stats and calculate the probability that Amir responds
# to 5 leads in a day, given that he responds to an average of 4
from scipy.stats import poisson
prob_5 = poisson.pmf(5, 4)
print(prob_5)

# ---------------------------------------------------------------------------- #
# More distributions
# Import expon from scipy.stats. What's the probability it takes Amir less than
# an hour to respond to a lead? On average, it takes 2.5 hours
from scipy.stats import expon
less_1_hour = expon.cdf(1, scale=2.5)
print(less_1_hour)

# What's the probability it takes Amir more than 4 hours to respond to a lead?
more_4_hours = 1 - expon.cdf(4, scale=2.5)
print(more_4_hours)

# What's the probability it takes Amir 3-4 hours to respond to a lead?
to_3_or_4 = expon.cdf(4, scale=2.5) - expon.cdf(3, scale=2.5)
print(to_3_or_4)

# ---------------------------------------------------------------------------- #
