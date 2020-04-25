# print (3 + 7)
# print (4 * 5)
# print (2 - 5)
# print (type(22 / 7))
# print (type(0.0))
# print (6 ** 8)
# print (7 // 3)
# print (bin(1024))

# user_name = 'pratham'
# user_password = "learnPython"
# long_str = '''
# Hello there prath
#  0   0 
#    o
#   ===

# How are you doing? '''

# print (long_str)

# first_name = 'Prathamesh'
# last_name = 'Rahate'
# full_name = first_name + ' ' + last_name
# print (full_name)


#Formatted strings
# name = 'Johnny'
# age =  30
# #print ('Hi ' + name + ' you are ' + str(age) + ' years old.')
# # Below is the formatted string, feature of python 3
# print (f'Hi {name} you are {age} years old.')


# selfish = 'me me me'
# print (selfish[0])
# print (selfish[4])

# selfish = '01234567'
# #  [start:stop:step]
# print (selfish[0:4])
# print (selfish[1:3])
# print (selfish[0:7:2])
# print (selfish[::2]) #will step by 2 and print
# print (selfish[-1]) #will start from end
# print (selfish[::-1]) #will print reverse


# username = input ("Enter username:")
# password = input ("Enter password:")

# pswd_hide = str('*' * len(password))
# print (f'{username}, your password {pswd_hide} is {len(password)} letters long')


# li = [1,2,3,4]
# li2 = ['a', 'b', 'e']
# li3 = [1,2, 'a', 'c', True]

# amazon_cart = [
#   'Notebooks',
#   'Headphones',
#   'Sports Shoes',
#   'Grocery'
# ]

# print(amazon_cart)
# #list slicing is similar to string slicing
# print (amazon_cart[1:])
# # IMP: Lists are mutable
# amazon_cart [0] = 'Laptop' # this is valid
# print (amazon_cart)

# # this created new list and assigns it to new_cart
# # below statement is equivalent to copying list to another list
# new_cart = amazon_cart[1:] 
# print(new_cart)

# # but following statement will modify amazon_cart value if new_cart is modified since they new_cart points to same memory as of amazon_cart
# new_cart = amazon_cart
# new_cart[2] = 'Running Shoes'
# print (new_cart)
# print (amazon_cart)

#List methods

#adding

amazon_cart = [
   'Notebooks',
   'Headphones',
   'Sports Shoes',
   'Grocery'
 ]

# append() modifies list in place
# new_list = amazon_cart.append(100)

#insert(index, data) inserts data at index in place in list
# new_list = amazon_cart.insert(3, 100)

# extend extends the list with iterable data in place
#amazon_cart.extend([100, 101])
# print (new_list)
#print (amazon_cart)

#pop(index) pops element from index, if index not specified then pops last element
#print (amazon_cart.pop())
#print (amazon_cart)
#print (amazon_cart.pop(1))

#remove(value) removes value from list
#amazon_cart.remove(100)
#print(amazon_cart)

#clear () clears entire the list
#print(amazon_cart.clear())
#print(amazon_cart)

#index methond in list
#index (value, start, stop) return first occurance of value
#basket = [1,2,3,6,5,8,0,4]

#print(basket)

#print(basket.index(4))

# sort the list in ascending order
#basket.sort()

# reverse() reverses the indices in list
#basket.reverse()
#print (basket)

#print(list(range(100)))

#sentence = ''

#new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'prath'])

#print(new_sentence)


# Dictionary
# is an unoredered key value pairs
# key can be any immutable object i.e. key can not change
# keys in dictionary has to be unique
# value can be of any data type , it can be list, string, int or boolean Value

mydict = {
    'a': [4,5,3],
    'b': "Hello World",
    'c': True,
    123: [7,8,9],
    'age': 29
#    [5]: "This is not allowd as list is mutable object"
}

#print(mydict)
#print(mydict['a'][1])
#print(mydict[123])

# Dictinoary methods
# get method is used to get access keys to see if they exist and get the value
#print(mydict.get('c'))

# this would normally result in error as key doesn't exist
# but with get it returns None is key is not present otherwise returns value
#print(mydict.get('hey'))

# here we set default value in case key is not present, if it is present it will print actual value 
#print(mydict.get('age', 30))

# another way to create dictionary
user2 = dict(name='Pratham', last_name='Rahate', age=29)
#print(user2)
#print(user2['last_name'])

# in used same way as incae of list
#print('name' in user2)

# check key in key of dictionary
#print('name' in user2.keys())

# check values in dictionary
#print('rahate' in user2.values())

#prints items in dictionary
#print(user2.items())

# copy ceates copy of ditctionary
user3 = user2.copy()
#print(user3)

#clear clears the ditctionary
#print(user2.clear())

#pop pos the item from dictionary also removes the key from dictionary
#print(user2.pop('age'))
#print('age' in user2.keys())

# popitems randomy pops item in dictionary
#print(user2.popitem())

#update updates value for Key
# if the obejct is not in dictionary it will update dictionary with object
#user2.update({'age':30})
#print(user2)

#user2.update({'Location':'Mumbai'})
#print(user2)

# tuples
# tuples are immutable lists
mytuple = (23,'Prath', True, 23)

# Following statement is invalid as tuples are immutable
#mytuple[1] = 'z'
#print(mytuple[0])

