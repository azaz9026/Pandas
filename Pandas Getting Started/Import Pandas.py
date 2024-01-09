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