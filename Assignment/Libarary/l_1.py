# Create a guessing game in Python. Computer has to randomly select a number between 1 to 10 and then prompt user to guess it. If user guesses correctly display You Win. If user guess is not correct display, You Loose. Number was {num}.


import random

num = random.randint(1, 10)
guess_num = int(input("Guess a number between 1 and 10: "))

if guess_num == num:
    print("You Win")
else:
    print(f"You Loose. Number was {num}")
