# Write a program to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4)

n = int(input("Enter a number: "))

temp = n
arm = 0

while temp > 0:
    digit = temp % 10
    arm = arm + digit ** 3
    temp = temp // 10

if arm == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")