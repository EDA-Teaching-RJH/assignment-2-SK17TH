
import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
guess = None

print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Loop until the user guesses the correct number
while guess != secret_number:
    # Get user's guess
    guess = int(input("Enter your guess: "))
    
    # Check if the guess is too low, too high, or correct
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the correct number!")

