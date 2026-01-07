# Write a function to check whether a number is prime or not. Using this function, print the first 15 prime numbers.


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


count = 0
number = 2

while count < 15:
    if is_prime(number):
        print(number, end=" ")
        count = count + 1
    number = number + 1
