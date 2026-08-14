# Enter number of students from user. For those many students accept marks of 5 subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.

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