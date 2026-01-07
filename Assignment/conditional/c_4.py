# Take two numbers as input and print largest among them 

a=float(input("Enter the first number:"))
b=float(input("Enter the second number:"))

if a> b:
    print(f"Largest number is {a}:")
elif a<b:
    print(f"Largest number is {b}")
else:
    print("Given numbers are eQual")
    