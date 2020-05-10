# functional Programming
# separation of data and functions, data and functions/methods are not combined in object similar to classes, they are separate entities

#pure functions
# two basic rules
#1 given same set of input it produce same output everytime
#2 function should not produce any sideeffect i.e. it should not affect or interact with outside world/data such as printing inside function or modifying outside variables that are not part of function itslef

#def multiply_by2(li):
#    new_list = []
#    for item in li:
#        new_list.append(item*2)
#    return new_list

#print(multiply_by2([1,2,3,4]))

# few functions that represent pure functions
# map, filter, zip and reduce

# map(action, data)

new_list = [1,2,3,4,5]
def multiply_by2(li):
    return li * 2

# map object need to be converted to list as it returns an object
print(list(map(multiply_by2, new_list)))
print(new_list)

# filter(action, data)
# filter can return less number of data 
def get_odd(item):
    return item % 2 != 0

print(list(filter(get_odd, new_list)))

# zip, zips two or many iterables into one
my_list = [3,5,6,7,8]
print(list(zip(new_list, my_list)))

# reduce is not built in function
# it has to be imported from functools
from functools import reduce

def accumulator(acc, item):
    return acc + item

# here 0 is the default or initial value of acc
print(reduce(accumulator, [1,2,3,4,5,6,7,8,9], 0))