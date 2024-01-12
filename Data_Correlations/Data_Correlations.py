# Data Correlations ---------------------------------------------------------------------------------------------------------------------------------------

'''
Finding Relationships -------------------------------------------------------------------------------------------------------------------------------------

A great aspect of the Pandas module is the corr() method.

The corr() method calculates the relationship between each column in your data set.

The examples in this page uses a CSV file called: 'data.csv'.
'''

# Show the relationship between the columns:

# df.corr()

import pandas as pd

df = pd.read_csv('data2.csv')

print(df.corr())

# Note: The corr() method ignores "not numeric" columns.


'''
Perfect Correlation:
We can see that "Duration" and "Duration" got the number 1.000000, which makes sense,
each column always has a perfect relationship with itself.

Good Correlation:
"Duration" and "Calories" got a 0.922721 correlation, which is a very good correlation,
and we can predict that the longer you work out, the more calories you burn, and the 
other way around: if you burned a lot of calories, you probably had a long work out.

Bad Correlation:
"Duration" and "Maxpulse" got a 0.009403 correlation, which is a very bad correlation, 
meaning that we can not predict the max pulse by just looking at the duration of the 
work out, and vice versa.
'''