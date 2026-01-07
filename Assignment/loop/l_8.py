# 8.Store a list of fruits. Create a new list such that if a fruit starts with a/A, convert it to uppercase; otherwise, convert it to lowercase (use for loop and list comprehension).


fruits = ["Apple", "banana", "Apricot", "Mango", "avocado", "Orange"]
new_fruits = []

for fruit in fruits:
    if fruit.startswith('a') or fruit.startswith('A'):
        new_fruits.append(fruit.upper())
    else:
        new_fruits.append(fruit.lower())

print(new_fruits)
