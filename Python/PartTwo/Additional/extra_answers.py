#
#! Lists
# Create a list named fruits with the following items: "apple", "banana", "orange", "grape".
fruits = ["apple", "banana", "orange", "grape"]

# Add "watermelon" to the end of the fruits list.
fruits.append("watermelon")

# Insert "kiwi" at the second position in the fruits list.
fruits.insert(1, "kiwi")

# Remove "orange" from the list.
fruits.remove("orange")

# Print the third item in the fruits list.
print(fruits[2])

#! Sets
# Create a set named colours with the following items: "red", "blue", "green".
colors = {"red", "blue", "green"}

# Add "yellow" to the colours set.
colors.add("yellow")

# Remove "blue" from the set.
colors.remove("blue")

# Check if "green" is in the set.
print("green" in colors)

# Print the number of items in the colours set.
print(len(colors))

#! Tuples
# Create a tuple named days with the days of the week.
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# Print the third day of the week.
print(days[2])

# Attempt to change the second day to "Funday" (observe the error).
# Concatenate days tuple with a tuple containing "Saturday" and "Sunday".
updated_days = days + ("Saturday", "Sunday")

# Print the updated days tuple.
print(updated_days)

#! Dictionaries
# Create a dictionary named student with "name", "age", and "grade" keys.
student = {"name": "", "age": 0, "grade": ""}

# Assign values to the keys: name - "Name", age - int, grade - "Char".
student["name"] = "Alice"
student["age"] = 25
student["grade"] = "A"

# Update students age to by one and grade to "A+".
student["age"] = 26
student["grade"] = "A+"

# Print all the keys in the student dictionary.
print(student.keys())

# Print all the values in the student dictionary.
print(student.values())

#! Membership Operators
# Create a list named numbers with the following items: 10, 20, 30, 40, 50.
numbers = [10, 20, 30, 40, 50]

# Check if 25 is in the numbers list.
numbers = [10, 20, 30, 40, 50]

# Check if 30 is not in the numbers list.
print(30 not in numbers)

# Create a set named letters with the items: "a", "b", "c".
letters = {"a", "b", "c"}

# Check if "b" is in the letters set.
print("b" in letters)


#! Compound Data Structures
# Create a list of dictionaries named people with two dictionaries.
people = [{"name": "", "age": 0}, {"name": "", "age": 0}]

# Each dictionary should have "name" and "age" as keys.
print(people[1]["name"])
print(people[1]["age"])

# Print the name and age of the second person in the list.
print(people[1]["name"], people[1]["age"])

# Update the age of the first person.
people[0]["age"] = 30

# Add a new person to the list of dictionaries.
new_person = {"name": "Eve", "age": 28}
people.append(new_person)
