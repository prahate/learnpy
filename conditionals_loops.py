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