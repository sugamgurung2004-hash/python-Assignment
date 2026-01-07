# Get two input from user and display if first number is divisible by the second.[21 is(not) divisible by 7]

a=int(input('Enter the first number:'))
b=int(input('Enter the second number:'))

if b == 0:
    print("Division by zero is not allowed.")
elif a % b == 0:
    print(f"{a} is divisible by {b}")
else:
    print(f"{a} is NOT divisible by {b}")