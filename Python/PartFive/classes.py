# class ClassName:
#     # Class attributes and methods go here

#     def __init__(self, arg1, arg2):
#         pass
#         # Constructor method (optional)
#         # This method is called when an instance of the class is created.
#         # You can initialize instance variables here.

#     def method_name(self, arg1, arg2):
#         pass
#         # Method definition
#         # Methods are functions defined within the class and are associated with class instances.
#         # The 'self' parameter refers to the instance of the class and is passed implicitly.
#         # You can perform operations and interact with instance variables here.

#     def another_method(self, arg1, arg2):
#         pass
#         # Another method definition


# obj = ClassName(arg1_value, arg2_value, ...)


#! Creating a class
# Class: Blueprint for each instance
# class Animal:
#     pass


# # Objects - Instances of a class
# animal1 = Animal()
# animal2 = Animal()
# # print(animal1)
# # print(animal2)

# # Instance variables
# animal1.name = "Bean"
# animal1.animal_type = "Dog"
# animal1.age = 1
# print(animal1.name)
# print(animal1.animal_type)
# print(animal1.age)

# # Instance variables
# animal2.name = "Fen"
# animal2.animal_type = "Cat"
# animal2.age = 1
# print(animal2.name)
# print(animal2.animal_type)
# print(animal2.age)

#! Class atributes
# It's a lot of code and prone to mistakes, Not much benefit of OOP doing it manually
# What if we get all of this information on the animal when it is created rather than manually.

# ? Instance variables
# Bound to Object
# Declared inside the__init__ method
# Not shared by objects. Every object has its own copy
# An instance variable can be accessed and modified using the dot notation – instance_name.attribute_name
class Animal1():
    # __init__ method  - Constructor
    # Initialize information about our object when it is created
    def __init__(self, name, animal_type, age):
        # Setting the instance variables
      # animal2.name = 'Maddy'
        self.name = name
        self.animal_type = animal_type
        self.age = age

# Objects - Instance of our class
animal1 = Animal1('Bean', 'Dog', 1)
print(f'{animal1.name} is a {animal1.animal_type} and is {animal1.age} year(s) old')

animal2 = Animal1('Pancake', 'Dog', 4)
print(f'{animal2.name} is a {animal2.animal_type} and is {animal2.age} months(s) old')


#! Class methods
# This is a lot of typing for each animal we want to display.
# Instead lets create a method in our class that displays the informtion for us


# ? Class Variables
# Bound to Class
# Declared inside the class, but outside of any method
# Shared by all objects of a class
# A class variable can be accesses and modified using the class name - class_name.attribute_name


#! Class without a constructor
# A class without a custom constructor will have a default constructor provided by Python.
# The purpose of this default constructor is to initialize the object's attributes.
# The default constructor is part of your source code and is present in the class's definition within your .py file.
# It doesn't contain any additional code unless you add custom initialization.


#! Non-parameterized constructor
# A non-parameterized constructor is where no parameters are defined or needed
# Such a constructor type is used when objects are initialized with default values


#! Parameterized constructor
# For a more dynamic functionality of creating objects and initializing instance variables with different values, a parameterized constructor is used
# The first parameter is still 'self' but you can have additional parameters and it can have any number of arguments
# We can supply different values via arguments at the time of object creation


#! Inheritience
# Inheritance is the process of sharing the properties of a parent class to a child class
# OR
# It is the capability of one class to derive or inherit the properties of another class
