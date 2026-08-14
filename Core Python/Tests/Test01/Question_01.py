import math

length = int(input('Enter the length:'))
breadth = int(input('Enter the breadth:' ))
radius = int(input('Enter the breadth:' ))

area = (length*breadth)+(math.pi*radius * radius/2)
perimeter = (2*length)+breadth+(math.pi*radius)


print('Area:',area )
print('Perimeter:',perimeter)
