# Arionsae McCutcheon
# Variable Examples

from ast import keyword

from matplotlib.pylab import around


customer_id = 0 #assuming this is a int because ID usually is numeric

customer_name = "Arionsae" #assuming this is a string but I only put the first name, maybe this needs 2 feilds (First and Last name)

customer_gender = "Female" # this is a simple string variable

customer_DOB = '' # I left an empty string variable because im not sure if this should be an int or not 

drivers_license_number = '' # I left an empty string variable because a license plate has numbers and letters

auto_policy_number = 0 # I assumed this is a int because policy numbers are usually numeric but it could be a string if it has letters in it


creator_name = "Arionsae McCutcheon" # I assumed this is a string variable because it is a name
origin_city = "Buffalo" # I assumed this is a string variable because it is a city name

"""
a) What is the full list of reserved words that can’t be used for variable names? 
b) Pick 5 of these words and review the explanation for how it is used as a keyword in 
Python. Add these 5 definitions as # comments to your exercise document. Put ^^ 
around any terms that you are not familiar with.
"""

# This code below will print the list of reserved words in Python that cannot be used as variable names.
import keyword
key = keyword.kwlist

print(key)

# 5 reserved words and their definitions:


# 1. def: Used to define a function in Python.  
# 2. None: Represents the absence of a value or a null value.
# 3. import: Used to include external modules or libraries in a Python program.
# 4. class: Used to define a class in Python, which is a blueprint for creating objects.
#5. if: Used to make a decision in Python, allowing the program to execute certain code based on a condition.