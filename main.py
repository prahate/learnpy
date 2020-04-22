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
for items in 'Hello World':
    for i in [1,2]:
        print(items, i)

#for i in [1,2,3,4,5]:
#    print(i)