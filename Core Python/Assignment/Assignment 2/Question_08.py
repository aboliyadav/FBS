# Write a program to swap two numbers using third variable.

a = int(input('Enter First number :'))
b = int(input('Enter Second number :'))

temp = a
a = b 
b = temp 

print('After Swapping')
print('a:',a)
print('b:',b)