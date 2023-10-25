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
class Animal:
    pass


animal1 = Animal()
print(animal1)

# # Instance variables
animal1.name = "Bean"
animal1.animal_type = "Dog"
animal1.age = 1
print(animal1.name)
print(animal1.animal_type)
print(animal1.age)


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
        # animal1.name this the the same as line below
        self.name = name
        self.animal_type = animal_type
        self.age = age

# Objects - Instance of our class
animal1 = Animal1('Bean', 'Dog', 1)

print(f'{animal1.name} is a {animal1.animal_type} and is {animal1.age} year(s) old')

# animal2 = Animal1('Pancake', 'Dog', 4)
# print(f'{animal2.name} is a {animal2.animal_type} and is {animal2.age} months(s) old')


#! Class methods
# This is a lot of typing for each animal we want to display.
# Instead lets create a method in our class that displays the informtion for us
# class Animal2:
# #     # ? Class Variables
#     # Bound to Class
#     # Declared inside the class, but outside of any method
#     # Shared by all objects of a class
#     # A class variable can be accesses and modified using the class name - class_name.attribute_name
#     animal_class = "Unknown"

#     # Constructor
#     def __init__(self, name, animal_type, age):
#         # Instance variables
#         self.name = name
#         self.animal_type = animal_type
#         self.age = age

#     # Class Method
#     def animal_info(self):
#         return f"{self.name} is a {self.animal_type} and is {self.age} years(s) old"

#     # Behaviour
#     def animal_noise(self):
#         return "Some Animal Noise"

#     # End of Class Body


# # # Instance of my class - Object
# animal1 = Animal2("Monty", "Dog", 6)

# print(animal1.animal_info())
# print(animal1.animal_noise())

# print(animal1.animal_class)
# # Changing the value of the class variables will change all instances of Animal2's animal_class
# Animal2.animal_class = "Mammal"
# print(animal1.animal_class)


#! Class without a constructor
# A class without a custom constructor will have a default constructor provided by Python.
# The purpose of this default constructor is to initialize the object's attributes.
# The default constructor is part of your source code and is present in the class's definition within your .py file.
# It doesn't contain any additional code unless you add custom initialization.
# class Car:
#     # This class has no constructor
#     def car_method(self):
#         return "Beep"


# car1 = Car()
# # print(car1.car_method())


#! Non-parameterized constructor
# A non-parameterized constructor is where no parameters are defined or needed
# Such a constructor type is used when objects are initialized with default values
# class Student:
#     # Non-parameterized constuctor
#     def __init__(self):
#         self.name = "John"

#     def introduce(self):
#         return f"Hi i am {self.name}"


# student1 = Student()

# print(student1.name)
# print(student1.introduce())


#! Parameterized constructor
# For a more dynamic functionality of creating objects and initializing instance variables with different values, a parameterized constructor is used
# The first parameter is still 'self' but you can have additional parameters and it can have any number of arguments
# We can supply different values via arguments at the time of object creation

# class Car:
#     # A parmertize constructor
#     def __init__(self, make, model, door_num, colour, year, seat_num):
#         # Initilized instance variables
#         self.make = make
#         self.model = model
#         self.door_num = door_num
#         self.colour = colour
#         self.year = year
#         self.seat_num = seat_num

#     # Method to show car information:
#     def car_info(self):
#         return f"The car is a {self.make} with the model {self.model} from the year {self.year}. It has {self.door_num} doors, it has {self.seat_num} seats and it is a {self.colour} colour."

#     def accelerate(self):
#         if self.make == "BMW":
#             print("The BWM accelerates at a top speed of 120mph")
#         elif self.make == "Ford":
#             print("The Ford accerlates to a top speed of 90mph")
#         else:
#             print("Speed information is not available for this car make.")


# my_car = Car("BMW", "1 Series", 5, "White", "2015", 5)
# print(my_car.car_info())
# my_car.accelerate()

# car2 = Car("Ford", "Focus", 5, "Pink", "2012", 5)
# print(car2.car_info())
# car2.accelerate()

# car3 = Car("Peugoet", "Box", 3, "Black", "2017", 5)
# print(car3.car_info())
# car3.accelerate()


#! Inheritience
# Inheritance is the process of sharing the properties of a parent class to a child class
# OR
# It is the capability of one class to derive or inherit the properties of another class
# Parent class Animal
class Animal:
    def __init__(self, num_of_legs, domesticated, diet, num_of_teeth, animal_class):
        self.num_of_legs = num_of_legs
        self.domesticated = domesticated
        self.diet = diet
        self.num_of_teeth = num_of_teeth
        self.animal_class = animal_class

    def animal_info(self):
        return (
            f"This animal is part of the {self.animal_class} animal class. \n"
            f"It is {self.domesticated} that this animal is domesticated. \n"
            f"It uses is {self.num_of_teeth} teeth to eat its {self.diet} diet and walks (or not) on its {self.num_of_legs} number of legs "
        )


# Child class: Dog from Animal
class Dog(Animal):
    def __init__(self, breed, hair_type, size, colour, drools):
        self.breed = breed
        self.hair_type = hair_type
        self.size = size
        self.colour = colour
        self.drools = drools

    def dog_info(self):
        return (
            f"The dog is a {self.breed}.\n"
            f"It has {self.hair_type} hair. It is a {self.size} dog. \n"
            f"Is it the {self.colour} colour and it is {self.drools} that this animal drools"
        )

    def noise(self):
        return "BARK BARK BARK"


animal1 = Animal(
    num_of_legs=4,
    domesticated=True,
    diet="Canivore",
    num_of_teeth=42,
    animal_class="Mammal",
)
print(animal1.animal_info())

dog1 = Dog(
    breed="Dachushund",
    hair_type="Smooth",
    size="Small",
    colour="Brown and Tan",
    drools=False,
)
print(dog1.dog_info())
print(dog1.noise())

# Child class: Cat from Animal
