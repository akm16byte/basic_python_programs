#1.Grade Checker

# Grade Checker Program

# Take score input from the user
score = int(input("Enter the score: "))

# Determine the grade based on the score
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# Display the result
print("Your Grade:", grade)

#2.Student Grades
# Simple Student Grades Program
student_grades = {}
# Add a student
name = input("Enter student name: ")
grade = input("Enter grade: ")
student_grades[name] = grade
# Update a student
update_name = input("Enter name to update grade: ")
if update_name in student_grades:
    new_grade = input("Enter new grade: ")
    student_grades[update_name] = new_grade
else:
    print("Student not found.")
# Print all grades
print("\nAll Student Grades:")
for student, grade in student_grades.items():
    print(student, ":", grade)
#3.Write to a File
# Open a file in write mode (this creates the file if it doesn't exist)
file = open("my_notes.txt", "w")
# Write content to the file
file.write("Hello! This is my first file.\n")
file.write("I'm learning how to write to files in Python.\n")
# Always close the file after writing
file.close()
print("Content written to 'my_notes.txt' successfully.")

#4.Read from a File
# Open the file in read mode
file = open("my_notes.txt", "r")

# Read the entire content of the file
content = file.read()

# Print the content to the screen
print("File Content:\n")
print(content)

# Close the file
file.close()
