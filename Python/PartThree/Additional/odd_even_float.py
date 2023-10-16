user_input = input("Enter a number: ")
number = float(user_input)

if number.is_integer():
    if number % 2 == 0:
        print(f"{user_input} is a whole and even number.")
    else:
        print(f"{user_input} is a whole and odd number.")
else:
    print(f"{number} is a float.")


#
user_input = input("Enter a number: ")

try:
    number = int(user_input)
    is_float = False
except ValueError:
    number = float(user_input)
    is_float = True

if not is_float:
    if number % 2 == 0:
        print(f"{number} is an integer and even.")
    else:
        print(f"{number} is an integer and odd.")
else:
    print(f"{number} is a float.")
