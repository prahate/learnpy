# Error handling
# in python try and except and else block is used for handling errors
# example below shows it
# we can also have finally block in try exception to break out
while(True):
    try:
        age = int(input('What is your age?'))
        10/age
        # we can raise our own exceptions using raise
        raise Exception('My own exception')
    except ValueError:
        print('please enter number')
    except ZeroDivisionError:
        print('Please enter valid age other than 0')
    else:
        print('Thank you')
        break
    finally:
        print('Done with everything')

def sum(num1, num2):
    try:
        return num1 + num2
    except (ValueError, ZeroDivisionError) as err:
        print(err)

print(sum(6, 2))