#
#! Functions
"""1) 
Write a program to create a function that takes two arguments, name and age, and print their value."""


def print_name_and_age(name, age):
    print("Name:", name)
    print("Age:", age)


# Function Call
print_name_and_age("John", 25)

"""2) 
Write a function that takes 2 numbers as parameters and returns the highest of the 2 numbers."""


def find_highest_number_alternative(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


# Function Call
result_alt = find_highest_number_alternative(10, 5)
print("Highest number (alternative):", result_alt)


# or
def find_highest_number(num1, num2):
    return max(num1, num2)


# Function Call
result = find_highest_number(10, 5)
print("Highest number:", result)

"""3) 
Write a function that takes kilometers as a parameter, converts it into miles and returns the result. (Hint: Google the conversion arithmetic for km to miles)"""

# mile = km * 0.62137


def convert_km_to_miles(km):
    mile = km * 0.62137
    return mile


print(f"10km to miles is: ", convert_km_to_miles(10))

print(f"21km for half marathon in miles is: ", convert_km_to_miles(21))

print(f"42km for full marathon in miles is: ", convert_km_to_miles(42))

"""4) 
Write a function that takes a list of numbers as input and returns the sum of all the even numbers in the list. (Hint: Modulus)"""


def sum_of_even_nums(ls):
    total = 0
    for i in ls:
        if i % 2 == 0:
            total += i
    return total


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sum_of_even_nums(list1))

print(sum_of_even_nums([42, 43, 44, 109, 108, 202]))

"""5) 
Create a function that takes a string as input and returns the string reversed. (Hint: How did we revese lists? Slicing)"""

# string1 = 'test'

# print(string1[::-1])


def reverse_string(x):
    return x[::-1]


print(reverse_string("The meaning of life is 42"))
print(reverse_string("firebrand"))


# or
def reverse_string2():
    string_input = input("Enter a string: ")
    reversed = string_input[::-1]
    rereversed = reversed[::-1]
    return reversed, rereversed


print(reverse_string2())

"""6) 
Create function that can accept two variables and calculate addition and division. Also, it must return both addition and division in a single return call."""
# x = 5
# y = 1
# add = x + y
# # print(add)

# x = 8
# y = 2
# division = x / y
# # print(division)


def add_divide(num1, num2):
    add, division = num1 + num2, num1 / num2
    num1, num2, num3 = 0, 0, 0
    num1 = num2 = num2 = 0
    return add, division


print(add_divide(8, 2))
print(add_divide(100, 6))
print(add_divide(42, 3))


"""7) 
Create a function that checks to see if a given string is a palindrome or not. (Hint: The same backwards as forwards)"""


def palindome(string2):
    if string2.lower() == string2[::-1].lower():
        print(string2, "is a palindome (same backwards as forwards)")
    else:
        print(string2, "not a palindome")


palindome("hannaH")


def palindrome2(input_string):
    return input_string == input_string[::-1]


print(palindrome("hannah"))

""" 8)
Create a function that will show information about an employee. It should accept the employee's name and salary and display both.
If the salary is missing then assign default value 9000 to salary"""


def employee_information(name, salary=9000):
    return name, salary


print(employee_information("Maddy", 9000))
print(employee_information("Tom", 10000))
print(employee_information("Fred"))


#! Advance

""" 9)
Implement a Temperature Converter
Write a function celsius_to_fahrenheit that converts Celsius to Fahrenheit. Include exception handling to ensure the input is a valid number.
Example: celsius_to_fahrenheit(25) should return approximately 77

Parameter: int(celcium)
Do: Convert celcium to farenheit:
    (celcium * 1.8) + 32 = farenheit
Return: number(farenheit)
"""
import math


def convert_temp(celcius):
    farenheit = math.floor((celcius * 1.8) + 32)
    return farenheit


print(f"28 degrees C in farenheit is {convert_temp(28)}")
print(f"145 degrees C in farenheit is {convert_temp(145)}")

""" 10)
Build a List Reverser Function
Develop a function reverse_list that takes a list as input and returns its reverse.
Example: reverse_list([1, 2, 3, 4]) should return [4, 3, 2, 1]."""

list10 = [1, 2, 3, 4]

# print(list10[::-1])


def reverse_list2(my_list):
    return my_list[::-1]


input_l = input("Enter a list: ")
list_input = []

for item in input_l.split():
    list_input.append(int(item))

print(reverse_list2(list_input))

print(reverse_list2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


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

# Import the datetime module and print the current date and time.

# Import the math module and calculate the square root of a given number.

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
"""


def find_highest_number(num1, num2):
    try:
        if num1 > num2:
            return num1
        else:
            return num2
    except TypeError:
        return "Did not enter a number: TypeError"


# Function Call
print("Highest number:", find_highest_number(10, 5))
print("Highest number:", find_highest_number(10, "Hi"))


"""2) 
Use your addition and division function to add exception handling for a Zero division error (additional add user input and value error and type error.)
"""


def calculate_addition_and_division():
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter a number: "))
        try:
            division = a / b
        except ZeroDivisionError:
            return "ZERODIVISIONERROR. Cannot divide by zero"
    except ValueError:
        return "ValueError: Not an integer"
    else:
        addition = a + b
        return addition, division


# Function Call
print(calculate_addition_and_division())


"""3)
Create a dictionary and ask the user to enter a key.
Use a try-except block to handle a KeyError if the key is not found.
If the key is found, display its corresponding value; if not, inform the user."""


""" 4) Implement a recursive function to check if a given string is a palindrome.

Ensure your function handles the base case appropriately (e.g., an empty string or a string with one character is considered a palindrome).
Test your function with different strings to verify its correctness.
Consider using a suitable base case to terminate the recursion.
Think about how the recursive calls will lead to the final result.
"""
