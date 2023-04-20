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
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
