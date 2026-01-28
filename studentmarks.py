name = input("Enter student name: ")

m1 = int(input("Enter Maths marks: "))
m2 = int(input("Enter Science marks: "))
m3 = int(input("Enter English marks: "))

total = m1 + m2 + m3
average = total / 3

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Average:", average)

if average >= 80:
    print("Grade: A")
elif average >= 60:
    print("Grade: B")
elif average >= 40:
    print("Grade: C")
else:
    print("Grade: Fail")