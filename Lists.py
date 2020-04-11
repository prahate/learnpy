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

#List methods

#adding

#amazon_cart = [
#   'Notebooks',
#   'Headphones',
#   'Sports Shoes',
#   'Grocery'
# ]

# append() modifies list in place
# new_list = amazon_cart.append(100)

#insert(index, data) inserts data at index in place in list
# new_list = amazon_cart.insert(3, 100)

# extend extends the list with iterable data in place
amazon_cart.extend([100, 101])
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
print(amazon_cart.clear())
print(amazon_cart)
