#
#! NOT WITH OPEN
# Create a text file named "my_file.txt" and add the following content to it:
# "Hello, this is the initial content of the file."
# "This is the second line in the file."
# my_file = open('my_file.txt', 'x')
# my_file.close()
# Read the entire content of the file using the read() method and print it to the console.
# my_file = open('my_file.txt', 'r')
# print(my_file.read())
# my_file.close()
# Read the file line by line using the readlines() method and print each line (without newline characters) to the console.
# my_file = open('my_file.txt', 'r')
# for line in my_file.readlines():
#     print(line)
# my_file.close()
# Read the file using the readline() method and print the first and second lines to the console.
# my_file = open('my_file.txt', 'r')
# first_line = my_file.readline()
# print(first_line)
# second_line = my_file.readline()
# print(second_line)
# my_file.close()
# Append a new line to the file with the content: "This line is appended to the file."
# my_file = open('my_file.txt', 'a')
# my_file.write("\nThis line is appended to the file.")
# my_file.close()
# Read the updated content of the file using the read() method and print it to the console.
# my_file = open('my_file.txt', 'r')
# print(my_file.read())
# my_file.close()
# Overwrite the entire file with the content: "This content overwrites the entire file."
# my_file = open('my_file.txt', 'w')
# overwrite = "This content overwrites the entire file."
# my_file.write(overwrite)
# my_file.close()
# Read the overwritten content of the file using the read() method and print it to the console.
# my_file = open('my_file.txt', 'r')
# print(my_file.read())
# my_file.close()
# Remove the file "my_file.txt," and make sure to handle the case where the file doesn't exist.
import os

# try:
#     os.remove("my_file.txt")
#     print('File has been sucessfully removed')
# # Verify that the file has been removed (or if it didn't exist, print a message indicating that).◘
# except FileNotFoundError:
#     print('File does not exist')


#! With Open

# Open a new text file named "practice_file.txt" using the with open() statement.
# Write some text into the file.
# try:
#     with open('practice_file.txt', 'x') as file:
#         list_of_strings = ['hi', '\nbye', '\ncya']
#         file.writelines(list_of_strings)
#     with open('practice_file.txt', 'r') as file:
#         print(file.read())
# except FileExistsError:
#     print('File already exists')

# Read and print the content of "practice_file.txt" to the console using the with open() statement.
# with open('practice_file.txt', 'r') as file:
#     print(file.read())
# Append the line "This line is appended using 'with open()'." to the "practice_file.txt."
# with open("practice_file.txt", "a") as file:
#     file.write("\nThis line is appended using 'with open()'.")
# # Read and print the updated content of "practice_file.txt" to the console using the with open() statement.
# with open("practice_file.txt", "r") as file:
#     print(file.read())
# Remove "practice_file.txt," and handle the case where the file doesn't exist.
# try:
#     my_file = 'practice_file.txt'
#     os.remove(my_file)
#     print('file removed')
# except FileNotFoundError:
#     print('file does not exist')

#! Extra:
# Look in to reading other file types, like csv or binary

#! Class
"""
Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.
Hints: Use def methodName(self) to define a method."""

"""Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
Hints: To override a method in super class, we can define a method with the same name in the super class."""

"""Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.
Hints: Use Subclass(Parentclass) to define a child class."""
