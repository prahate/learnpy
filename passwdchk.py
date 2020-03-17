username = input ("Enter username:")
password = input ("Enter password:")

pswd_hide = str('*' * len(password))
print (f'{username}, your password {pswd_hide} is {len(password)} letters long')