# since tuples are immutable they can be used as keys for dictionary
# tuples are faster than list and they can be used when we dont require values in the list to be modified

#count methods counts the occurance of value in tuple
#print(mytuple.count(23))

# index method gives the index of the value if present is tuple
#print(mytuple.index(True))

#print(len(mytuple))


#set
# set is an unordered collection of unique objects
#myset = {1,2,3,4,5,5}

# in set every thing is unique, if there are repeated values in set then it will be considered once
#print(myset)

# add values to set
#myset.add(100)
#print(myset)

# lets say we have array with duplicate items and print it only non-repated item
#myarr = [1,2,3,4,5,6,6,6,7,7]
#print(set(myarr))

# following is invalid sets does not support indexing
#print(myset[0])

#set methods
#my_set = {1,2,3,4,5,3,4}
#your_set = {4,6,5,8,8,7,5}

# prints differing elements
#print(my_set.difference(your_set))

# removes element from set
#my_set.discard(4)
#print(my_set)

# updates my_set by removing same elements
#my_set.difference_update(your_set)
#print(my_set)

# prints common elements between two sets
# this is similar to print(my_set & your_set)
#print(my_set.intersection(your_set))

#print(my_set.isdisjoint(your_set))

# combine two set
# this is similar to print(my_set | your_set)
#print(my_set.union(your_set))

# Conditionals
# if else

#is_old = False
#is_licensed = True

#if is_old:
#    print("You are old enough")
#elif is_licensed:
#    print("You are licensed to drive") 
#else:
#    print("You are not old enough")

# Ternery operator in python

# condition_if_true if condition else condition_if_else
#is_friend = False;

#can_mesage = "Messaging allowed" if is_friend else "Messaging Not Allowed"

#print(can_mesage)

#if (4 > 5):
#    print("4 is greater than 5")
#if (4 < 5):
#    print("4 is less than 5")
#if (5 <= 5):
#    print("True")

#is_magician = True
#is_expert = False

#if (not is_magician):
#    print("You need magic powers")
#if (is_magician and is_expert):
#    print("You are master magician")
#if (is_magician and (not is_expert)):
#    print("Atleast you are getting there")

# for Loop
# here items is similar to i
# and 'Hello world' cna be any iterable object
#for items in 'Hello World':
#    for i in [1,2]:
#        print(items, i)

#for i in [1,2,3,4,5]:
#    print(i)

# iterating over dictionaries
#my_dict ={
#    'name' :"Prathames",
#    'last_name': "Rahate",
#    'age':29,
#    'is_single': False
#}

# if we ietrate the following way it will only iterate over key in dictionary
# we can use dictionary methods like keys(), items() and values() for interating over dictionary keys, data and values
# see below examples
#for items in my_dict:
#    print(items)

# this prints dictionary entires as tuples
#for items in my_dict.items():
#    print(items)
# another way to print dictionary entries not as tuples is
#for key, value in my_dict.items():
#    print(key, value)

# iterate over keys in dictionary
#for items in my_dict.keys():
#    print(items)

# iterate over items in dictionary
#for items in my_dict.values():
#    print(items)


#my_list = [1,2,3,4,5,6,7,8,9,10]
#total =0
#for i in my_list:
#    total = total + i

#print(total)

# range(start, end, increment) is useful in for loops
#for item in range(0,15, 2):
#    print(item)

# to print numbers in reverse
#for item in range(10, 0, -1):
#    print(item)

#range can also be used to create list of intergers
#print(list(range(1,10)))
#print(list(range(0,10,2)))


# enumerate takes an iterable obejct as input and returns the index of value in iterable object
# here i is index returned from enumerate
#for i, char in enumerate('Hellloooo'):
#    print(i,char)

#for i, char in enumerate(list(range(100))):
#    if char == 50:
#        print(f'index of 50 is :{i}')


# while loop
#i=0
#while i < 10:
#    print(i)
#    i = i+1

# use of while Loop
#while True:
#    response = input('Say something :')
#    if response == 'bye':
#        break

picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

for row in picture:
    for pixel in row:
        if pixel == 0:
            print(' ', end='')
        elif pixel == 1:
            print('*', end='')
    print('')



some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicate = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicate:
            duplicate.append(value)

print(duplicate)

# functions
# functions in python starts with def keyword, this tells interpreter it is function
# name and emoji are parameters that say_hello function takes

def say_hello(name, emoji):
    print(f'Helloooo there {name} {emoji}')

#here prath and :d are aguments
# they are also called positional arguments as their order is fixed
# positional arguments
say_hello('Prath', ':D')

#keyword Arguments
say_hello(emoji=':d', name='Dipa')

def say_gm(name='Prath', surname='Rahate'):
    print(f'Good Morning! {name} {surname}')

say_gm()

#returning from functions
# use keyword return to return values from function
def sum(num1, num2):
    return num1 + num2

print(sum(3,5))

# functions within functions
def sum2(num1, num2):
    def add5(num1, num2):
        return num1 + num2 + 5
    return add5(num1, num2)

print(sum2(2,4))


# docstrings in python
# inside function we can define docstrings to give infomration to user about function like what function compile
def some_func(a):
    '''
    INFO: This function prints value passed to it
    '''
    print(a)

some_func('Hey')
# or we can use help function to give info about function
help(some_func)