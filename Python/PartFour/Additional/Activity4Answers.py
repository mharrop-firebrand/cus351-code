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
Write a function that takes kilometers as a parameter, converts it into miles and returns the result. (Hint: Google the conversion arthimetic for km to miles)"""


def convert_km_to_miles(kilometers):
    miles = kilometers * 0.621371
    return miles


# Function Call
result = convert_km_to_miles(10)
print("Miles:", result)


"""4) 
Write a function that takes a list of numbers as input and returns the sum of all the even numbers in the list. (Hint: Modulus)"""


def sum_of_even_numbers(numbers):
    even_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
    return even_sum


# Function Call
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_of_even_numbers(numbers_list)
print("Sum of even numbers:", result)


# Or
def sum_of_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return sum(even_numbers)


# Function Call
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_of_even_numbers(numbers_list)
print("Sum of even numbers:", result)


"""5) 
Create a function that takes a string as input and returns the string reversed. (Hint: How did we revese lists? Slicing)"""


def reverse_string(input_string):
    return input_string[::-1]


# Function Call
result = reverse_string("hello")
print("Reversed string:", result)


"""6) 
Create function that can accept two variables and calculate addition and division. Also, it must return both addition and division in a single return call."""


def calculate_addition_and_division(a, b):
    addition = a + b
    division = a / b
    return addition, division


# Function Call
result_add, result_sub = calculate_addition_and_division(10, 2)
print("Addition:", result_add)
print("Division:", result_sub)


"""7) 
Create a function that checks to see if a given string is a palindrome or not. (Hint: The same backwards as forwards)"""


def is_palindrome(input_string):
    return input_string == input_string[::-1]


# Function Call
result = is_palindrome("level")
print("Is palindrome:", result)

""" 8)
Create a function that will show information about an employee. It should accept the employee's name and salary and display both.
If the salary is missing then assign default value 9000 to salary"""


def show_employee(name, salary=9000):
    print("Employee Name:", name)
    print("Employee Salary:", salary)


# Function Call
show_employee("John", 12000)
# If salary is not provided, the default value (9000) will be used.
show_employee("Alice")

#! Advance

""" 9)
Implement a Temperature Converter
Write a function celsius_to_fahrenheit that converts Celsius to Fahrenheit. Include exception handling to ensure the input is a valid number.
Example: celsius_to_fahrenheit(25) should return approximately 77"""


def celsius_to_fahrenheit(celsius):
    try:
        # Attempt to convert input to float
        celsius = float(celsius)
        # Conversion formula: (Celsius * 9/5) + 32
        fahrenheit = (celsius * 9 / 5) + 32
        return fahrenheit
    except ValueError:
        print("Invalid input. Please enter a valid number.")


# Function Call
result = celsius_to_fahrenheit(25)
print("Fahrenheit:", result)

""" 10)
Build a List Reverser Function
Develop a function reverse_list that takes a list as input and returns its reverse. Include exception handling to check if the input is a valid list.
Example: reverse_list([1, 2, 3, 4]) should return [4, 3, 2, 1]."""


def reverse_list(input_list):
    reversed_list = list(reversed(input_list))
    return reversed_list


# Function Call
result = reverse_list([1, 2, 3, 4])
print("Reversed list:", result)

""" 11)
Create a Grade Calculator
Write a function calculate_grade that takes a student's score as input and returns their grade (A, B, C, D, or F). Include exception handling to ensure the input is within a valid score range."""


