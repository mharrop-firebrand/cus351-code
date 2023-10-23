# Syntax Error Example
print("Hello World")
x = 2
if x > 5:
    print("x is greater than 5")

# Type Error Example
num = 10
result = num + 5

num_str = 10
result = num_str + 5
print(result)

# Name Error Example
variable = 5
print(variable)


def print_greeting(Message):
    print(Message)


hi = "Hi"
print_greeting("hi")


# Logic Error Example
"""
this function should return an int. With pi * r squared
"""


def calculate_area(radius):
    return (3.14 * radius) ** 2


result = calculate_area(5)
print(result)


def print_numbers():
    for i in range(6):
        print("hi")
    print(i)


print_numbers()


# Runtime Error Example
def division(x, y):
    return x / y


result = division(10, 2)
print(result)


my_list = [1, 2, 3, 4]

print(my_list[4])
