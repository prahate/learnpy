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

#class methods can be used to instantiate objects
#   @classmethod
#   def add_nums(cls, num1, num2):
#       return cls('Johnny', (num1 + num2))

# @staticmethod are similar to class methods except they dont have
# cls arguments
    @staticmethod
    def add_num2(num1, num2):
        return num1 + num2

# encapsulation
# binding of attributes and methods that manipulate data in object

#abstraction
# hiding information or only giving access to what is neccessary
# private and public variables
# python does not have private variables, only the syntax like appending the variable with '_' will signify to user that it is private variable

#inheritance
# inherit the properties of parent class

class User():
    def sign_in(self):
        print('Signed in')

class Archer(User):
    pass

class Wizard(User):
    pass

archer = Archer()
archer.sign_in()



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