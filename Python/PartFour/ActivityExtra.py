"""
Create a account creation function, that takes a first name, last name and uses another function to generate a random id and display this information
"""

import random


# Utility function to generate a unique user ID
def generate_user_id():
    return str(random.randint(1000, 9999))


# 1. Account Management
def create_account(first_name, last_name):
    user_id = generate_user_id()
    return {"user_id": user_id, "first_name": first_name, "last_name": last_name}


# Create user:
new_account_info = create_account("John", "Doe")

# new_account_info stores the function call to create account (which returns a dictionary)
# Using that object we can specify what value we want from the return dictionary with ['keyname']
print("User ID:", new_account_info["user_id"])
print("First Name:", new_account_info["first_name"])
print("Last Name:", new_account_info["last_name"])
