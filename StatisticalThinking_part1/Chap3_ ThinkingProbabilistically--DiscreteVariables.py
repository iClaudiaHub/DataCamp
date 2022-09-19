""" Chapter 3 Thinking Probabilistically-- Discrete Variables"""

import matplotlib.pyplot as plt
import numpy as np

# ------------------------------------------------------ #
# Generating random numbers using the np.random module
# Seed the random number generator:42
np.random.seed(42)

# Initialize random numbers: random_numbers
random_numbers = np.empty(100000)

# Generate random numbers by looping over range(100000)
for i in range(100000):
    random_numbers[i] = np.random.random()

# Plot a histogram
_ = plt.hist(random_numbers)


# plt.show()


# ------------------------------------------------------ #
# The np.random module and Bernoulli trials
def perform_bernoulli_trials(n, p):
    """Perform n Bernoulli trials with success probability p
        and return number of successes."""
    # Initialize number of successes: n_success
    n_success = 0

    # Perform trials
    for i in range(n):
        random_number = np.random.random()
        if random_number < p:
            n_success += 1

    return n_success


# ------------------------------------------------------ #
# How many defaults might we expect?
# Seed random number generator
np.random.seed(42)

# Initialize the number of defaults: n_defaults
n_defaults = np.empty(1000)

# Write a for loop with 1000 iterations to compute the number of defaults per 100 loans using the
# perform_bernoulli_trials() function. It accepts two arguments: the number of trials n - in this case 100 - and the
# probability of success p - in this case the probability of a default, which is 0.05. On each iteration of the loop
# store the result in an entry of n_defaults
for i in range(1000):
    n_defaults[i] = perform_bernoulli_trials(100, 0.5)

# Plot the histogram with default number of bins; label your axes
_ = plt.hist(n_defaults)
_ = plt.xlabel('number of defaults out of 100 loans')
_ = plt.ylabel('probability')
# plt.show()


# ------------------------------------------------------ #
# Will the bank fail?
# Plot the number of defaults you got from the previous exercise,
# in your namespace as n_defaults, as a CDF. The ecdf() function you wrote in the first chapter
def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    n = len(data)
    t = np.sort(data)
    z = np.arange(1, len(t) + 1 / n)
    return t, z


x, y = ecdf(n_defaults)

# Plot the ECDF with labeled axes

_ = plt.plot(x, y, marker='.', linestyle='none')
_ = plt.xlabel('x')
_ = plt.ylabel('y')
# plt.show()

# Compute the number of 100-loan simulations with 10 or more defaults: n_lose_money
n_lose_money = np.sum(n_defaults >= 10)

# Compute and print probability of losing money
print('Probability of losing money =', n_lose_money / len(n_defaults))

# ------------------------------------------------------ #
# Sampling out of the Binomial distribution
# Take 10,000 samples out of the binomial distribution, use parameters n = 100 and p = 0.05,
# and set the size keyword argument to 10000
n_defaults = np.random.binomial(100, 0.05, size=10000)

# Compute CDF: x, y
x, y = ecdf(n_defaults)

# plot de CDF With axis labels:
_ = plt.plot(x, y, marker='.', linestyle='none')
_ = plt.xlabel('')
_ = plt.ylabel('')

# Show the plot
# plt.show()

# ------------------------------------------------------ #
# Plotting the Binomial PMF
# Compute bin edges: bins
bins = np.arange(0, max(n_defaults) + 1.5) - 0.5

# Generate histogram
plt.hist(n_defaults, bins=bins)

# Label axes
_ = plt.xlabel(' ')
_ = plt.ylabel(' ')

# Show the plot
# plt.show()

# ------------------------------------------------------ #
# Relationship between Binomial and Poisson distributions
# Draw 10,000 samples out of Poisson distribution: samples_poisson
sample_poisson = np.random.poisson(10, 10000)

# Print the mean and std
print('Poisson:     ', np.mean(sample_poisson),
                       np.std(sample_poisson))

# Specify values of n and p to consider for Binomial: n, p
n = [20, 100, 1000]
p = [0.5, 0.1, 0.01]

# Draw 10,000 samples for each n,p pair: samples_binomial
for i in range(3):
    samples_binomial = np.random.binomial(n[i], p[i], size=10000 )

# Print results
    print('n =', n[i], 'Binom:', np.mean(samples_binomial),
                                 np.std(samples_binomial))

# ------------------------------------------------------ #
# Was 2015 anomalous?
# Draw 10,000 samples out of Poisson distribution: n_nohitters
n_nohitters = np.random.poisson(251/115, 10000)

# Compute number of samples that are seven or greater: n_large
n_large = np.sum(n_nohitters >= 7)

# Compute probability of getting seven or more: p_large
p_large = n_large / 10000

# Print the result
print('Probability of seven or more no-hitters:', p_large)

# ------------------------------------------------------ #
