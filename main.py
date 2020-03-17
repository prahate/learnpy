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


li = [1,2,3,4]
li2 = ['a', 'b', 'e']
li3 = [1,2, 'a', 'c', True]

amazon_cart = [
  'Notebooks',
  'Headphones',
  'Sports Shoes',
  'Grocery'
]

print(amazon_cart)
#list slicing is similar to string slicing
print (amazon_cart[1:])
# IMP: Lists are mutable
amazon_cart [0] = 'Laptop' # this is valid
print (amazon_cart)

# this created new list and assigns it to new_cart
# below statement is equivalent to copying list to another list
new_cart = amazon_cart[1:] 
print(new_cart)

# but following statement will modify amazon_cart value if new_cart is modified since they new_cart points to same memory as of amazon_cart
new_cart = amazon_cart
new_cart[2] = 'Running Shoes'
print (new_cart)
print (amazon_cart)