import random
import math

# Function to get an integer from the user
def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

# Function to conduct one round of the game
def play_game():
    # Getting the lower bound value
    lower = get_integer("Enter the lower bound: ")

    # Getting the upper bound value
    upper = get_integer("Enter the upper bound: ")

    # Checking if the lower bound is less than the upper bound
    if lower > upper:
        print("The lower bound cannot be greater than the upper bound. Try again.")
        return

    # Generating a random number within the range
    x = random.randint(lower, upper)
    max_guesses = round(math.log(upper - lower + 1, 2))
    print(f"\n\tYou have {max_guesses} chances to guess the integer!\n")

    # Initializing the number of attempts
    count = 0

    # Loop for guessing the number
    while count < max_guesses:
        count += 1
        guess = get_integer("Guess the number: ")

        # Checking conditions
        if x == guess:
            print(f"Congratulations! You guessed it in {count} tries.")
            return  # Ends the function after guessing the number
        elif x > guess:
            print("You guessed too low!")
        else:
            print("You guessed too high!")

    # If the number of attempts is exhausted and the user did not guess the number
    print(f"\nThe number was {x}")
    print("\tBetter luck next time!")

# Function to restart the game
def main():
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing! See you next time!")
            break

if __name__ == "__main__":
    main()
