# The range() function has different forms, but the most common form is range(start, stop, step).
# List of number 1-5
print(list(range(5)))  # [1, 2, 3, 4]
# Generates a sequence of numbers from 1 to 5
for i in range(1, 6):
    print(i)

# Generates a sequence of odd numbers from 0 to 9 every 2
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)

# Generates a sequence of odd numbers from 1 to 9 every 2
for i in range(1, 10, 2):  # 1, 3, 5, 7, 9
    print(i)

# Generates a sequence of numbers from 0 to 5
for i in range(0, 6):
    print(i)

# Loops over a sequence of numbers from 0 to 5
numbers = [0, 1, 2, 3, 4, 5]
for i in numbers:
    print(i)

# iterate over the indices of a list or string
word = "Python"
# range(0,7)
for letter in range(len(word)):
    print(f"letter at index {letter} is {word[letter]}")
    print(word[letter], letter)

# Instead of writing it all out:
print(word[0])
print(word[1])
print(word[2])
print(word[3])
print(word[4])
print(word[5])
