# Write a Program to input two angles from user and find third angle of the triangle.

A = int(input('Enter Angle 1 :'))
B = int(input('Enter Angle 2 :'))

C = 180 - (A + B)

print('Third angle of Triangle is :', C)
