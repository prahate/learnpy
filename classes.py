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



player1 = PlayerCharacter('Harry', 29)
print(player1.name)
print(player1.age)
print(player1.membership)


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