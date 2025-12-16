# Creating a dictionary with student names as keys and their marks as values
student_marks = {"Alice": 85, "Rohan": 90, "Sonam": 78, "David": 92}

# Asking the user to input a student's name
name = input("Enter the student's name: ")

# Checking if the student exists in the dictionary
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found.")
