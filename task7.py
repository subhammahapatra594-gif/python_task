# Store all student records
students = []

# Number of students
n = int(input("Enter number of students: "))

for i in range(n):
    # Create a student record
    student = {}

    student["Name"] = input("Enter Name: ")
    student["Roll No"] = input("Enter Roll No: ")
    student["Branch"] = input("Enter Branch: ")
    student["Marks"] = int(input("Enter Marks: "))

    # Add record to list
    students.append(student)

# Display records
print("\nStudent Records")

for student in students:
    print(student)