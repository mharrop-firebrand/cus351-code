import os
import random
import custom_module
import math
from datetime import datetime, timedelta

# ! OS Module
# Get Current working directory
current_directory = os.getcwd()
print("My Current Working Directory is:", current_directory)

# Make new directory
os.mkdir("new_folder")

# Remove the current working directory
os.rmdir("new_folder")

# List directorys
print(os.listdir())


#! Math Module
# Square Root
num = int(input("Please enter a number to find the square root: "))
square_root = math.sqrt(num)
print(f"The square root of {num} is: {square_root}")

# Euler's number
print("Eulers Number: ", math.e)

# Pi value
print("Pi Number: ", math.pi)

# Floor the given number
x = 5.7
print(math.floor(x))

# Ceiling the given number
x = 5.7
print(math.ceil(x))

# Exponentiation
base = 2
exponent = 3
result = math.pow(base, exponent)
print(f"{base} to the power of {exponent} is {result}")

#! Random
# Random (0.0-1.0)
print("Random Float:", random.random())
# Random Int
print("Random Number between 10 and 28:", random.randint(10, 28))
# Random Choice
cake = ["Chocolate", "Viccy Sponge", "Carrot", "Lemon Drizzle"]
print("Random Cake:", random.choice(cake))
# Random Range
print(random.randrange(0, 99, 2))

#! Datetime
# Datetime now
print("The current date and time:", datetime.now())

# Format to an object
date_string = "28 May 2023"
print(type(date_string))

date_object = datetime.strptime(date_string, "%d %b %Y")
print(type(date_object))
print(date_object)

format_date = date_object.strftime("%d %b %Y")
print(type(format_date))
print(format_date)

# Difference between two dates:

# Last christmas
date1 = datetime(2022, 12, 25)
# Fomatted to print 12/25/22
format_date1 = date1.strftime("%x")

# Time now
date2 = datetime.now()
# Fomatted to print 10/19/23
format_date2 = date2.strftime("%x")

# Diffrence between last christmas and now
difference = (date2 - date1).days

# Next chistmas
date3 = datetime(2023, 12, 25)

# difference between now and next christmas
difference2 = (date3 - date2).days

print("Days since last christmas", difference)
print(
    f'Days since "{format_date1}" to now: "{format_date2}" is: {difference}\nDays until next chirstmas is {difference2}'
)


#! Custom Module
# Use functions from the custom module
print(custom_module.greet("Maddy"))

print(custom_module.add(5, 10))
