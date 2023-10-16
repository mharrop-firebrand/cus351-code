# for outer_variable in outer_sequence:
#     Outer loop code
#     for inner_variable in inner_sequence:
#         Inner loop code
#     Outer loop code


# Matrix


# Be cautious about using nested loops excessively as they can lead to performance issues, especially with larger data sets


""" 
*
**
***
****
*****
"""

# Nested while loop to generate the triangular pattern


# Multiplication Table
# for outer in range(1, 11):
#     for inner in range (1, 11):
#         print(outer * inner, end= ' ')
#     print()


# Inner loop executes 3 times to print the current list item
weekdays = ["Mon", "Tue", "Wed", "Thur", "Fri"]

for days in weekdays:
    times = 0
    while times < 3:
        print(days, end=" ")
        times += 1
    print()
