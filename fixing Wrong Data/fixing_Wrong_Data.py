# fixing Wrong Data ------------------------------------------------------------------------------------------------------------------------------

'''
Replacing Values ----------------------------------------------------------------------------------------------------------------
 
One way to fix wrong values is to replace them with something else.

In our example, it is most likely a typo, and the value should be "45" instead of "450", and we could just insert "45" in row 7:
'''

# Example
# Set "Duration" = 45 in row 7:
import pandas as pd

df = pd.read_csv('data1.csv')

f = df.loc[7, 'Duration'] = 45


#  -------------------------------------------------------------------------------------------------------------------------------------

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120


'''
Removing Rows ---------------------------------------------------------------------------------------------------------------------------

Another way of handling wrong data is to remove the rows that contains wrong data.

This way you do not have to find out what to replace them with, and there is a good chance you do not need them to do your analyses.
'''

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)
    
print(df.to_string())