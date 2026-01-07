# From the tuple (1, 4, 7, 12, 17, 20), display all even numbers and calculate their sum.

numbers = (1, 4, 7, 12, 17, 20)
even_sum = 0

for num in numbers:
    if num % 2 == 0:
        print(num)
        even_sum = even_sum + num

print("Sum of even numbers are:", even_sum)
