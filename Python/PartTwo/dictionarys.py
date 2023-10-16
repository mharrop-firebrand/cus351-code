#
# ! Dictionaries
"""
A dictionary is a mutable data structure that stores mappings of unique keys to values
A key in a dictionary has to be an immutable data type e.g. int, tuple or string
We define or create dictionary using only {} items separated by commas , or via the dict() function 
key: value
"""

# Empty dictionary
empty_dictionary = {}
print(type(empty_dictionary))

empty_dict = dict()

# Dictionary with keys as strings
ages = {"Maddy": 46, "Bob": 13, "John": 66}
print(ages)

# As integers
scores = {101: "Maths", 103: "English", 104: "Science", 101: "Spanish"}
print(scores)

# mixed keys
mixed_dict = {
    1: "One",  # key int: string value
    "Two": 2,  # key string: int value
    (3, 4): "Three-Four",  # key tuple: string value
    "Five-Six-Seven-Eight": [5, 7, "Seven", "Eight"],  # key string: list value
}
# print(mixed_dict)

#! Dictionary Methods
# zip() function
names = ["Maddy", "Diane", "Samuel", "Syd"]
happiness_level = [100, 99, 75, 88]
happy_dict = dict(zip(names, happiness_level))
print(happy_dict)
# {'Maddy': 100, 'Diane': 99, 'Samuel': 75, 'Syd': 88}

# To access keys within a dictionary, we can use dict.keys() function
cars = {
    "Vaxhaul": "Astra",
    "Ford": "Focus",
    "Lambourgini": "Aventador",
    "Skoda": "Citigo",
}
print(cars.keys())

# dict.values() To access a dictionary values
print(cars.values())

# dict.items() returns items in a list format of (key, value) tuple pairs
print(cars.items())

# Using pop()
removed_item = cars.pop("Skoda")
print(f"Removed value for 'Skoda': {removed_item}.")
print("Removed value for 'Skoda':", removed_item)
print("Removed value for 'Skoda': " + removed_item)
print(f"Updated dictionary after the pop() {cars}")

cars = {
    "Vaxhaul": "Astra",
    "Ford": "Focus",
    "Lambourgini": "Aventador",
    "Skoda": "Citigo",
}
print(cars)
# Using update()
new_cars = {"VW": "Golf", "Aston Martin": "Vanquish", "Nissan": "Cube"}
cars.update(new_cars)
print(cars)

#! Compound data structure
periodic_dict = {
    "Hydrogen": {"Number": 1, "Weight": 1.0000007, "Symbol": "H"},
    "Helium": {"Number": 2, "Weight": 4.0000078, "Symbol": "He"},
}
print(periodic_dict)

# Get keys of dictionary helium
print(periodic_dict.get("Helium").keys())  # 'Number', 'Weight', 'Symbol'
# Get value of number inside helium
print(periodic_dict.get("Helium").get("Number"))  # 2
# get value of weight key inside hydrogen
print(periodic_dict.get("Hydrogen").get("Weight"))  # 1.0000007
