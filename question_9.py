"""
There are different types of users specified in the "User Type" column. 
Find how many there are of each type and store the counts in a pandas Series in the user_types variable.

Hint: What pandas function returns a Series with the counts of each unique value in a column?
"""

import pandas as pd

filename = 'chicago.csv'
df = pd.read_csv(filename)

user_types = df['User Type'].value_counts()
print(user_types)
