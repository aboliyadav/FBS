x = 10 
# Immutable -Reuse 
y = 10 
z = 20 
li1 = [10 ,20 ]
# Mutable-New memory 
# allocated 
li2 = [10 ,20 ]

print(id(x))
print(id(y))
print(x is y)
print(x is z)

print(id(li1))
print(id(li2))
