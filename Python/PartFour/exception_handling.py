#
#! Common Exceptions:
# AttributeError
# EOFError
# IOError
# IndexError
# KeyError
# KeyboardInterrupt
# NameError
# StopIteration
# TypeError
# ValueError

#! Try
# try:
#   Code that might raise an exception
#   ...
# except SomeException:
#   Code to handle the exception
#   ...

#! NameError
# print(name)

#! Handling NameError
# try:
#     print(name)
# except NameError as e:
#     print("Error:", e)

# print("Hi")


#! ZeroDivisionError
# OUR PROGRAM WILL BREAK AND NOT CONTINUE SO WE NEED TO HANDLE IT
# num1 = int(input("Please enter a number: "))
# num2 = int(input("Please enter another number: "))
# result = num1 / num2
# print(result)

#! Handling ZeroDivisionError
# try:
#     num1 = int(input("Please enter a number: "))
#     num2 = int(input("Please enter another number: "))
#     result = num1 / num2
#     print(result)
# except ZeroDivisionError:
#     print("ERROR: CANNOT DIVIDE BY ZERO")
# except ValueError:
#     print("VALUE ERROR: DID NOT ENTER A NUMBER")

#! Handling ValueError
# try:
#     age = int(input("Please enter your age: "))
#     print("Your age is: ", age)
# except ValueError:
#     print("Error: invalid input. Did not enter a valid integer")
# # Multiple Exceptions
# except:
#     print("Something went wrong")


#! Inside a function
# def add_numbers():
#     try:
#         num1 = int(input("Please enter a number: "))
#         num2 = int(input("Please enter another number: "))
#         result = num1 + num2
#         print(result)
#     except ValueError:
#         print("ERROR: invalid integers for addition")


# add_numbers()

#! Else

# Else statement must come after the except statement
# try:
#   code that raised an exception
# except:
#   optional block to handle exceptions
# else:
#   if no exception raised execute
# finally:
#   always run

# Try Else
# try:
#     age = int(input("Please enter your age: "))
#     print(age)
# except ValueError:
#     print("That was not an integer, valueError")
# else:
#     print("No exception thrown, correct value")
# # Finally
# finally:
#     print("This function was run, bye")


#! Raise
# raise [ExceptionType([message])]
# ExceptionType: This is the type of exception you want to raise. It can be any built-in or custom exception class.
# message (optional): This is an optional string that provides additional information about the exception. It is helpful for debugging and providing context about the raised exception.
# ValueError
# x = 10

# if x > 5:
#     raise ValueError('X should be less than or equal to 5')

def divide(x, y):
    try:
        if y == 0:
            raise ZeroDivisionError('Division by zero is not allowed')
            # When an exception is raised using the raise statement, it immediately interrupts the normal flow of the program, and the program jumps to the nearest except block that can handle that exception.
            # if none is found, the program terminates with an unhandled exception
        return x / y
    except ZeroDivisionError:
        print('Error: Division by zero is not allowed')
        return None

print(divide(10, 2))
result =divide(10, 0)
if result is None:
    print('Division Failed')

