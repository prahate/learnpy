# Conditionals
# if else
is_old = False
is_licensed = True

if is_old:
    print("You are old enough")
elif is_licensed:
    print("You are licensed to drive") 
else:
    print("You are not old enough")

# Ternery operator in python
# condition_if_true if condition else condition_if_else
is_friend = False;

can_mesage = "Messaging allowed" if is_friend else "Messaging Not Allowed"

print(can_mesage)

is_magician = True
is_expert = False

if (not is_magician):
    print("You need magic powers")
if (is_magician and is_expert):
    print("You are master magician")
if (is_magician and (not is_expert)):
    print("Atleast you are getting there")

# for Loop
# here items is similar to i
# and 'Hello world' cna be any iterable object
# iterables -> list, dictionary, tuple, set, string
# iterated one by one check each item in collection
for items in 'Hello World':
    for i in [1,2]:
        print(items, i)

#for i in [1,2,3,4,5]:
#    print(i)

# iterating over dictionaries
my_dict ={
    'name' :"Prathames",
    'last_name': "Rahate",
    'age':29,
    'is_single': False
}

# if we ietrate the following way it will only iterate over key in dictionary
# we can use dictionary methods like keys(), items() and values() for interating over dictionary keys, data and values
# see below examples
for items in my_dict:
    print(items)

# this prints dictionary entires as tuples
for items in my_dict.items():
    print(items)
# another way to print dictionary entries not as tuples is
for key, value in my_dict.items():
    print(key, value)

# iterate over keys in dictionary
for items in my_dict.keys():
    print(items)

# iterate over items in dictionary
for items in my_dict.values():
    print(items)

my_list = [1,2,3,4,5,6,7,8,9,10]
total =0
for i in my_list:
    total = total + i

print(total)

# range(start, end, increment) is useful in for loops
#for item in range(0,15, 2):
#    print(item)

# to print numbers in reverse
for item in range(10, 0, -1):
    print(item)

#range can also be used to create list of intergers
#print(list(range(1,10)))
#print(list(range(0,10,2)))


# enumerate takes an iterable obejct as input and returns the index of value in iterable object
# here i is index returned from enumerate
#for i, char in enumerate('Hellloooo'):
#    print(i,char)

for i, char in enumerate(list(range(100))):
    if char == 50:
        print(f'index of 50 is :{i}')


# while loop
i=0
while i < 10:
    print(i)
    i = i+1

# use of while Loop
while True:
    response = input('Say something :')
    if response == 'bye':
        break