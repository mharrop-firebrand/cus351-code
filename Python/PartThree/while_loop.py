#
#! While Loops

# while condition:
#   Code block to be executed as long as the condition is True

# printing numbers using a while loop
num = 1

""" Iterations
    inifinte
    while num(1) is less than (or not equal to) 5:
        print num(1)

    num = 1
    while num(1) is less than (or not equal to) 5:
        print num(1)
        add 1 to num(1)

    num = 2

    while num(2) is less than (or not equal to) 5:
        print num(2)
        add 1 to num(2)

    num = 3

    while num(3) is less than (or not equal to) 5:
        print num(3)
        add 1 to num(3)

    num = 4

    while num(4) is less than (or not equal to) 5:
        print num(4)
        add 1 to num(4)

    num = 5
    while num(5) is  equal to 5:
        print num(5)
        add 1 to num(5)

    num = 6
    while num(6) is more than and not equal to 5:
    """


while num <= 5:
    print(num)
    num += 1


"""
It's crucial to ensure that the condition inside the while loop eventually becomes False to avoid an infinite loop.
"""

# Sum of numbers
total = 0
number = 100
while number <= 200:
    total += number
    number += 1
    print(total)

print("Sum of number", total)

""" Iterations
    iteration 1:
    total is 0
    number is 1
    total += number adds 1 to total (total is now 1)
    number += 1 increments number to be 2

    iteration 2:
    total is 1
    number is 2
    total += number add 2 to total (total is now 3)
    number += 1 increments number to be 3

    Iteration 3:
    total is 3
    number is 3
    total += number add 3 to total (total is now 6)
    number += 1 increments number to be 4

    Iteration 4:
    total is 6
    number is 4
    total += number add 4 to total (total is now 10)
    number += 1 increments number to be 5

    Iteration 5:
    total is 10
    number is 5
    total += number add 5 to total (total is now 15)
    number += 1 increments number to be 6

    total is 15
    number is 6
    the condition number <= 5 is no longer true so the loop exits.

    """


# Password Checker
password = input("Enter the password: ").strip().lower()

while password != "secret":
    print("Incorrect Password. Please try again.")
    password = input("Enter the password: ").strip().lower()


print("Access Granted!")
