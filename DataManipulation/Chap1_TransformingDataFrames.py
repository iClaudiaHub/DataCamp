""" Chapter1 Transforming DataFrames"""

import pandas as pd

homelessness = pd.read_csv('datasets/homelessness.csv')

# --------------------------------------------------------------------------------------#
# Inspecting a DataFrame

# Print the head of the homelessness DataFrame
print(homelessness.head())

# Print information about the column types and missing values in homelessness
print(homelessness.info())

# Print the number of rows and columns in homelessness
print(homelessness.shape)

# Print some summary statistics that describe the homelessness DataFrame
print(homelessness.describe())

# --------------------------------------------------------------------------------------#
# Parts of a DataFrame

# Print the values of homelessness
print(homelessness.values)

# Print the column index of homelessness
print(homelessness.columns)

# Print the row index of homelessness
print(homelessness.index)

# --------------------------------------------------------------------------------------#
# Sorting rows

# Sort homelessness by the number of homeless individuals, from smallest to largest,
# and save this as homelessness_ind.
# Print the head of the sorted DataFrame
homelessness_ind = homelessness.sort_values('individuals')
print(homelessness_ind.head())

# Sort homelessness by the number of homeless family_members in descending order,
# and save this as homelessness_fam.
# Print the head of the sorted DataFrame
homelessness_fam = homelessness.sort_values('family_members', ascending=False)
print(homelessness_fam.head())

# Sort homelessness first by region (ascending), and then by number of family members (descending).
# Save this as homelessness_reg_fam.
# Print the head of the sorted DataFrame
homelessness_reg_fam = homelessness.sort_values(['region', 'family_members'], ascending=[True, False])
print(homelessness_reg_fam.head())

# --------------------------------------------------------------------------------------#
# Subsetting columns

# Create a DataFrame called individuals that contains only the individuals column of homelessness.
# Print the head of the result.
individuals = homelessness['individuals']
print(individuals.head())

# Create a DataFrame called state_fam that contains only the state and family_members columns of homelessness,
# in that order.
# Print the head of the result
state_fam = homelessness[['state', 'family_members']]
print(state_fam.head())

# Create a DataFrame called ind_state that contains the individuals and state columns of homelessness, in that order.
# Print the head of the result.
ind_state = homelessness[['individuals', 'state']]
print(ind_state.head())

# --------------------------------------------------------------------------------------#
# Subsetting rows by categorical variables

# Filter homelessness for cases where the USA census region is "South Atlantic" or it is "Mid-Atlantic",
# assigning to south_mid_atlantic. View the printed result.
south_mid_atlantic = homelessness[(homelessness['region'] == 'South Atlantic') |
                                  (homelessness['region'] == 'Mid_Atlantic')]
print(south_mid_atlantic)

# Filter homelessness for cases where the USA census state is in the list of Mojave states, canu,
# assigning to mojave_homelessness. View the printed result.
canu = ["California", "Arizona", "Nevada", "Utah"]

mojave_homelessness = homelessness[homelessness['state'].isin(canu)]
print(mojave_homelessness)

# --------------------------------------------------------------------------------------#
# Adding new columns

# Add a new column to homelessness, named total, containing the sum of the individuals and family_members columns.
homelessness['total'] = homelessness['individuals'] + homelessness['family_members']

# Add another column to homelessness, named p_individuals, containing the proportion of homeless people
# in each state who are individuals.
homelessness['p_individuals'] = homelessness['individuals'] / homelessness['total']
print(homelessness)

# --------------------------------------------------------------------------------------#
# Combo-attack!

# Add a column to homelessness, indiv_per_10k, containing the number of homeless individuals
# per ten thousand people in each state
homelessness['indiv_per_10k'] = 1000 * homelessness['individuals'] / homelessness['state_pop']

# Subset rows where indiv_per_10k is higher than 20, assigning to high_homelessness
high_homelessness = homelessness[homelessness['indiv_per_10k'] > 20]

# Sort high_homelessness by descending indiv_per_10k, assigning to high_homelessness_srt
high_homelessness_str = high_homelessness.sort_values('indiv_per_10k', ascending=False)

# Select only the state and indiv_per_10k columns of high_homelessness_srt and save as result.
# Look at the result
result = high_homelessness_str[['state', 'indiv_per_10k']]
print(result)

# --------------------------------------------------------------------------------------#
