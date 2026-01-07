# Calculate the factorial of a number entered by the user using both while and for loops.

# Using for loop
num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact = fact * i

print(f"The factorial of given number using for loop is {fact}")

# Using While Loop
num = int(input("Enter a number: "))

fact2 = 1
i = 1

while i <= num:
    fact2 = fact2 * i
    i += 1


print(f"The factorial of given number using While Loop is {fact2}")
