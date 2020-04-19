# Dictionary is a data type  or data structure in python
# Dictionary is an unordered key value pair
# Dictionary in python has format as follows
# mydict = {
#   key: value,
#   key: value    
# }
# key is used to access values in dictionary
# to print Value
# print(mydict[key])
# Dictionary values can be any other data type, it can be list, string, boolean

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
#    [5]: "This is not allowd as list is mutable object"
}

print(mydict)
print(mydict['a'][1])
print(mydict[123])

# Dictinoary methods
# get method is used to get access keys to see if they exist and get the value
print(mydict.get('c'))

# this would normally result in error as key doesn't exist
# but with get it returns None is key is not present otherwise returns value
print(mydict.get('hey'))

# here we set default value in case key is not present, if it is present it will print actual value 
print(mydict.get('age', 30))

# another way to create dictionary
user2 = dict(name='Pratham', last_name='Rahate')
print(user2)
print(user2['last_name'])

# in used same way as incae of list
print('name' in user2)

# check key in key of dictionary
print('name' in user2.keys())

# check values in dictionary
print('rahate' in user2.values())

#prints items in dictionary
print(user2.items())

# copy ceates copy of ditctionary
user3 = user2.copy()
print(user3)

#clear clears the ditctionary
#print(user2.clear())

#pop pos the item from dictionary also removes the key from dictionary
#print(user2.pop('age'))
#print('age' in user2.keys())

# popitems randomy pops item in dictionary
print(user2.popitem())

#update updates value for Key
# if the obejct is not in dictionary it will update dictionary with object
user2.update({'age':30})
print(user2)

user2.update({'Location':'Mumbai'})
print(user2)
