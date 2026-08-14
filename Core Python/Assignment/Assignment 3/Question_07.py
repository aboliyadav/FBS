# Write a program to check if user has entered correct userid and password.

userid = input('Enter userid :')
Password = input('Enter password :')

if userid == 'admin' and Password == '1234':
    print('login successful .')
else:
    print('Invalid userid and password .')    