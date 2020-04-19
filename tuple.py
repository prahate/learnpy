# tuples
# tuples are immutable lists
mytuple = (23,'Prath', True, 23)

# Following statement is invalid as tuples are immutable
#mytuple[1] = 'z'
print(mytuple[0])

# since tuples are immutable they can be used as keys for dictionary
# tuples are faster than list and they can be used when we dont require values in the list to be modified

#count methods counts the occurance of value in tuple
print(mytuple.count(23))

# index method gives the index of the value if present is tuple
print(mytuple.index(True))

print(len(mytuple))