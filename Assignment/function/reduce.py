# Reduce
list_a = [1, 2, 4]

list_result = list((lambda x,y:map(x,y), list_a))
print(list_result)
# next(list_result)
