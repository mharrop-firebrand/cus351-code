#
#! For loops
# for item in sequence:
#   Code block to be executed for each item in the sequence

# Printing numbers from a list
numbers = [1, 2, 3, 4, 5]

for i in numbers:
    print(i)

# Calculating the sum of numbers from a list
numbers = [1, 2, 3, 4, 5]

sum_of_number = 0
# for each items in our list of number:
# do something
for num in numbers:
    sum_of_number += num
    print(f"{num} item in list")
    print(f"{sum_of_number} current sum of number")

print(f"Final sum of numbers {sum_of_number}")

# List of artists
name_of_artists = ["Garth Brooks", "Billie Joel", "Tupac", "Razerlight"]

for artist in name_of_artists:
    print("The favourite artist is:", artist)
    if artist == "Tupac":
        print("Yo its tupac dude!")
    else:
        print("Not tupac")

# Fruit
fruits_list = ["apple", "banana", "orange", "grape", "kiwi"]

for i in fruits_list:
    if len(i) >= 5:
        print(f"The fruit: {i} has 5 or more characters")
    else:
        print(f"The fruit: {i} has less than 5 characters")

# Dictionarys
happy = {
    "maddy": True,
    "bob": True,
    "Jo": False,
    "Sophie": True,
    "Jamie": False,
}
# print(happy)
for key, value in happy.items():
    print(f"Key: {key}, Value: {value}")

true_keys = [key for key, value in happy.items() if value == True]
print("The keys with the value True are:", true_keys)


happy = {
    "maddy": True,
    "bob": True,
    "Jo": False,
    "Sophie": True,
    "Jamie": {"name": "Jam", "age": 23},
}

nested_dict = happy.get("Jamie")

if nested_dict is not None:
    for key, value in nested_dict.items():
        print(f"Key: {key}, Value: {value}")
else:
    print("no nest dictionary")
