import os
import random

# ! OS Module
# Get Current working directory
# current_directory = os.getcwd()
# print('My Current Working Directory is:', current_directory)

# Make new directory
# os.mkdir('new_folder')

# Remove the current working directory
# os.rmdir('new_folder')

# List directorys
# print(os.listdir())


#! Math Module
# Square Root

# Euler's number

# Pi value

# Floor the given number

# Ceiling the given number

# Exponentiation

#! Random
# Random (0.0-1.0)
print('Random Float:', random.random())
# Random Int
print('Random Number between 10 and 28:', random.randint(10, 28))
# Random Choice
cake = ['Chocolate', 'Viccy Sponge', 'Carrot', 'Lemon Drizzle']
print('Random Cake:', random.choice(cake))
# Random Range
print(random.randrange(0, 99, 2))

#! Datetime
# Datetime now

# Format to an object
import custom_module
#! Custom Module
# Use functions from the custom module
print(custom_module.greet('Maddy'))

print(custom_module.add(5, 10))