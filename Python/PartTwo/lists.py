"""
# ! Lists
List can be defined by using square brackets []
Each element in the list should be separated by using commas , ,
Each item within a list has its own position and index
"""
# Empty list
empty_list = []
# print(empty_list)

# Homogeneous
# List of integers
num_list = [1, 2, 3, 4, 5]
# print(num_list)

# List of strings
str_list = ["Hello", "World", "Python"]
# print(str_list)

# A "heterogeneous list" and it's types
het_list = [50, 3.14, "Hello", True, 10000, -50]
# print(het_list)

# Two Separate Lists
list1 = [1, 2, 3]
list2 = ["Hello", "World"]

# Combining two lists for a "nested list"
# list3 = [list1, list2]
# print(list3)

#! Indexing
#      0,  1,    2,       3
#     -4, -3,   -2,      -1
ls = [9, -10, False, "Hello"]
# print(ls[0])
# print(ls[3])
# print(ls[-2])

ls2 = ["Maddy", 3.14, "Cake", 42, True, False, -10]
# print(ls2[3])
# print(ls2[5])
# print(ls2[-6])
# print(ls2[0])
# print(ls2[10]) #ERR index out of range


"""
Slicing []
The lower index is inclusive and the upper index is exclusive
Syntax: [start: stop: step]
start: optional. Starting index of the slice. Defaults to 0.
stop:  optional. The last index of the slice or the number of items to get.
Defaults to 'len(sequence)'.
step:  optional. Extended slice syntax. Step value of the slice. Defaults to 1.
"""

#! A list with ints
ls3 = [5, 10, 50, 100, 150, 200]
# Get the first element
# print(ls3[0:5])  # 5, 10, 50, 100, 150,
# print(ls3[0:3])  # 5, 10, 50
# print(ls3[3:])  # 100, 150, 200
# print(ls3[:4])  # 5, 10, 50, 100
# print(ls3[::2])  # 5, 50, 150
# print(ls3[0:6]) # No index error
print(ls3[0:-4])  # 5, 10
# print(ls3[-5:-2])  # 10, 50, 100
print(ls3[::-1])  # 200, 150, 100, 50, 10, 5

word = "Paint Brush"  # hsurB tniaP
print(word[::-1])