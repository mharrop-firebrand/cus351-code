def user_info():
    while True:
        first_name = input("Enter the first name: ")
        if len(first_name) < 2:
            print("First name must be at least 2 characters long.")
        elif any(char.isdigit() for char in first_name):
            print("First name cannot contain numbers.")
        else:
            return first_name

user_info()
