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

def superfunc(name, *args, message='Hello', **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    print(f'{message} {name}')
    return sum(args) + total

print(superfunc('prath', 1,2,3, num1=12, num2=12))

## RUle position of arguments to function
# params, *args, default_parameters, **kwargs
def superfunc(name, *args, mess='Hello there', **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    print(f'{mess} {name}')
    return sum(args) + total

print(superfunc('prath', 1,2,3,4,5, num1=10, num2=10))


def highest_even(li):
    highest = 0
    for value in li:
        if value % 2 == 0:
            if value > highest:
                highest = value

    return highest

# more optimised solution
def highest_even2(li):
    even = []
    for value in li:
        if value % 2 == 0:
            even.append(value)

    return max(even)


print(highest_even2([1,4,6,8,66,55,32,45]))