# Create a Rock, Scissor, Paper game. Computer chooses & prompt user to choose his choice. Display You Win/Loose. [Should ask if he wants to replay]

import random

choices = ["rock", "paper", "scissor"]

while True:
    computer = random.choice(choices)
    user = input("Choose Rock, Paper, or Scissor: ").lower()

    if user not in choices:
        print("Invalid choice! Try again.")
        continue

    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a Tie!")
    elif (
        (user == "rock" and computer == "scissor") or
        (user == "paper" and computer == "rock") or
        (user == "scissor" and computer == "paper")
    ):
        print("You Win")
    else:
        print("You Loose")

    replay = input("Do you want to play again? (yes/no): ").lower()
    if replay != "yes":
        print("Thanks for playing!")
        break
