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
#def sum(num1, num2):
#    return num1 + num2

#print(sum(3,5))

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

# *args and **kwargs
# *agrs is used to pass any number of arguments to function
# internal to function args are tuple to function
# **kwargs is used to pass any number of key word args to function
# internal to function kwargs are dictionary

def super_func(*args, **kwargs):
    print(*args)
    print(kwargs)
    print(args)
    total = 0
    for items in kwargs.values():
        total+= items
    return sum(args) + total

print(super_func(1,2,3,4,5, num1=12, num2=23))

## RUle position of arguments to function
# params, *args, default_parameters, **kwargs
#def superfunc(name, *args, mess='Hello there', **kwargs):
#    total = 0
#    for items in kwargs.values():
#        total += items
#    print(f'{mess} {name}')
#    return sum(args) + total

#print(superfunc('prath', 1,2,3,4,5, num1=10, num2=10))

#def highest_even(li):
#    highest = 0
#    for value in li:
#        if value % 2 == 0:
#            if value > highest:
#                highest = value
#    return highest


#print(highest_even([1,4,6,8,66,55,88,45]))

#def highest_even2(li):
#    even = []
#    for value in li:
#        if value % 2 == 0:
#            even.append(value)

#    return max(even)


#print(highest_even2([1,4,6,8,66,55,32,45]))




# class in python
# class in python must follow naming convention like camelcasing
# creating custom object type
# class object attribute can not be modified across instances

#class
class MyObj():
    pass

obj1 = MyObj() # instantiating class
print(type(obj1)) # obj1 is instance of class

class PlayerCharacter:
    #class object attribute
    membership = True
    def __init__(self, name, age):
        self.name = name    # these are class attributes
        self.age = age

    def run(self):
        print('Run')

# classmethods
# they are defined with @classmethod
# class methods can be used without instantiating class
    @classmethod 
    def add_nums(cls, num1, num2):
        return num1 + num2

#class methods can be used to instantiate objects
#   @classmethod
#   def add_nums(cls, num1, num2):
#       return cls('Johnny', (num1 + num2))

# @staticmethod are similar to class methods except they dont have
# cls arguments
    @staticmethod
    def add_num2(num1, num2):
        return num1 + num2



player1 = PlayerCharacter('Harry', 29)
print(player1.name)
print(player1.age)
print(player1.membership)
print(PlayerCharacter.add_nums(5,7))


#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Billy', 2)
cat2 = Cat('Tom', 3)
cat3 = Cat('Meow', 1)


# 2 Create a function that finds the oldest cat
def find_elder_cat(*args):
    return max(args)

print(f'The Oldest cat is {find_elder_cat(cat1.age, cat2.age, cat3.age)} years old')

# encapsulation
# binding of attributes and methods that manipulate data in object

#abstraction
# hiding information or only giving access to what is neccessary
# private and public variables
# python does not have private variables, only the syntax like appending the variable with '_' will signify to user that it is private variable

#inheritance
# inherit the properties of parent class

class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('Signed in')

    def attack(self):
        print('Do nothing')

# Here Archer and wizard class inherit User class as parent
class Archer(User):
    def __init__(self, name, arrows, email):
        # super refers to parent class here it is User
        # it allowsa calling parent class's init method without passing self as argument and initialise email as shown below
        super().__init__(email)
        self.name = name
        self.arrows = arrows
    
    def attack(self):
        User.attack(self)   # calling parents methond inside child
        print(f'Attacking with {self.name} and arrows {self.arrows}')

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def attack(self):
        print(f'Attacking with {self.name} and power {self.power}')
    pass

archer = Archer('Johnny', 20, 'jhonny@yahoo.com')
wizard = Wizard('Jack', 50)

print(archer.email)
wizard.attack()


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



