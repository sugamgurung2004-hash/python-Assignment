# Get input of name , age and salary from user and display if he/she is eligible for loan.For person to be eligible for loan he/she has to br at least 21 years with minimum salary of 25K

name=input("Enter the name:").capitalize()
age=int(input("Enter the age:"))
salary=float(input("Enter the salary:"))

if age >= 21 and salary >= 25000:
    print(f"{name} is eligible for a loan.")
else:
    print(f"{name} is NOT eligible for a loan.")



