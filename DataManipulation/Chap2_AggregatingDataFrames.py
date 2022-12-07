""" Chap2 Aggregating DataFrames """

import pandas as pd
import numpy as np

sales = pd.read_csv('datasets/walmart.csv')

# ----------------------------------------------------------------------------------------------------#
# Mean and median

# Explore your new DataFrame first by printing the first few rows of the sales DataFrame.
print(sales.head())

# Print information about the columns in sales
print(sales.info())

# Print the mean of the weekly_sales column
print(sales['weekly_sales'].mean())

# Print the median of the weekly_sales column.
print(sales['weekly_sales'].median())

# ----------------------------------------------------------------------------------------------------#
# Summarizing dates

# Print the maximum of the date column.
print(sales['date'].max())

# Print the minimum of the date column.
print(sales['date'].min())


# ----------------------------------------------------------------------------------------------------#
# Efficient summaries

# Use the custom iqr function defined for you along with .agg()
# to print the IQR of the temperature_c column of sales
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)


# Print IQR of the temperature_c column
print(sales['temperature_c'].agg(iqr))

# Update the column selection to use the custom iqr function with .agg() to print the IQR of temperature_c,
# fuel_price_usd_per_l, and unemployment, in that order
print(sales[['temperature_c', 'fuel_price_usd_per_l', 'unemployment']].agg(iqr))

# Update the aggregation functions called by .agg(): include iqr and np.median in that order
print(sales[['temperature_c', 'fuel_price_usd_per_l', 'unemployment']].agg([iqr, np.median]))

# ----------------------------------------------------------------------------------------------------#
# Cumulative statistics

sales_1_1 = sales[sales['type'] == 'A']

# Sort the rows of sales_1_1 by the date column in ascending order
sales_1_1 = sales_1_1.sort_values('date', ascending=True)

# Get the cumulative sum of weekly_sales and add it as
# a new column of sales_1_1 called cum_weekly_sales
sales_1_1['cum_weekly_sales'] = sales_1_1['weekly_sales'].cumsum()

# Get the cumulative maximum of weekly_sales, and add it as a column called cum_max_sales
sales_1_1['cum_max_sales'] = sales_1_1['weekly_sales'].cummax()

# Print the date, weekly_sales, cum_weekly_sales, and cum_max_sales columns
print(sales_1_1[['date', 'weekly_sales', 'cum_weekly_sales', 'cum_max_sales']])

# ----------------------------------------------------------------------------------------------------#
# Dropping duplicates

# Remove rows of sales with duplicate pairs of store and type and save as store_types and print the head
store_types = sales.drop_duplicates(['store', 'type'])
print(store_types.head())

# Remove rows of sales with duplicate pairs of store and department and save as store_depts and print the head
store_depts = sales.drop_duplicates(['store', 'department'])
print(store_depts)

# Subset the rows that are holiday weeks using the is_holiday column, and drop the duplicate dates,
# saving as holiday_dates
holiday_dates = sales[sales['is_holiday']].drop_duplicates('date')
print(holiday_dates)

# Select the date column of holiday_dates, and print
print(holiday_dates['date'])

# ----------------------------------------------------------------------------------------------------#

# ----------------------------------------------------------------------------------------------------#

# ----------------------------------------------------------------------------------------------------#
