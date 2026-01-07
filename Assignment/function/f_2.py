# Write a function sum all that takes any number of numeric argument and display the sum

def sum_num(n):
    sum = 0
    for i in range(1, n):
        sum += i
    print(sum)

n = int(input("Enter range: "))
sum_num(n)

