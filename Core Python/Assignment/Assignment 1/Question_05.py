# Write a program to enter P, T, R and calculate Compound Interest.

P = int(input('Enter amount of principle P :'))
R = int(input('Enter rate of interest R:'))
T = int(input('Enter time(year) T :'))

Amount = P*(1 + R/100)**T
CI = Amount - P

print('Compound Interest is :', CI)