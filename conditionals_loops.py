# Conditionals
# if else
is_old = False
is_licensed = True

if is_old:
    print("You are old enough")
elif is_licensed:
    print("You are licensed to drive") 
else:
    print("You are not old enough")

# Ternery operator in python
# condition_if_true if condition else condition_if_else
is_friend = False;

can_mesage = "Messaging allowed" if is_friend else "Messaging Not Allowed"

print(can_mesage)

is_magician = True
is_expert = False

if (not is_magician):
    print("You need magic powers")
if (is_magician and is_expert):
    print("You are master magician")
if (is_magician and (not is_expert)):
    print("Atleast you are getting there")

# for Loop
# here items is similar to i
# and 'Hello world' cna be any iterable object
for items in 'Hello World':
    for i in [1,2]:
        print(items, i)

#for i in [1,2,3,4,5]:
#    print(i)