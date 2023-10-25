# The ‘isinstance()’ function can be used to detect the data type of an object using an ‘if’ statement

# This can be useful for writing functions that require objects to be of certain data types

# For example:
# You do not want string values passed to a function for calculating sum
# Similarly, numeric values should not be passed to a function that expects text values


var = 12

if(isinstance(12, int) == True):
    print('You have an integer')
else:
    print('This is no an integer value')