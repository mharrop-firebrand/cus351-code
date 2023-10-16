while True:
    try:
        # Get the first number from the user
        num1 = float(input("Enter the first number: "))

        while True:
            # Get the operator from the user
            operator = input("Enter operator (+, -, *, /) or 'exit' to quit: ")

            # Check if the user wants to exit
            if operator.lower() == "exit":
                print("Goodbye!")
                exit()

            # Check if the operator is valid
            if operator not in ["+", "-", "*", "/"]:
                print(f"Invalid operator {operator}. Please enter +, -, *, or /.")
                print(f"Currently we have {num1}")
                continue  # Restart the loop

            # Get the second number from the user
            while True:
                user_input = input("Enter the second number: ")
                try:
                    num2 = float(user_input)
                    break  # Break out of the second number input loop if successful
                except ValueError:
                    print(f"Invalid input {user_input}. Please enter a valid number.")
                    print(f"Currently we have {num1} {operator}")

            # Perform calculations based on the operator5
            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                # Check for division by zero using try-except
                try:
                    result = num1 / num2
                except ZeroDivisionError:
                    print("Error: Division by zero is not allowed.")
                    continue  # Go back to asking for the second number

            print(f"Result: {result}")

            # Ask the user whether to continue or quit
            decision = input("Do you want to continue? (yes/no): ")
            if decision.lower() != "yes" and decision.lower() != "y":
                print("Goodbye!")
                exit()

            # If the user wants to continue, use the result as the first number for the next calculation
            num1 = result
            break

    except KeyboardInterrupt:
        print("\nCtrl+C detected.")
        decision = input("Do you want to continue? (yes/no): ")
        if decision.lower() != "yes" and decision.lower() != "y":
            print("Goodbye!")
            exit()
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except Exception as e:
        print(f"An error occurred: {e}")
