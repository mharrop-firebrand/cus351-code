#
#! Functions
#! OLD WAY
# x = 5
# y = "Maddy"
# print(x + y)


#! Simple Function
# Function without arguments or return value:
# def add():
#     x = 5
#     y = 7
#     print(x + y)

# Call the function
# add()


#! Parameters & Arguments
# Function to times one number by another number
def add(x, y):
    """
    This function add() takes two paramenters.
    Parameters: x(int) and y(int)
    """
    print(x + y)
    print(f"{x} + {y}")


# Call the function
# add(10)
# add(60, 92)
# add(5, 42)
# add(-109, 3)
# add(690000, 22)
# add('Hi', "60")
# add('Hi', 6) Doesnt work


#! Default Parameters
# Function with arguments but no return value:
def times(x, z, y=5, j=0):
    print(x * y)
    print(z)


# num1 = 6
# num2 = 8
# times(num1, num2, 10, 2)
# times(6, 10)
# times(6, 8, 10, 2)


#! Arguments
# ? It is important to have the same number of arguments and parameters
# Key Word argument
def subtract(num1, num2):
    print(num1 - num2)


# subtract(num2 = 16, num1 = 42)
# subtract(16, 42)
# subtract(108, 15)
# subtract(num2 = 10, num1 = 15)
# subtract(num1 = 50, num2 = 15)
# subtract() doesnt work

# Data structure as argument

# for i in ls:
#     print(i)


def my_list(ls):
    for i in ls:
        print(i)
    return i


ls = ["Hello", "Maddy", "Python", "World"]
# sentence = 'The word is', my_list(ls)
# print(my_list(ls))

# my_list(["Hi", "Hello", "Bye"])

ls2 = list((1, 2, 3, 4))
# my_list(ls2)

# my_list(list(('Hello')))



def dictionary_loop(dictionary):
    for key, value in dictionary.items():
        print(f'Key: {key}, Value: {value}')


person = {'Name': 'Maddy', 'Age': 46, 'City': 'Manchester'}
# dictionary_loop(person)

bank_account_info = {'Account Number': '1648208', 'Sort-Code': '51-61-00', 'Account Name': 'Madeline Harrop'}
# dictionary_loop(bank_account_info)

#! Return Statments
# Function with arguments and a return value:
def divide(num1, num2):
    result = num1 / num2
    print(result)
    return result

# x = divide(50, 10)
# print(x * 2)

# With a return and storing in a tuple
def calculations(x, y):
    add = x + y
    subtract = x - y
    divide = x / y
    multiply = x * y

    result = add, subtract, divide, multiply
    return result

# print(calculations(14, 42))


# Storing an input in a function
def my_post():
    post_text = input('Write your post here: ')
    return post_text

print(my_post())
print(my_post())

#! Pass
