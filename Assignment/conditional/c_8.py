# Get a customer name and birth year from user input and display if he/she can have license vote:Ram, You are [not] eligible for driving.(License Age:18 and 70)

name=input("Enter your name:").capitalize()
birth_year=int(input("Enter your birth year:"))
current_year=2025
age=current_year-birth_year


if 18<= age <=70:
    print(f"{name} you are eligible for license.")
else:
    print(f"{name} you are not eligible for license.")