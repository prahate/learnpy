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