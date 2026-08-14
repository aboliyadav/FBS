# Write a program to check if given 3 digit number is a palindrome or not.

num = int(input("Enter a 3 digit number: "))

a = num // 100
b = (num // 10) % 10
c = num % 10

if a == c:
    print("Palindrome number")
else:
    print("Not a palindrome number")