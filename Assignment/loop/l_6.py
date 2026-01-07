# From the set {1, 4, 5, 7, 8, 11, 12, 15, 18}, generate a new list such that odd numbers are doubled and even numbers are tripled. The new list should not include the number 5. Stop further processing if the number 15 is encountered.

set_num = {1, 4, 5, 7, 8, 11, 12, 15, 18}
new_set = []

for i in set_num:
    if i == 5:
        continue
    elif i == 15:
        break
    elif i % 2 == 1:
        new_set.append((i * 2))
    elif i % 2 == 0:
        new_set.append((i * 3))
print(new_set)
