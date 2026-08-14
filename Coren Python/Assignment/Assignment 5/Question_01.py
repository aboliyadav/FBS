Correct_id ='admin'
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