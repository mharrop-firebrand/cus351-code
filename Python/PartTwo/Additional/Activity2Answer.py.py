# Can you create a list of your favorite foods in Python?
favorite_foods = ["Pizza", "Pasta", "Ice Cream", "Chocolate"]

# How would you print the list and its length?
print(favorite_foods)
print("Number of favorite foods:", len(favorite_foods))

# If you have a list of numbers from 1 to 10, how can you print the first three and last three numbers using list slicing?
numbers = list(range(1, 11))
print("First three numbers:", numbers[:3])
print("Last three numbers:", numbers[-3:])

# Can you create a matrix (a nested list) representing a 3x3 grid of numbers in Python?
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Can you add a new food to your list and then remove one of the existing foods?
favorite_foods.append("Sushi")  # Add a new food
favorite_foods.remove("Pasta")  # Remove an existing food

# How would you print the updated list? W3 schools for list methods
print("Updated favorite foods:", favorite_foods)


#! Lists:
# Consider the following lists
# a = [1, 5, 8]
# b = [2, 6, 9, 10]
# c = [100, 200]

# What is the output of the following statements?
# 1. print(max([len(a), len(b), len(c)]))
# 2. print(min([len(a), len(b), len(c)]))

# Choices:
# 1. 200, 3
# 2. 300, 14
# 3. 4, 2 #ANSWER
# 4. 2, 4

# len(a) = 3, len(b) = 4, len(c) = 2
# max([3, 4, 2]) gives 4
# min([3, 4, 2]) gives 2

# 2) What is the output of the following code?
# names = ["Carol", "Albert", "Ben", "Donna"]
# print(" & ".join(sorted(names)))

# Choices:
#         1. Albert, Ben, Carol, Donna #ANSWER
#         2. Carol & Albert & Ben & Donna
#         3. & Albert & Ben & Carol & Donna &
#         4. Albert & Ben & Carol & Donna


# 3) What is the output of the following code?

# names = ["Carol", "Albert", "Ben", "Donna"]
# names.append("Eugenia")
# print(sorted(names))

# Choices:
#          1. Albert & Ben & Carol & Donna & Eugenia
#          2. ['Albert', 'Ben', 'Carol', 'Donna', 'Eugenia'] #ANSWER


#! Dictionarys
# Create an empty dictionary called personal_info.

# Add the following key-value pairs to the dictionary:
# "name": "John Doe"
# "age": 25
# "email": "john@example.com"

# Create an empty dictionary
personal_info = {}

# Add key-value pairs
personal_info["name"] = "John Doe"
personal_info["age"] = 25
personal_info["email"] = "john@example.com"

# Print the resulting dictionary
print(personal_info)

# or

# Create a dictionary with initial key-value pairs
personal_info = {"name": "John Doe", "age": 25, "email": "john@example.com"}

# Print the resulting dictionary
print(personal_info)


#! Students

# Create a dictionary named student with "name", "age", and "grade" keys.
student = {
    "name": "Maddy",
    "age": 25,
    "grade": "D",
}

# Update students age by one and grade to "A+".
student["age"] += 1
student["grade"] = "A+"

# Print all the keys in the student dictionary.
print("Keys in the student dictionary:", list(student.keys()))

# Print all the values in the student dictionary.
print("Values in the student dictionary:", list(student.values()))

#! Extra
# 1)
cities = {"Shanghai": 17.8, "Istanbul": 13.3, "Karachi": 13.0, "Mumbai": 12.5}
print(cities)

# 2)
keys = ["key1", "key2", "key3"]
values = [1, 2, 3]
res_dict = dict(zip(keys, values))
print(res_dict)

# 3)
keys = ["key1", "key2", "key3"]
values = [1, 2, 3]
res_dict = dict(zip(keys, values))
print(res_dict)

# 4)
dict_1 = {"key1": 1, "key2": 2, "key3": 3}
dict_2 = {"key4": 4, "key5": 5, "key6": 6}
dict3 = {**dict_1, **dict_2}
print(dict3)

# 5)
dictionary = {
    "class": {"student": {"name": "Mike", "marks": {"physics": 70, "history": 80}}}
}
print(dictionary["class"]["student"]["marks"]["history"])

# 6)
verse_dict = {
    "if": 3,
    "you": 6,
    "can": 3,
    "keep": 1,
    "your": 1,
    "head": 1,
    "when": 2,
    "all": 2,
    "about": 2,
    "are": 1,
    "losing": 1,
    "theirs": 1,
    "and": 3,
    "blaming": 1,
    "it": 1,
    "on": 1,
    "trust": 1,
    "yourself": 1,
    "men": 1,
    "doubt": 1,
    "but": 1,
    "make": 1,
    "allowance": 1,
    "for": 1,
    "their": 1,
    "doubting": 1,
    "too": 3,
    "wait": 1,
    "not": 1,
    "be": 1,
    "tired": 1,
    "by": 1,
    "waiting": 1,
    "or": 2,
    "being": 2,
    "lied": 1,
    "don't": 3,
    "deal": 1,
    "in": 1,
    "lies": 1,
    "hated": 1,
    "give": 1,
    "way": 1,
    "to": 1,
    "hating": 1,
    "yet": 1,
    "look": 1,
    "good": 1,
    "nor": 1,
    "talk": 1,
    "wise": 1,
}
print(verse_dict, "\n")

# find number of unique keys in the dictionary
num_keys = len(set(verse_dict.keys()))
print("The number of unique keys in the dictionary are: ", num_keys)

# find whether 'breathe' is a key in the dictionary
contains_breathe = "breathe" in verse_dict
print("Is the word breathe in the dictionary: ", contains_breathe)

# create and sort a list of the dictionary's keys
sorted_keys = sorted(verse_dict.keys())

# get the first element in the sorted list of keys
print("The first element in the list of sorted keys is: ", sorted_keys[0])

# find the element with the highest value in the list of keys
print("The key with the highest value in the dictionary is: ", sorted_keys[-1])

# 7)
employees = ["Joe", "Tom"]
defaults = {"designation": "Developer", "salary": 8000}
res = dict.fromkeys(employees, defaults)
print(res)

# 8)
sample_dict = {
    "emp1": {"name": "Jhon", "salary": 7500},
    "emp2": {"name": "Emma", "salary": 8000},
    "emp3": {"name": "Brad", "salary": 500},
}
sample_dict["emp2"]["salary"] = 10000
print(sample_dict)
