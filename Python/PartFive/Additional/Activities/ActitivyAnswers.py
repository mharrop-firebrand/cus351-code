#
#! NOT WITH OPEN
# Create a text file named "my_file.txt" and add the following content to it:
# "Hello, this is the initial content of the file."
# "This is the second line in the file."

# Read the entire content of the file using the read() method and print it to the console.

# Read the file line by line using the readlines() method and print each line (without newline characters) to the console.

# Read the file using the readline() method and print the first and second lines to the console.

# Append a new line to the file with the content: "This line is appended to the file."

# Read the updated content of the file using the read() method and print it to the console.

# Overwrite the entire file with the content: "This content overwrites the entire file."

# Read the overwritten content of the file using the read() method and print it to the console.

# Remove the file "my_file.txt," and make sure to handle the case where the file doesn't exist.

# Verify that the file has been removed (or if it didn't exist, print a message indicating that).


#! With Open

# Open a new text file named "practice_file.txt" using the with open() statement.
# Write some text into the file.

# Read and print the content of "practice_file.txt" to the console using the with open() statement.

# Append the line "This line is appended using 'with open()'." to the "practice_file.txt."

# Read and print the updated content of "practice_file.txt" to the console using the with open() statement.

# Remove "practice_file.txt," and handle the case where the file doesn't exist.


#! Extra:
# Look in to reading other file types, like csv or binary

"""
Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.
Hints: Use def methodName(self) to define a method."""


class Rectangle(object):
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.length * self.width


Rectangle = Rectangle(2, 10)
print(Rectangle.area())

"""Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
Hints: To override a method in super class, we can define a method with the same name in the super class."""


class Rectangle(object):
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.length * self.width


Rectangle = Rectangle(2, 10)
print(Rectangle.area())
"""Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.
Hints: Use Subclass(Parentclass) to define a child class."""


class Person(object):
    def getGender(self):
        return "Unknown"


class Male(Person):
    def getGender(self):
        return "Male"


class Female(Person):
    def getGender(self):
        return "Female"


Male = Male()
Female = Female()
print(Male.getGender())
print(Female.getGender())
