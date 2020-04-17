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
print(user2[last_name])