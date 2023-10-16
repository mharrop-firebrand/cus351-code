import random

# Generate a random number between 1 and 10
correct_number = random.randint(1, 10)

# Initialize a list with numbers from 1 to 10
number_list = list(range(1, 11))

# Initialize the player's points
points = 100

while True:
    # Ask the user for a guess
    guess = int(input(f"Guess a number between 1 and 10 (Points: {points}): "))

    # Check if the guess is correct
    if guess == correct_number:
        print(
            f"Congratulations! You guessed the correct number. {points} points awarded."
        )
        break
    elif guess in number_list:
        print("Incorrect! Try again.")
        # Remove the guessed number from the list
        number_list.remove(guess)
        # Deduct 10 points for an incorrect guess
        points -= 10
        # Check if the player is out of points
        if points <= 0:
            print("Sorry, you're out of points. Game over.")
            break
    else:
        print("Invalid guess. Please choose a number between 1 and 10.")

    # Print the remaining numbers in the list
    print(f"Remaining numbers: {number_list}.")
    print(f"You have {points} left.")
