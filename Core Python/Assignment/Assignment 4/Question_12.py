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