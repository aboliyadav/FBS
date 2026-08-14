# with passing parameter (with input)
# with returning value (with output)



def addition(num1 ,num2):
    add = num1 + num2
    
    return add 

num1 = int(input('Enter number 1:'))
num2 = int(input('Enter number 2:'))

res = addition(num1 ,num2)
print('Addition:', res)