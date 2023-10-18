# Square of a Number:
# Write a lambda function to calculate the square of a given number.
square = lambda x: x**2
print(square(5))  # Output: 25

# Addition of Two Numbers:
# Create a lambda function to add two numbers.
add = lambda x, y: x + y
print(add(3, 7))  # Output: 10

# Check if a Number is Even:
# Use a lambda function to check if a number is even.
is_even = lambda x: x % 2 == 0
print(is_even(6))  # Output: True

# Reverse a String:
# Write a lambda function to reverse a given string.
reverse_string = lambda s: s[::-1]
print(reverse_string("hello"))  # Output: olleh

# Concatenate Strings:
# Use a lambda function to concatenate two strings.
concatenate = lambda s1, s2: s1 + s2
print(concatenate("Hello", "World"))  # Output: HelloWorld

# Find the Maximum of Two Numbers:
# Create a lambda function to find the maximum of two numbers.
max_of_two = lambda x, y: x if x > y else y
print(max_of_two(8, 4))  # Output: 8

# Filter Even Numbers from a List:
# Use a lambda function with filter to filter even numbers from a list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# Map Square to Each Element of a List:
# Use a lambda function with map to square each element of a list.
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
