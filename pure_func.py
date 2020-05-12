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

#lambda expressions are functions that are annonymous and used only once
# they are defined as below
# lambda param: action(param)
# multiply_by2 can be implemented using lambda expression as follows

print(list(map(lambda item: item*2, my_list)))

my_list2 = [5,4,3]

print(list(map(lambda item: item* item, my_list2)))

# little tough one
a = [(0,2), (4,3), (9,9), (10, -1)]
a.sort(key=lambda x: x[1])
print(a)

# list, set and dictionary comprehensions
# list comprehensions

my_list = []
for char in 'hello':
    my_list.append(char)

#print(my_list)

# all of the above can be done in single line using list comprehensions
# my_list = [param for param in interable]
my_li = [char for char in 'Hellooo' ]
#print(my_li)

my_li2 = [num for num in range(100)]
#print(my_li2)

my_li3 = [num for num in range(100) if num % 2 == 0]
#print(my_li3)

# all numbers are multiplied by 2
my_li4 = [num*2 for num in range(0,100)]
print(my_li4)