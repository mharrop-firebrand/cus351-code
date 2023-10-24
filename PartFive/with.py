# Unlike open() where you have to close the file with the close() method, the with statement closes the file for you without you telling it to.

# This is because the with statement calls 2 built-in methods behind the scene - __enter()__ and __exit()__

#! read()
my_file = "example.txt"
# Open the file in read mode
with open(my_file, "r") as file:
    # File handling operations go here
    print(file.read())
# The file is automatically closed when the block inside 'with' is exited


#! readlines()
with open(my_file, "r") as file:
    # Open the file in read mode
    for line in file:
        print(line)
# The file is automatically closed when the block inside 'with' is exited
