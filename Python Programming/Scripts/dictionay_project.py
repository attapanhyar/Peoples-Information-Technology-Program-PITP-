# "Student Grade Management System".
# Project Objective:
# The goal is to create a system where users (teachers) can add, update, delete,
# and view student grades. The program will allow managing grades for multiple 
# students and display average, highest, and lowest grades.


grades = {}

# Function to add a student and their grade
def add_student(name, grade):
    grades[name] = grade
    print(f"{name} has been added with grade {grade}.")

# Function to update an existing student's grade
def update_student(name, grade):
    if name in grades:
        grades[name] = grade
        print(f"{name}'s grade has been updated to {grade}.")
    else:
        print(f"Student {name} not found.")

# Function to delete a student
def delete_student(name):
    if name in grades:
        del grades[name]
        print(f"Student {name} has been removed.")
    else:
        print(f"Student {name} not found.")

# Function to display all students and their grades
def display_students():
    if not grades:
        print("No students found.")
    else:
        for name, grade in grades.items():
            print(f"{name}: {grade}")

# Function to calculate and display average, highest, and lowest grades
def display_statistics():
    if not grades:
        print("No student data to show statistics.")
    else:
        all_grades = list(grades.values())
        avg_grade = sum(all_grades) / len(all_grades)
        highest_grade = max(all_grades)
        lowest_grade = min(all_grades)
        print(f"Average Grade: {avg_grade:.2f}")
        print(f"Highest Grade: {highest_grade}")
        print(f"Lowest Grade: {lowest_grade}")

# Main menu function
def main_menu():
    while True:
        print("\n--- Student Grade Management System ---")
        print("1. Add a student")
        print("2. Update a student's grade")
        print("3. Delete a student")
        print("4. Display all students and grades")
        print("5. Display grade statistics")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter student's name: ")
            grade = float(input(f"Enter grade for {name}: "))
            add_student(name, grade)

        elif choice == '2':
            name = input("Enter the student's name to update: ")
            grade = float(input(f"Enter the new grade for {name}: "))
            update_student(name, grade)

        elif choice == '3':
            name = input("Enter the student's name to delete: ")
            delete_student(name)

        elif choice == '4':
            print("\n--- Student List ---")
            display_students()

        elif choice == '5':
            print("\n--- Grade Statistics ---")
            display_statistics()

        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

# Start the system
main_menu()
