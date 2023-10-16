def create_square(size):
    for i in range(size):
        for j in range(size):
            print("*", end=" ")
        print()


create_square(5)


# Create shapes
def draw_shape(shape, size):
    if shape == "Square":
        for i in range(size):
            for j in range(size):
                print("*", end=" ")
            print()
    elif shape == "Triangle":
        for i in range(1, size + 1):
            for j in range(i):
                print("*", end=" ")
            print()
    elif shape == "Rectangle":
        width = size * 2
        for i in range(size):
            for j in range(width):
                print("*", end=" ")
            print()
    else:
        print("Please enter a correct shape, options are: Square, Rectangle, Triangle")


# draw_shape("Square", 8)
# draw_shape("Square", 3)
# draw_shape("Triangle", 4)
# draw_shape("Rectangle", 4)


# Create a star
def star_pattern(size):
    for i in range(1, 2 * size):
        for j in range(1, 2 * size):
            if j == i or j == 2 * size - i or i == size or j == size:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


star_pattern(int(input("Please enter a size:")))


# Create a diamond
def diamond_pattern(size):
    for i in range(1, size + 1):
        for j in range(1, size - i + 1):
            print(" ", end=" ")
        for k in range(1, 2 * i):
            print("*", end=" ")
        print()

    for i in range(size - 1, 0, -1):
        for j in range(1, size - i + 1):
            print(" ", end=" ")
        for k in range(1, 2 * i):
            print("*", end=" ")
        print()


diamond_pattern(int(input("Please enter a size: ")))
