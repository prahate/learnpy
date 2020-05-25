# decorators
# functions in python can be passed around as variables to other functions
# see example below
def hello():
    print('Helllooooo')

greet = hello
#this will print function location in memory
print(greet)
# to print we can do something like
print(greet())

# so we can do something like this
def hello2(func):
    func()

def greet2():
    print('Hey there')

# we can call it
a = hello2(greet2)
print(a)

# High order functions hello2
# it can be function that accepts another function like hello2 above
# or function that can return function as shown below
def greet3():
    def func():
        return 5
    return func

#define your own decorator
# wraper function and modify or existing function as shown below
def my_decorator(func):
    def wrap_func():
        print('################')
        func()
        print('################')
    return wrap_func

@my_decorator
def print_hello():
    print('Hellooo from decorator')

# the aboe statement is similar to folowing statement
#a = my_decorator(print_hello)
#a()

print_hello()

#passing parameter to my_decorator
def my_decorator2(func):
    def wrap_func2(x):
        func(x)
    return wrap_func2


@my_decorator2
def hello2(greeting):
    print(greeting)

hello2("Good Morning")
# above is equivalent to
#a = my_decorator2(hello2("Good Evening"))

# to pass any number of argumnets there is something called as decorator pattern which can be used
# it is as shown below
# def my_decorator(func):
#   def wrap_func(*args, **kwargs):
#       func(*args, **kwargs)
#   return wrap_func

#write performance decorator that will tell how long it took for the function to execute
from time import time
def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        func(*args, **kwargs)
        t2 = time()
        print(f'Time taken {t2 - t1} s')
    return wrapper

@performance
def multiply_demo():
    for i in range(10000000):
        i**3

multiply_demo()