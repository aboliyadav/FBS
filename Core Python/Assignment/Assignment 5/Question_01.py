# Write a program to prompt user to enter userid and password. If Id and password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.
Correct_id = 'Admin'
Correct_Password = '1234'

for i in range(3):
    userid = input('Enter userID :')
    Password = input('Enter password:')
    
    if userid == Correct_id and Password == Correct_Password :
        print('Login Successful')
        break
    else:
        print('Incorrect UserID or Password')

else:
    print('You have exceeded 3 attempts program terminated.')        