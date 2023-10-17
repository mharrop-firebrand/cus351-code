"""
for outer_variable in outer_sequence:
    Outer loop code
        for inner_variable in inner_sequence:
            Inner loop code
    Outer loop code    
"""
# ? Be cautious about using nested loops excessively as they can lead to performance issues, especially with larger data sets

# Matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# outer loop for the rows in my list
for row in matrix:
    # inn loop for the elements in each row
    for element in row:
        print(element, end=" ")
    print()  # This is to move on to the next line after each row is printed

# ls = [1, 2, 3]

# for i in ls:
#     print(i)

# Shapes
""" 
*
**
***
****
*****
"""
# triangle_size = 5
# i = 1
# while i <= triangle_size:
#     j = 1
#     while j <= i:
#         print('*', end='')
#         j += 1
#     print() # Move on to the next line after each row is printed
#     i += 1

# Multiplication Table
# row = 1
# while row <= 10:
#     column = 1
#     while column <= 10:
#         result = row * column
#         print(f'{row} X {column} = {result}', end=' ')
#         column += 1
#     print()
#     row += 1


# Schedule Grid
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
time_slots = ['Morning', 'Afternoon', 'Evening']

for day in weekdays:
    for slot in time_slots:
        print(f'{day}: {slot}', end = "\n")
        # Send to API dave wants monday Evening
    print()
