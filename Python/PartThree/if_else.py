# ! Conditional Statements
# Simple if statement
# if condition:
#   Code block to be executed if the condition is True

#! If Statment
# With strings
weather = """Raining"""

if weather == "Raining":
    print("Grab a coat")
    print("Maybe also an umbrella")
    print("Maybe some wellies?")
else:
    print("I don't know the weather sorry.")

# ! If else statement
# if condition:
#   Code block to be executed if the condition is True
# With Integers
age = int(input("Please enter your age: "))

if age >= 18:
    print("Come in the club, you are an adult")
else:
    print("You are underage, you cannot come in")


# ! Elif statement
pizza_topping = input("Please enter a pizza topping: ").strip().lower()

if pizza_topping == "pepperoni":
    print("Here is your pepperoni pizza.")
elif pizza_topping == "tomatoes":
    print("Here is your tomato pizza.")
elif pizza_topping == "cheese":
    print("Here is your really boring plain cheese pizza...")
elif pizza_topping == "pineapple":
    print("Try not to get in a fight, here is your pineapple pizza.")
else:
    print("Sorry no other pizza options.")
print(pizza_topping)


# ! Complex comparisons
# Logial operators
# and - both have to be true
age = 17
grade = 90

if age >= 18 and grade >= 90:
    print("You are an adult with a good grade")
elif age < 18:
    print("Underage")
elif age < 18 and grade < 90:
    print("underage and bad")

# Age2
age = 18
grade = 90

if age < 18 and grade < 90:
    print("underage and bad")
elif age < 18:
    print("Underage")
elif age >= 18 and grade >= 90:
    print("You are an adult with a good grade")

# Weather
weather = "Raining"
temp = "Cold"

if weather == "Raining" and temp == "Cold":
    print("It's cold and raining, grab a coat")


# or - one has to be true
is_sunny = True
is_warm = False
# To pass our if:
# if  True   or False
# if  True   or True
# if  False  or True
if is_sunny or is_warm:
    print("It is either sunny or warm or both")
else:  # False or False
    print("Neither sunny or warm")


# not -flips the operator
number = 42

if not number == 0:
    print(f"{number} is not equal to zero")
else:
    print(f"{number} is equal to zero")

# Raining
raining = " "
# if False
# If raining is not True
if not raining:
    print("It is not raining")
elif raining:
    print("It is raining")

# if True
# if raining is true
if raining:
    print("It is raining")

# ! Multiple
# User information
age = 17
is_student = False
has_job = True

if (age < 18 or age > 65) and not is_student and has_job:
    print("You are eligable for a discount")
else:
    print("No discount for you!")
