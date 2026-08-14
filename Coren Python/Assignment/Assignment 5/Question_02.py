n = int(input("Enter number of students: "))

total_percentage = 0

for i in range(n):
    print("Student", i + 1)

    s1 = float(input("Enter marks of Subject 1: "))
    s2 = float(input("Enter marks of Subject 2: "))
    s3 = float(input("Enter marks of Subject 3: "))
    s4 = float(input("Enter marks of Subject 4: "))
    s5 = float(input("Enter marks of Subject 5: "))

    percentage = (s1 + s2 + s3 + s4 + s5) / 5

    print("Percentage =", percentage, "%")

    total_percentage = total_percentage + percentage

average = total_percentage / n

print("Average Percentage =", average, "%")