# In the case of reading, appending or deleting a file, if the file does not already exists then you will get a 'FileNotFoundError'

# We can use the 'os' module and embed an 'if' statement before reading, appending or deleting a file to check if a file exists
import os
# os.remove()
my_file2 = r"C:\Users\mharrop\OneDrive - Firebrand Training Limited\Documents\Teaching\CUS351\WeekThree\PartFive\example.txt"
# If statement for not going to be found
if os.path.exists(my_file2):
    my_file = open(my_file2, 'r')
    print(my_file.read())
    my_file.close()
else:
    print('This file does not exist')