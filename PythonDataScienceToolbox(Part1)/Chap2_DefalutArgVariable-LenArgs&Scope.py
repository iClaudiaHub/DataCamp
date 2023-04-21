""" Chapter2 Default arguments, variable-length arguments and scope"""

# -------------------------------------------------------------------------------------------------------------------- #
# The keyword global

# Create a sting: team
team = 'teen titans'


# Define change_team()
def change_team():
    """ Change the value of the global variable team."""
    #     Use team in global scope
    global team
    #     Change the value of team in global scope 'justice league'
    team = 'justice league'


print(team)

change_team()

print(team)

# -------------------------------------------------------------------------------------------------------------------- #
# Python's built-in scope

import builtins

print(dir(builtins))


# -------------------------------------------------------------------------------------------------------------------- #
# Nested Functions I
def three_shouts(word1, word2, word3):
    """Return a tuple of stings concatenated with '!!!'."""

    # Define inner
    def inner(word):
        """Return a sting concatenated with '!!!'."""
        # Return a string
        return word + '!!!'

    # Return a tuple of strings
    return inner(word1), inner(word2), inner(word3)


# Call three_shouts() and print
print(three_shouts('a', 'b', 'c'))


# -------------------------------------------------------------------------------------------------------------------- #
# Nested Functions II

def echo(n):
    """Return the inner_echo function."""

    # Define inner echo
    def inner_echo(word1):
        """Concatenate n copies of word1."""
        echo_word = word1 * n
        return echo_word

    # Return inner_echo
    return inner_echo


# Call echo: twice
twice = echo(2)

# Call echo: thrice
thrice = echo(3)

print(twice('hello'), thrice('hello'))


# -------------------------------------------------------------------------------------------------------------------- #
# The keyword nonlocal and nested functions

def echo_shout(word):
    """Change the value of a nonlocal variable"""

    #     Concatenate word with itself:echo_word
    echo_word = word + word
    print(echo_word)

    #     Define inner function shout()
    def shout():
        """Alter a variable in the enclosing scope"""
        #         Use echo_word in nonlocal scope
        nonlocal echo_word
        #         Change echo_word to echo_word concatenated with'!!!'
        echo_word = echo_word + '!!!'

    #   Call function shout()
    shout()
    #     Print echo_word
    print(echo_word)


# Call function echo_shout() with argument "hello"
echo_shout('hello')


# -------------------------------------------------------------------------------------------------------------------- #
# Functions with one default argument
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three exclamation marks at the end of the sting."""
    #     Concatenate echo copies of word1 using * operator.Assign the result to echo_word
    echo_word = word1 * echo
    #     Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + "!!!"
    #     Return shout_word
    return shout_word


# Call shout_echo() with "Hey": no_echo
no_echo = shout_echo("Hey")

# Call shout_echo() with 'Hey' and echo=5: with_echo
with_echo = shout_echo('Hey', echo=5)

print(no_echo)
print(with_echo)


# -------------------------------------------------------------------------------------------------------------------- #
# Functions with multiple default arguments
def shout_echo(word1, echo=1, intense=False):
    """Concatenate echo copies of word1 and three exclamatin marks at the end of the sting."""
    #     Concatenate echo copies pf word1 using * operator: echo_word
    echo_word = word1 * echo
    # Make echo_word uppercase if intense is True
    if intense is True:
        #         Make uppercase and concatenate '!!!': echo_word_new
        echo_word_new = echo_word.upper() + '!!!'
    else:
        #         Concatenate '!!!' to echo_word: echo_word_new
        echo_word_new = echo_word + '!!!'
    #     Return echo_word_new
    return echo_word_new


# Call shout_echo() with 'Hey', echo=5 and intense=True: with_big_echo
with_big_echo = shout_echo("Hey", echo=5, intense=True)

# Call shout_echo() with 'Hey' and intense=True: big_no_echo
big_no_echo = shout_echo("Hey", intense=True)

print(with_big_echo)
print(big_no_echo)


# -------------------------------------------------------------------------------------------------------------------- #
# Functions with variable-length arguments (*args)
def gibberish(*args):
    """Concatenate strings in *args together"""
    #     Initialize an empty sting:hodgepodge
    hodgepodge = ""
    #       Concatenate the strings in args
    for word in args:
        hodgepodge += word

    #   Return hodgepodge
    return hodgepodge


#  Call gibberish() with one string: one_word
one_word = gibberish('luke')
# Call gibberish() with five strings: many_words
many_words = gibberish("luke", "leia", "han", "obi", "darth")

print(one_word)
print(many_words)


# -------------------------------------------------------------------------------------------------------------------- #
# Functions with variable-length keyword arguments (**kwargs)
def report_staus(**kwargs):
    """Print out the status of a movie character."""

    print("\nBEGIN: REPORT\n")

    #   Iterate over the key-value pairs of kwargs
    for keys, value in kwargs.items():
        #         Print out the keys and values, separated by a column
        print(keys + ":" + value)
    print("\nEND REPORT")


# First call to report_status()
report_staus(name='luke', affiliation='jedi', status='missing')

# Second call to report_status()
report_staus(name='anakin', affiliation='sith lord', status='deceased')

# -------------------------------------------------------------------------------------------------------------------- #
# Bringing it all together (1)

import pandas as pd

tweets_df = pd.read_csv('datasets/tweets.csv')


def count_entries(tweets_df, col_name='lang'):
    """return a dictionary with counts of occurrences as value for each key."""
    #     Initialize an empty dictionary:cols_count
    cols_count = {}
    #     Extact column from DataFrame: col
    col = tweets_df[col_name]

    #     Iterate over the column in DataFrame
    for entry in col:
        #         If entry in col_count, add1
        if entry in cols_count.keys():
            cols_count[entry] += 1
        #       Else add the entry to cols_count, set the value to 1
        else:
            cols_count[entry] = 1

    #   Return the cols_count dictionary
    return cols_count


# Call count_entries(): result1
result1 = count_entries(tweets_df)

# call count_entries(): result2
result2 = count_entries(tweets_df, col_name='source')

print(result1)
print(result2)


# -------------------------------------------------------------------------------------------------------------------- #
# Bringing it all together (2)

def count_entries(df, *args):
    """Return a dictionary with counts of occurrences as value for each key."""

    #     Initialize an empty dictionary:cols_count
    cols_count = {}

    #     Iterate over column names in args
    for col_name in args:
        #         Extract column fromDaraFrame: col
        col = tweets_df[col_name]
        #         Iterate over the column in DataFrame
        for entry in col:
            #             If entry is in cols_count, add1
            if entry in cols_count.keys():
                cols_count[entry] += 1
            else:
                cols_count[entry] = 1
    #   Return the cols_count
    return cols_count


# Call count_entries(): result1
result1 = count_entries(tweets_df, 'lang')

# Call count_entries(): result2
result2 = count_entries(tweets_df, 'lang', 'source')

print(result1)
print(result2)

# -------------------------------------------------------------------------------------------------------------------- #
