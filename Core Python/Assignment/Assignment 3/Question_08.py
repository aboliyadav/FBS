import random

userid = input("Enter User ID: ")
password = input("Enter Password: ")

if userid == "admin" and password == "1234":
    num = random.randint(1000, 9999)
    print("Your captcha number is:", num)

    captcha = int(input("Enter the captcha number: "))

    if captcha == num:
        print("Login Successful")
    else:
        print("Captcha Failed")
else:
    print("Invalid User ID or Password")