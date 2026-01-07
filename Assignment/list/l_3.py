#You are running stationary.Store items:book*2, pen*3,pencil*1, marker*1 in a list.

stationary_list=['book','book','pen','pen','pen','pencil','marker']

#1 Display this list.Add pen at end of list and display the list again
print(stationary_list)
stationary_list.append('copy')
print(stationary_list)

#2 Count number of pencil on list and display it

print(stationary_list.count('pencil'))

#3 Add sticky_note in list at third position and display the list 

stationary_list.insert(2,'sticky note')
print(stationary_list)

#4 Remove pencil from list and display list

stationary_list.remove('pencil')
print(stationary_list)


#5 Remove item from 2nd position .Display removed items and the list

stationary_list.pop(1)
print(stationary_list)

#6 Remove item from 1st and 2nd position.Display removed items and the list

remove_1=stationary_list.pop(0)
remove_2=stationary_list.pop(0)
print(remove_1)
print(remove_2)
print(stationary_list)


#7 Display total items in the list 

print(len(stationary_list))

#8 Display all items of list seperated by comma

print(','.join(stationary_list))

#9 Display the items from position 1 to 3 from list

print(stationary_list[0:3])


#10 Display on which position the pen lies in the list . Also display item on 3rd position

print(stationary_list.index('pen'))
print(stationary_list[2])