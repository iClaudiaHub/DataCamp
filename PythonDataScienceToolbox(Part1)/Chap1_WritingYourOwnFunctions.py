""" Chapter1 Writing your own Functions"""


# -------------------------------------------------------------------------------------------------------------------- #
# Write a simple function

# Define the function shout
def shout():
    """ Print a sting with three exclamation marks"""
    shout_word = 'congratulations' + '!!!'
    print(shout_word)


# Call shout
shout()


# -------------------------------------------------------------------------------------------------------------------- #
# Single-parameter functions

# Define shout with the parameter, word
def shout(word):
    """ Print a sting with three exclamation marks"""
    shout_word = word + '!!!'
    print(shout_word)


# Call shout with the sting 'congratulations'
shout('congratulations')


# -------------------------------------------------------------------------------------------------------------------- #
# Functions that return single values

# Define shout with the parameter, word
def shout(word):
    """ Return a string with three exclamation marks"""
    shout_word = word + '!!!'

    #   Replace print with return
    return shout_word


# Pass 'congratulations' to shout: yell
yell = shout('congratulations')

# print yell
print(yell)


# -------------------------------------------------------------------------------------------------------------------- #
#  Functions with multiple parameters

# Define shout with parameters word1 and word2
def shout(word1, word2):
    """ Concatenate strings with three exclamation marks"""
    shout1 = word1 + '!!!'
    shout2 = word2 + '!!!'
    new_shout = shout1 + shout2
    return new_shout


yell = shout('congratulations', 'you')
print(yell)

# -------------------------------------------------------------------------------------------------------------------- #
# A brief introduction to tuples

nums = (3, 4, 6)
print(type(nums))
# Unpack nums into num1, num2, num3
num1, num2, num3 = nums

# Construct a new tuple, even_nums composed of the same elements in nums,
# but with the 1st element replaced with the value, 2.
even_nums = (2, num2, num3)
print(even_nums)

# -------------------------------------------------------------------------------------------------------------------- #
#  Bringing it all together (1)

# Import pandas
import pandas as pd

#  Import Twitter data as DataFrame: df
tweets_df = pd.read_csv("datasets/tweets.csv")

# Initialize an empty dictionary: langs_count
langs_count = {}

# Extract column from DataFrame: col
col = df['lang']

#  Iterate over 'lang' column in DataFrame
for entry in col:
    # If language is in langs_count, add1
    if entry in langs_count.keys():
        langs_count[entry] += 1
    else:
        langs_count[entry] = 1

# Print the populated dictionary
print(langs_count)


# -------------------------------------------------------------------------------------------------------------------- #
# Bringing it all together (2)

# Define the function count_entries(), which has two parameters
def count_entries(df, col_name):
    """ Return a dictionary with counts of occurrences as value for each key"""

    langs_count = {}
    col = df[col_name]

    for entry in col:
        if entry in langs_count.keys():
            langs_count[entry] += 1
        else:
            langs_count[entry] = 1

    return langs_count


result = count_entries(tweets_df, 'lang')
print(result)

# -------------------------------------------------------------------------------------------------------------------- #
