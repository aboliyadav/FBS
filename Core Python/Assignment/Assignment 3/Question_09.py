# Input 5 subject marks from user and display grade(eg.First class,Second class ..)

S1 = float(input('Enter subject 1 marks :'))
S2 = float(input('Enter subject 2 marks :'))
S3 = float(input('Enter subject 3 marks :'))
S4 = float(input('Enter subject 4 marks :'))
S5 = float(input('Enter subject 5 marks :'))

percentage = (S1+S2+S3+S4+S5)/5

print("Percentage =", percentage)

if percentage >= 75:
    print("Distinction")
elif percentage >= 60:
    print("First Class")
elif percentage >= 50:
    print("Second Class")
elif percentage >= 35:
    print("Pass Class")
else:
    print("Fail")