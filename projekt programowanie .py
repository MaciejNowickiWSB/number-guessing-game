import random
import math

def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

def play_game():
    lower = get_integer("Enter the lower bound: ")
    upper = get_integer("Enter the upper bound: ")

    if lower > upper:
        print("The lower bound cannot be greater than the upper bound. Try again.")
        return

    x = random.randint(lower, upper)
    max_guesses = round(math.log(upper - lower + 1, 2))
    print(f"\n\tYou have {max_guesses} chances to guess the integer!\n")

    count = 0

    while count < max_guesses:
        count += 1
        guess = get_integer("Guess the number: ")

        if x == guess:
            print(f"Congratulations! You guessed it in {count} tries.")
        elif x > guess:
            print("You guessed too low!")
        else:
            print("You guessed too high!")

    print(f"\nThe number was {x}")
    print("\tBetter luck next time!")

def main():
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing! See you next time!")
            break

if __name__ == "__main__":
    main()
