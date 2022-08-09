"""
Use pandas to load chicago.csv into a dataframe, and find the most frequent hour when people start traveling. 
There isn't an hour column in this dataset, but you can create one by extracting the hour from the "Start Time" column. 
To do this, you can convert "Start Time" to the datetime datatype using the pandas to_datetime() method and extracting properties such as the hour with these properties.

Hint: Another way to describe the most common value in a column is the mode.
"""

import pandas as pd

filename = 'chicago.csv'

df = pd.read_csv(filename)

df['Start Time'] = pd.to_datetime(df['Start Time'])

df['hour'] = df['Start Time'].dt.hour

popular_hour = df['hour'].mode()[0]

print('Most Popular Start Hour Is: {}'.format(popular_hour))