def calculate_grade(score):
    try:
        score = float(score)
        if 0 <= score <= 100:
            if score >= 90:
                return "A"
            elif score >= 80:
                return "B"
            elif score >= 70:
                return "C"
            elif score >= 60:
                return "D"
            else:
                return "F"
        else:
            print("Invalid input. Please enter a score between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


# Function Call
result = calculate_grade(85)
print("Grade:", result)

""" 12)
Function that takes a LIST of numbers as input from a user and returns a sum of them. 
(Hints: look at append(), loop over input, could take first a number of elements then use that number of elements as the range for the loop?)"""


def calculate_sum_from_input():
    try:
        # Get the number of elements in the list
        num_elements = int(input("Enter the number of elements: "))

        # Get each number from the user and calculate the sum
        numbers = []
        for i in range(num_elements):
            num = float(input(f"Enter number {i + 1}: "))
            numbers.append(num)

        # Calculate the sum of the numbers
        sum_of_numbers = sum(numbers)

        return sum_of_numbers

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return None


# Function Call
result = calculate_sum_from_input()

if result is not None:
    print("Sum of the numbers:", result)

""" 13)
Write a function that calculates how many days it is until Christmas and returns the number of sleeps left until the big day. 
(hint, look at date time)"""
from datetime import datetime, timedelta


def days_until_christmas():
    today = datetime.now()
    christmas = datetime(today.year, 12, 25)

    if today > christmas:
        christmas = datetime(today.year + 1, 12, 25)

    days_left = (christmas - today).days
    return days_left


# Function Call
result = days_until_christmas()
print("Days until Christmas:", result)

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


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


"""
Import the modules in another file and call the functions:
Add 5 and 10.
Subtract 7 from 15.
Multiply 3 and 6.
Divide 20 by 4."""
import calculator

result_add = calculator.add(5, 10)
result_subtract = calculator.subtract(15, 7)

result_multiply = calculator.multiply(3, 6)

result_divide = calculator.divide(20, 4)

print(result_add)
print(result_subtract)
print(result_multiply)
print(result_divide)

""" 2)
Create a custom module named shapes that contains functions for calculating the area of different shapes (circle, rectangle, triangle). (Hint: use math module for pi) """
import math


def circle_area(radius):
    return math.pi * radius**2


def rectangle_area(length, width):
    return length * width


def triangle_area(base, height):
    return 0.5 * base * height


"""Import the modules in another file and call the functions:
Calculate the area of:
A circle with a given radius
A rectangle with given length and width
A triangle with given base and height."""
import shapes

circle_radius = 5
circle_area = shapes.circle_area(circle_radius)
print(circle_area)

rectangle_length = 10
rectangle_width = 4
rectangle_area = shapes.rectangle_area(rectangle_length, rectangle_width)
print(rectangle_area)

triangle_base = 6
triangle_height = 8
triangle_area = shapes.triangle_area(triangle_base, triangle_height)
print(triangle_area)


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


# Answer:
def find_highest_number(num1, num2):
    try:
        if num1 > num2:
            return num1
        else:
            return num2
    except TypeError:
        return "Error: Invalid types. Both arguments should be numeric."


# Function Call
print("Highest number:", find_highest_number(10, 5))
print("Highest number:", find_highest_number(10, "Hi"))


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


# Answer:
def calculate_addition_and_division():
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))

        addition = a + b
        division = a / b

        return addition, division

    except ZeroDivisionError:
        print(
            "Error: Cannot divide by zero. Please enter a non-zero value for the second number."
        )

    except ValueError:
        print("Error: Please enter valid integer values for both numbers.")

    except TypeError:
        print(
            "Error: Unexpected type encountered. Please ensure both numbers are integers."
        )


# Function Call
result = calculate_addition_and_division()
if result:
    print("Addition:", result[0])
    print("Division:", result[1])

# Answer:
"""3)
Create a dictionary and ask the user to enter a key.
Use a try-except block to handle a KeyError if the key is not found.
If the key is found, display its corresponding value; if not, inform the user."""

my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}

try:
    user_key = input("Enter a key to access from the dictionary: ")
    value = my_dict[user_key]
    print(f"The value for {user_key} is: {value}")
except KeyError:
    print(f"Error: Key '{user_key}' not found in the dictionary.")
except Exception as e:
    print("An unexpected error occurred:", e)

''' Implement a recursive function to check if a given string is a palindrome.

Ensure your function handles the base case appropriately (e.g., an empty string or a string with one character is considered a palindrome).
Test your function with different strings to verify its correctness.
Consider using a suitable base case to terminate the recursion.
Think about how the recursive calls will lead to the final result.
'''

def is_palindrome(s):
    # Base case: If the string has 0 or 1 characters, it's a palindrome
    if len(s) <= 1:
        return True
    
    # Recursive case: Check if the first and last characters are the same
    if s[0] == s[-1]:
        # Recur on the substring without the first and last characters
        return is_palindrome(s[1:-1])
    else:
        return False

# Example Usage
word1 = "level"
word2 = "python"

result1 = is_palindrome(word1)
result2 = is_palindrome(word2)

print(f"Is '{word1}' a palindrome? {result1}")
print(f"Is '{word2}' a palindrome? {result2}")
