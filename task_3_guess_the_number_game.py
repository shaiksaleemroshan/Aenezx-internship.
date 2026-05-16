# Guess the Number Game

import random

computer_number = random.randint(1, 100)

print("Welcome to Guess the Number Game")
print("Guess a number between 1 and 100")

guess = 0

while guess != computer_number:

    guess = int(input("Enter your guess: "))

    if guess < computer_number:
        print("Your guess is too low")

    elif guess > computer_number:
        print("Your guess is too high")

    else:
        print("Congratulations! You guessed the correct number")
        