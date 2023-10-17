# Square
size = 5
print("Square:")
for i in range(size):
    for j in range(size):
        print("*", end=" ")
    print()

# Triangle
size = 5
print("\nTriangle:")
for i in range(1, size + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# Rectangle
size = 5
width = size * 2
print("\nRectangle:")
for i in range(size):
    for j in range(width):
        print("*", end=" ")
    print()


# Star Pattern
size = int(input("Please Enter a size: "))

for i in range(1, 2 * size):
    for j in range(1, 2 * size):
        if j == i or j == 2 * size - i or i == size or j == size:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

'''
for i in range(1, 2 * size): outer loop iterates over the rows of star pattern. from 1 to 2*size -1
for j in range(1, 2 * size): inner loop iterates over the columns of each row, from 1 to 2*size -1

if statement inside the loops checks the condition for print * or " " based on position of i and j
j == i or j == 2 * size - i: prints * if j is equal to i or j is equal to 2 * size -1. This creates the diagonal line of the star
i == size or j == size: prints * if i is equal to the size or j is equal to the size. This creates horizontal and verticale lines of the star pattern

'''