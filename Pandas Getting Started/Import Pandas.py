# Installation of Pandas -------------------------------------------------------------------------------------------------------

'''
If you have Python and PIP already installed on a system, then installation of Pandas is very easy.

Install it using this command
'''

# pip install pandas

# Import Pandas ------------------------------------------------------------------------------------------------------------------
# Once Pandas is installed, import it in your applications by adding the import keyword:

import pandas # Now Pandas is imported and ready to use.

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)


# Pandas as pd ----------------------------------------------------------------------------------------------------------------------

# Pandas is usually imported under the pd alias.

# alias: In Python alias are an alternate name for referring to the same thing

# Create an alias with the as keyword while importing:
import pandas as pd

data = {
  'Name': ["Azaz", "Lux", "Harsit"],
  'Roll No': [100, 200, 300]
}

mydata = pd.DataFrame(data)

print(mydata)


# Checking Pandas Version ------------------------------------------------------------------------------------------------------------------

# The version string is stored under __version__ attribute.

print(pd.__version__)