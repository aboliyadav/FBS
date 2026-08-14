# Write a program to calculate the percentage of student based on marks of any 5 subjects.

Marathi = int(input(' Marathi Subject marks 1 :'))
History = int(input(' History Subject marks 2 :'))
Math  = int(input(' Math Subject marks 3 :'))
Hindi  = int(input(' Hindi Subject marks 4 :'))
Geography = int(input(' Geography Subject marks 5 :'))

Total = Marathi + History + Math + Hindi + Geography
percentage = (Total/500)*100

print('percentage of students is :' , percentage)