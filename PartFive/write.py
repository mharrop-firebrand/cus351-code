#! Write to a file
# There are two different methods we can use to write to a file

# write() - this method is used to write a string to a file. It only accepts a string as the argument and for anything else, a TypeError will occur

# writelines() - we can use this method to write a list of strings to a file. This method can accept a string or a list as an argument

#! Important
# ? If this file does not exist then a new file with the specified file-name will be created and content will be added to it
# ? if a file already exists then writing to that file will truncate it. This means any existing content will be deleted and new content will be added to the file

#! write()
# This will write our text in example.txt
# my_file = open("example.txt", "w")
# string_to_write = "This is the brand new line"
# my_file.write(string_to_write)
# my_file.close()


#! writelines()
my_file = open('example2.txt', 'w')
# List of strings seperated by \n for new lines
list_of_string = ['This is the new first line in example2', '\nThis is the second line', '\nFinal Line.']
# So we don't write over out example.py we'll create a new file
# This will create a file and write lines
my_file.writelines(list_of_string)
my_file.close()
# Verify the contents has been added
my_file = open('example2.txt')
print(my_file.read())
my_file.close()