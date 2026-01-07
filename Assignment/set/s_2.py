#.You are running a stationery store. Store the following items in a list•	book – •pen – 3•pencil – 1•marker – 1 in a list.
# Perform the following operations:

stationary_item=['book','pen','pen','pen','pencil','marker']

# 	1.	Store unique items in a variable and display it

new_item=set(stationary_item)
print(new_item)

# 	2.	Display the total count of unique items

length_item=len(stationary_item)
print(length_item)

# 	3.	Add sticky_notes to the unique items variable and display it

new_item.add('sticky notes')
print(new_item)

# 	4.	Remove pen from the variable and display it

new_item.remove('pen')
print(new_item)

#   5.	Remove staple from the variable and display it

new_item.discard('staple')
print(new_item)