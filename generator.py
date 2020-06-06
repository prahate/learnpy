#generators in python
# generate sequence of values over time
# generators use special keyward in python called yield 
# generators are iterables
# but not all iterales are generators
# is a generator --range(100) it gives 100 values without storing them in memory, ie. values are generated in real time one by one
# list(range(100)) --  is not generator, it creates memory for holding 100 values

#writing generator function
def generator_func(num):
    for i in range(num):
        yield i # yield pauses the function and waits for next to resume

#for item in generator_func(1000):
#    print(item)

g = generator_func(100)
print(g)    # prints object
print(next(g))  #prints 0
print(next(g))  #prints 1

#for loop using generators
def special_for(iterable):
    iterator = iter(iterable)

    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break

special_for([1,2,3,5])

def fib(num):
    a =0
    b =1
    for i in range(num):
        yield a
        temp =a
        a = b
        b = temp + b

for x in fib(20):
    print(x)