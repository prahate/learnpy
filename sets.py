#set
# set is an unordered collection of unique objects
myset = {1,2,3,4,5,5}

# in set every thing is unique, if there are repeated values in set then it will be considered once
#print(myset)

# add values to set
myset.add(100)
print(myset)

# lets say we have array with duplicate items and print it only non-repated item
#myarr = [1,2,3,4,5,6,6,6,7,7]
#print(set(myarr))

# following is invalid sets does not support indexing
#print(myset[0])

#set methods
my_set = {1,2,3,4,5,3,4}
your_set = {4,6,5,8,8,7,5}

# prints differing elements
print(my_set.difference(your_set))

# removes element from set
#my_set.discard(4)
#print(my_set)

# updates my_set by removing same elements
#my_set.difference_update(your_set)
#print(my_set)

# prints common elements between two sets
# this is similar to print(my_set & your_set)
print(my_set.intersection(your_set))

print(my_set.isdisjoint(your_set))

# combine two set
# this is similar to print(my_set | your_set)
print(my_set.union(your_set))