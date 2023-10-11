#
# ! Type casting
# Int to String
num = 42
num_str = str(num)
print(type(num_str))
print('Meaning of life ' + num_str)

# String to int
string_of_number = "123"
# print(string_of_number + 1) wont work
string_of_numbers_ints = int(string_of_number)
print(string_of_numbers_ints + 1)

num = int(input("please enter a number: "))
print(num)
print(type(num))
