#
#! Functions
"""1) 
Write a program to create a function that takes two arguments, name and age, and print their value."""

"""2) 
Write a function that takes 2 numbers as parameters and returns the highest of the 2 numbers."""

"""3) 
Write a function that takes kilometers as a parameter, converts it into miles and returns the result. (Hint: Google the conversion arthimetic for km to miles)"""

"""4) 
Write a function that takes a list of numbers as input and returns the sum of all the even numbers in the list. (Hint: Modulus)"""

"""5) 
Create a function that takes a string as input and returns the string reversed. (Hint: How did we revese lists? Slicing)"""

"""6) 
Create function that can accept two variables and calculate addition and division. Also, it must return both addition and division in a single return call."""

"""7) 
Create a function that checks to see if a given string is a palindrome or not. (Hint: The same backwards as forwards)"""

""" 8)
Create a function that will show information about an employee. It should accept the employee's name and salary and display both.
If the salary is missing then assign default value 9000 to salary"""

#! Advance

""" 9)
Implement a Temperature Converter
Write a function celsius_to_fahrenheit that converts Celsius to Fahrenheit. Include exception handling to ensure the input is a valid number.
Example: celsius_to_fahrenheit(25) should return approximately 77"""

""" 10)
Build a List Reverser Function
Develop a function reverse_list that takes a list as input and returns its reverse. Include exception handling to check if the input is a valid list.
Example: reverse_list([1, 2, 3, 4]) should return [4, 3, 2, 1]."""

""" 11)
Create a Grade Calculator
Write a function calculate_grade that takes a student's score as input and returns their grade (A, B, C, D, or F). Include exception handling to ensure the input is within a valid score range."""

""" 12)
Function that takes a LIST of numbers as input from a user and returns a sum of them. 
(Hints: look at append(), loop over input, could take first a number of elements then use that number of elements as the range for the loop?)"""

""" 13)
Write a function that calculates how many days it is until Christmas and returns the number of sleeps left until the big day. 
(hint, look at date time)"""

#! Built-in Modules:
# Import the random module and generate a random number between 1 and 10.
import random

random_number = random.randint(1, 10)
print(random_number)

# Import the datetime module and print the current date and time.
import datetime

current_datetime = datetime.datetime.now()
print(current_datetime)

# Import the math module and calculate the square root of a given number.
import math

number = 25
square_root = math.sqrt(number)
print(square_root)

#! Custom Modules:
""" 1)
Create a custom module named calculator that contains functions for basic arithmetic operations (addition, subtraction, multiplication, division)."""

"""
Import the modules in another file and call the functions:
Add 5 and 10.
Subtract 7 from 15.
Multiply 3 and 6.
Divide 20 by 4."""

""" 2)
Create a custom module named shapes that contains functions for calculating the area of different shapes (circle, rectangle, triangle). (Hint: use math module for pi)"""

"""Import the modules in another file and call the functions:
Calculate the area of:
A circle with a given radius
A rectangle with given length and width
A triangle with given base and height."""


#! Exception handling:
"""1) 
Use your highest number function to handle a type error incase strings were passed in to the function call

def find_highest_number(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


# Function Call
print("Highest number:", find_highest_number(10, 5))
print("Highest number:", find_highest_number(10, 'Hi'))
"""

"""2) 
Use your addition and division function to add exception handling for a Zero division error (additional add user input and value error and type error.)

def calculate_addition_and_division(a, b):
    addition = a + b
    division = a / b
    return addition, division


# Function Call
result_add, result_sub = calculate_addition_and_division(10, 2)
print("Addition:", result_add)
print("Division:", result_sub)
"""

"""3)
Create a dictionary and ask the user to enter a key.
Use a try-except block to handle a KeyError if the key is not found.
If the key is found, display its corresponding value; if not, inform the user."""
