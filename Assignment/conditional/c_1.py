# Get customer name and birth year from user input and display is he/she can vote:Ram you are [not] eligible for voting.[people with age 18 or more can vote]

name=input("Enter the name:").capitalize()
birth_year=int(input("Enter the birth year:"))
current_year=2025
age=current_year-birth_year

if age>=18:
    print(f"{name} you are eligible for voting ")
else:
    print(f"{name} you are not eligible for voting")
