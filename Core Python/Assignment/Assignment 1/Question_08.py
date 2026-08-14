# Write a program to convert days into years, weeks and days.

Days = int(input('Enter the value of Days :'))

Years = Days // 365
Days = Days % 365 
Weeks = Days // 7
Days = Days % 7

print('Years ,Weeks and Days is :', Years , Weeks  , Days)