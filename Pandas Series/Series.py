# Pandas Series -----------------------------------------------------------------------------------------------------------------------------------------

'''
What is a Series?
A Pandas Series is like a column in a table.

It is a one-dimensional array holding data of any type.
'''

# Create a simple Pandas Series from a list
import pandas as pd
 
a = [1,2,3,4,5,6]

mydata = pd.Series(a)
print(mydata)

'''
Labels --------------------------------------------------------------------------------------------------------------------------------------------------

If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.

This label can be used to access a specified value.
'''
print(mydata[0])


'''
Create Labels -------------------------------------------------------------------------------------------------------------------------------------------

With the index argument, you can name your own labels.
'''
a = [1, 7, 2]

myvar = pd.Series(a , index = ['x','y','z'])

print(myvar)

# When you have created labels, you can access an item by referring to the label.

# Return the value of "y":

print(myvar["y"])


# Key/Value Objects as Series ----------------------------------------------------------------------------------------------------------------------------

# You can also use a key/value object, like a dictionary, when creating a Series.


calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)


# ---------------------------------------------------------------------------------------


person = {"name":"Azaz" , "Age":21 , "Subject":"Python"}
mydata = pd.Series(person)
print(mydata)

# Create a Series using only data from "name" and "Subject":

print(pd.Series(person , index = ["name" , "Subject"]))


'''
DataFrames -------------------------------------------------------------------------------------------------------------------------------------------------------

Data sets in Pandas are usually multi-dimensional tables, called DataFrames.

Series is like a column, a DataFrame is the whole table.
'''

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)