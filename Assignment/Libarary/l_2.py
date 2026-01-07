# Modify this guessing game so that user has three attempt to guess. On incorrect display Incorrect!! Guess higher/lower number depending upon if number guessed by user is lower or higher. If user can’t guess in 3 attempt display You Loose. Number was {num}.

import random

num = random.randint(1, 10)
chances = 3

while chances > 0:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == num:
        print("You Win")
        break
    else:
        chances = chances - 1
        if chances > 0:
            print(f"Wrong guess! You have {chances} chances left.")

if chances == 0:
    print(f"You Loose. Number was {num}")
