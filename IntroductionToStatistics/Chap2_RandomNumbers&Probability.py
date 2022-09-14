"""Chapter 2 Random numbers and probability"""

import pandas as pd
import numpy as np

amir_deals = pd.read_csv('datasets/amir_deals.csv')

# --------------------------------------------------------------------------------------#
# Calculating probabilities
# Count the number of deals Amir worked on for each product type and store in counts
counts = amir_deals['product'].value_counts()
print(counts)

# Calculate the probability of selecting a deal for the different product types by
# dividing the counts by the total number of deals Amir worked on. Save this as probs
probs = counts / amir_deals.shape[0]
print(probs)

# --------------------------------------------------------------------------------------#
# Sampling deals
# Set random seed to 24
np.random.seed(24)

# Sample 5 deals without replacement
sample_without_replacement = amir_deals.sample(5)
print(sample_without_replacement)

# Sample 5 deals with replacement
sample_with_replacement = amir_deals.sample(5, replace=True)
print(sample_with_replacement)

# --------------------------------------------------------------------------------------#
# Discrete distributions

# --------------------------------------------------------------------------------------#
# Continuous distribution

# To model how long Amir will wait for a back-up using a continuous uniform distribution,
# save his lowest possible wait time as min_time and his longest possible wait time as max_time.
# Remember that back-ups happen every 30 minutes
min_time = 0
max_time = 30

# Import uniform from scipy.stats and calculate the probability that Amir has to wait less than
# 5 minutes, and store in a variable called 'prob_less_than_5'
from scipy.stats import uniform

prob_less_than_5 = uniform.cdf(5, 0, 30)
print(prob_less_than_5)

# Calculate the probability that Amir has to wait more than 5 minutes,
# and store in a variable called 'prob_greater_than_5'
prob_greater_than_5 = 1 - uniform.cdf(5, 0, 30)
print(prob_greater_than_5)

# Calculate the probability that Amir has to wait between 10 and 20 minutes,
# and store in a variable called 'prob_between_10_and_20'
prob_between_10_and_20 = uniform.cdf(20, 0, 30) - uniform.cdf(10, 0, 30)
print(prob_greater_than_5)

# --------------------------------------------------------------------------------------#
# The binomial distribution

# import binom from scipy.stats and set the random seed to 10
from scipy.stats import binom
np.random.seed(10)

# Simulate 1 deal worked on by Amir, who wins 30% of the deals he works on
print(binom.rvs(1, 0.3, size=1))

# Simulate 52 weeks of 3 deals
deals = binom.rvs(3, 0.3, size=52)

# Print mean deals won per week
print(np.mean(deals))

# --------------------------------------------------------------------------------------#
# Calculating binomial probabilities

# What's the probability that Amir closes all 3 deals in a week? Save this as 'prob_3'
prob_3 = binom.pmf(3, 3, 0.3)
print(prob_3)

# What's the probability that Amir closes 1 or fewer deals in a week? Save this as 'prob_less_than_or_equal_1'
prob_less_than_or_equal_1 = binom.pmf(1, 3, 0.3)
print(prob_less_than_or_equal_1)

# What's the probability that Amir closes more than 1 deal? Save this as 'prob_greater_than_1'
prob_greater_than_1 = 1 - binom.pmf(1, 3, 0.3)

# --------------------------------------------------------------------------------------#
# Calculate the expected number of sales out of the 3 he works on that Amir will win each week
# if he maintains his 30% win rate
won_30pct = 3 * 0.3
print(won_30pct)

# Calculate the expected number of sales out of the 3 he works on that he'll win if his win rate drops to 25%.
won_25pct = 3 * 0.25
print(won_25pct)

# Calculate the expected number of sales out of the 3 he works on that he'll win if his win rate rises to 35%
won_35pct = 3 * 0.35
print(won_35pct)

# --------------------------------------------------------------------------------------#
