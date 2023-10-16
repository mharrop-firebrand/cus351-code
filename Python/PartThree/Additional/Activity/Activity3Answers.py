#
#! If-Else:
# Write an if-else statement to check if a given number is even or odd.
num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Take the age of a person as input. If the age is less than 18, print "You are a minor." Otherwise, print "You are an adult."
age = 26
if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")

# Given a variable x, check if it is positive, negative, or zero using if-else statements.
x = 10
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")


"""
Write a program to ask the user to enter the length of a square and
calculate the area. Print "This is a square of area n".
1 -> 1
2 -> 4
3 -> 9
"""
string_length = input("Enter length of square: ")
length = int(string_length)
area = length * length
print(area)

# or
while True:
    try:
        # Ask the user to enter the length of the square
        length = float(input("Enter the length of the square: "))

        # Check if the length is valid (non-negative)
        if length >= 0:
            break  # Exit the loop if the input is valid
        else:
            print("Please enter a non-negative number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Calculate the area of the square
area = length**2

# Print the result
print(f"This is a square of area {area}")

"""
If:
Write a program to allow the user to enter the length and width of a rectangle and
calculate the area. If the length and width are equal, print "This is a square of
area nn.nn". Otherwise, print "This is a rectangle of area nn.nn".
"""
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
area = round(length * width, 2)
if length == width:
    print("This is a square of area", area)
else:
    print("This is a rectangle of area", area)


"""
If
Write a program to display a menu of options:
Menu
1. Music
2. History
3. Design and Technology
4. Exit
Please enter your choice:
The user then enters a choice and the program prints a message such as "You
chose History". If they choose option 4, the program prints "Goodbye".
"""

print("Menu")
print("1. Music")
print("2. History")
print("3. Design and Technology")
print("4. Exit")
choice = input("\nPlease enter your choice: ")

if choice == "1":
    print("Music is the food of love")
elif choice == "2":
    print("History is bunk")
elif choice == "3":
    print("Not as easy as you think...")
else:
    print("Goodbye")

input("\nPress Enter to exit ")

"""
If
Write a program to input the value of goods purchased in a shop. A discount is subtracted from the value to find the amount owed.
If the value is £200 or more, 10% discount is given.
If the value is between £100 and £199.99, 5% discount is given.
Print the value of goods, discount given and amount owed.
"""
goodsValue = float(input("Enter value of goods purchased: "))

if goodsValue >= 200:
    discount = 0.1 * goodsValue
elif goodsValue >= 100:
    discount = 0.05 * goodsValue
else:
    discount = 0

amountOwed = goodsValue - discount
print(
    "Value of goods:", goodsValue, " Discount:", discount, " Amount owing:", amountOwed
)

"""
If
Question: Write a program that asks the user to input a year. Your program should then determine if the given year is a leap year or not. (A leap year is a year that is divisible by 4)
Hint: You can use the modulo operator % to check for divisibility.
"""
year = int(input("Enter a year: "))

if year % 4 == 0:
    print("Leap year.")
else:
    print("Not a leap year.")

"""
If
Write a program that checks if a given string is a palindrome (reads the same forwards and backwards). Use data structures to implement this.
Example:
Input: "radar"
Output: It's a palindrome!
"""
input_str = "radar"
is_palindrome = input_str == input_str[::-1]
if is_palindrome:
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")

#! For Loop:
# Write a for loop to print the numbers from 1 to 5.

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

for i in range(1, 6):
    print(i)

# Create a list of fruits (e.g., ["apple", "banana", "orange"]). Use a for loop to print each fruit in the list.
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# Write a for loop to calculate the sum of numbers from 1 to 10.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_of_numbers = 0
for num in numbers:
    sum_of_numbers += num
print(sum_of_numbers)

# or
total = 0
for i in range(1, 11):
    total += i
print(total)

"""
For Loop
Question: Create a program that prints the first 5 even numbers. Use a for loop and the range() function to achieve this.
"""
for number in range(2, 12, 2):
    print(number)

"""
For Loop
Using a string, reverse the order of characters in each word of the sentence, while keeping the words themselves in the same order. sentence = "Python is fun"
Example:
Input: "Python is fun"
Output: "nohtyP si nuf"
"""
reversed_words = " ".join(word[::-1] for word in sentence.split())
print(reversed_words)
# or
sentence = "Python is fun"
words = sentence.split()

for i in range(len(words)):
    words[i] = words[i][::-1]

reversed_words = " ".join(words)

print(reversed_words)
# or
sentence = "Python is fun"
words = sentence.split()
reversed_words = []

for word in words:
    reversed_words.append(word[::-1])

result = " ".join(reversed_words)
print(result)

"""
For Loop
Write a program that takes a string as input and counts the number of vowels (a, e, i, o, u) in the string. Display the count for each vowel separately, along with the total vowel count. 
Input: "Hello, how are you?"
Output:
a: 1
e: 2
i: 0
o: 3
u: 1
Total Vowels: 7
"""
input_str = "Hello, how are you?"
vowels = "aeiou"

vowel_counts = {vowel: input_str.lower().count(vowel) for vowel in vowels}
total_vowels = sum(vowel_counts.values())

for vowel, count in vowel_counts.items():
    print(f"{vowel}: {count}")

print(f"Total Vowels: {total_vowels}")

# or
input_str = "Hello, how are you?"
vowels = "aeiou"

vowel_counts = {vowel: 0 for vowel in vowels}

for char in input_str.lower():
    if char in vowels:
        vowel_counts[char] += 1

for vowel, count in vowel_counts.items():
    print(f"{vowel}: {count}")

total_vowels = sum(vowel_counts.values())
print(f"Total Vowels: {total_vowels}")

# or
input_str = "Hello, how are you?"
vowels = "aeiou"

vowel_counts = {vowel: 0 for vowel in vowels}

for char in input_str.lower():
    if char in vowels:
        vowel_counts[char] += 1
        print(f"{char}: {vowel_counts[char]}")

total_vowels = sum(vowel_counts.values())
print(f"Total Vowels: {total_vowels}")

#! While Loop:
# Write a while loop to print the numbers from 1 to 5.
i = 1
while i <= 5:
    print(i)
    i += 1

# Create a variable counter and set it to 5. Use a while loop to count down from 5 to 1.
counter = 5
while counter >= 1:
    print(counter)
    counter -= 1

# Use a while loop to calculate the factorial of a given number.

num = 5
factorial = 1
while num > 0:
    factorial *= num
    num -= 1
print(factorial)

# Create a multiplication table for a given number (e.g., 5) using a while loop. Print the results from 5 times that number down to 1 time that number.
number = 5
i = 10
while i >= 1:
    result = number * i
    print(f"{number} x {i} = {result}")
    i -= 1

# Iteration 1:
#    num = 5
#    factorial *= num  # 1 * 5 = 5
#    num -= 1          # 5 - 1 = 4

# Iteration 2:
#    num = 4
#    factorial *= num  # 5 * 4 = 20
#    num -= 1          # 4 - 1 = 3

# Iteration 3:
#    num = 3
#    factorial *= num  # 20 * 3 = 60
#    num -= 1          # 3 - 1 = 2

# Iteration 4:
#    num = 2
#    factorial *= num  # 60 * 2 = 120
#    num -= 1          # 2 - 1 = 1

# Iteration 5:
#    num = 1
#    factorial *= num  # 120 * 1 = 120
#    num -= 1          # 1 - 1 = 0

# Iteration 6:
#    num = 0
#    The loop exits as num > 0 is no longer true.


"""
While Loop Practice
Question: Write a program that repeatedly asks the user to guess a secret number between 1 and 10. If the guessed number is correct, the program should print "Congratulations!" and exit the loop. If the guessed number is incorrect, the program should print "Try again!" and continue looping.
"""
secret_number = 7
guess = int(input("Guess the secret number: "))
while guess != secret_number:
    print("Try again!")
    guess = int(input("Guess the secret number: "))
print("Congratulations!")

"""
Implement a simple password validation program. Ask the user to enter a password. Keep asking until the user enters a password of at least 8 characters with a combination of letters and numbers.
"""
password = "secret"
attempts = 3

while attempts > 0:
    user_input = input("Enter the password: ")
    if user_input == password:
        print("Login successful!")
        break
    else:
        print(f"Invalid password. {attempts - 1} attempts left.")
        attempts -= 1


# or
while True:
    password = input(
        "Enter a password (at least 8 characters with a combination of letters and numbers): "
    )

    # Check if the password meets the criteria
    if (
        len(password) >= 8
        and any(char.isalpha() for char in password)
        and any(char.isdigit() for char in password)
    ):
        print("Password is valid. Thank you!")
        break
    else:
        print("Invalid password. Please try again.")

"""
Write a program to generate and print the Fibonacci sequence up to a specified limit. Ask the user to enter the limit, and then use a while loop to generate the Fibonacci numbers.
"""
limit = int(input("Enter the limit for the Fibonacci sequence: "))

a = 0
b = 1


print("Fibonacci sequence up to", limit, ":", a, b, end=" ")

while a + b <= limit:
    a, b = b, a + b
    # or
    # temp = a
    # a = b
    # b = temp + b
    print(b, end=" ")

print()


# David L
limit = int(input("please enter limit for Fibonacci sequence: "))
limit_reached = bool(False)

while limit_reached == 0:
    sequence = (n - 1) + (n - 2)
    print("test", sequence)
    if sequence > limit:
        limit_reached = True
    else:
        sequence = (n - 1) + (n - 2)
        print(sequence)

        n += 1

#! Ternary Operator:
# Write a ternary operator to check if a number is positive or negative and print the result accordingly.
num = -5
print("Positive" if num >= 0 else "Negative")

# Given two variables x and y, use a ternary operator to print the smaller of the two values.
x = 10
y = 5
print(x if x < y else y)

# Use a ternary operator to determine whether a given number is even or odd and print the result.
num = 7
print("Even" if num % 2 == 0 else "Odd")

# ! Nested Loops:
# Write a nested loop to print a multiplication table from 1 to 5 (1x1 to 5x10).
for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")

# Create two lists, colors and fruits, and use a nested loop to print all possible combinations of colors and fruits.
colors = ["red", "blue", "green"]
fruits = ["apple", "banana", "orange"]
for color in colors:
    for fruit in fruits:
        print(color, fruit)

# Using a for loop write a nested loop to create a pattern of stars:
# """
# *
# **
# ***
# ****
# *****
# """
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

# ! Loop Control:
# Use a for loop and the continue statement to print all numbers from 1 to 10 except for the number 5.
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
# Use a while loop and the break statement to find the first multiple of 7 between 1 and 50.
num = 1
while num <= 50:
    if num % 7 == 0:
        print(num)
        break
    num += 1

# Use the else clause with a for loop to check if a given number is prime.
num = 17
for i in range(2, num):
    if num % i == 0:
        print(f"{num} is not a prime number.")
        break
else:
    print(f"{num} is a prime number.")
#! If and Loop
"""
Combining If and For Loop
Question: Write a program that prints all the odd numbers between 1 and 20. However, for numbers divisible by 3, print "Divisible by 3" instead of the number itself.
"""

for number in range(1, 21):
    if number % 3 == 0:
        print("Divisible by 3")
    else:
        print(number)

"""
Combining If and While Loop
Question: Create a program that simulates a simple calculator. 
It should repeatedly ask the user for two numbers and an operator (+, -, *, /). 
Then, based on the operator, perform the corresponding calculation and display the result. 
The program should continue running until the user enters "exit".
"""
while True:
    num1 = float(input("Enter the first number: "))
    operator = input("Enter an operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        print("Invalid operator")
        continue

    print("Result:", result)
    exit_choice = input("Enter 'exit' to stop or any key to continue: ")
    if exit_choice == "exit":
        break
