"""
Create a account creation function, that takes a first name, last name and uses another function to generate a random id and display this information
"""
import random


# Create user ID function
def generate_user_id():
    return str(random.randint(1000, 9999))


# Create account function
def create_account(first_name, last_name):
    try:
        # print(Name)
        if not first_name or not last_name or (first_name == " " or last_name == " "): # if firstname or lastname == False
            raise ValueError('Both first name and last name are required') 
            # This might not always happend so we may hit a Name error that was want to except from the try
            # If this value error does raise the program is terminated
        user_id = generate_user_id()
        result = {"user_id": user_id, "first_name": first_name, "last_name": last_name}
        return result
    except NameError:
        return f"Error: There was a name error, caught and handled gracefully carry on with the program:"


new_account1 = create_account("john", " ")
print(new_account1)

# print(name)



raise Exception('hi')