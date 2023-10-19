"""
Create a account creation function, that takes a first name, last name and uses another function to generate a random id and display this information
"""
import random


# Create user ID function
def generate_user_id():
    return str(random.randint(1000, 9999))


# Create account function
def create_account(first_name, last_name):
    user_id = generate_user_id()
    result = {"user_id": user_id, "first_name": first_name, "last_name": last_name}
    return result


new_account1 = create_account("John", "Doe")
print(new_account1)
# {'user_id': '1234', 'first_name': 'John', 'last_name': 'Doe'}
print("UserId:", new_account1["user_id"])
print("First Name:", new_account1["first_name"])
print("Last Name:", new_account1["last_name"])
