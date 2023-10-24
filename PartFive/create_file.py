# We can use the 'x' mode within the 'open()' function

#! Create file
try:
    with open("example2.txt", "x") as file:
        file.write("I am the new content in this file")
    with open("example.txt", "r") as file:
        print(file.read())
except FileExistsError:
    print("File Already exists")
