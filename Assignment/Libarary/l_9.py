# Calculate LCM of numbers present in a list
import math

numbers = [4, 6, 8]


def lcm(a, b):
    return a * b // math.gcd(a, b)


result = numbers[0]
for i in range(1, len(numbers)):
    result = lcm(result, numbers[i])

print("LCM of the list is:", result)
