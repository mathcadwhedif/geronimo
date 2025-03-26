

import random as rnd  

students = []

# Class to store the student information
class Student:
    def __init__(self, name, age, grade, marks):
        self.name = name
        self.age = age
        self.grade = grade
        self.marks = marks

    # Method to check if student passed or no
    def has_passed(self):
        return self.marks >= 50  # 'return' keyword

# Function to get student details
def get_student_info():
    global students  # Using 'global'
    
    while True:  # 'while' loop
        try:  # 'try' block for exception handling
            name = input("Enter Student Name: ")
            age = int(input("Enter Age: "))
            
            # Using 'assert' to ensure valid age
            assert age > 0, "Age must be positive!"
            
            grade = input("Enter Grade (A/B/C/D/F): ").upper()
            marks = float(input("Enter Marks: "))
            
            # Using 'lambda' function to determine pass/fail
            check_grade = lambda m: "Pass" if m >= 50 else "Fail"
            
            # Create a Student object
            student = Student(name, age, grade, marks)
            
            # Append to global list
            students.append(student)

            # Using 'if', 'elif', and 'else' for decision making
            if marks >= 90:
                print("Excellent work!")
            elif marks >= 75:
                print("Good job!")
            else:
                print("Keep improving!")

            print(f"Result: {check_grade(marks)}")

            # 'break' to exit loop
            more = input("Add another student? (yes/no): ").strip().lower()
            if more != 'yes':
                break

        except ValueError:  # Handling invalid input
            print("Invalid input! Please enter correct values.")
        except AssertionError as error:  # Using 'as' for exception aliasing
            print("Error:", error)
        finally:  # 'finally' block to ensure message is displayed
            print("Processing next student...\n")

# Function to display students
def display_students():
    if not students:  # Using 'not'
        print("No students found!")
        return

    print("\n--- Student Information ---")
    for idx, student in enumerate(students, start=1):
        print(f"{idx}. Name: {student.name}, Age: {student.age}, Grade: {student.grade}, Marks: {student.marks}")

# Function to delete a student
def delete_student():
    global students
    name = input("Enter student name to delete: ")

    for student in students:
        if student.name == name:  # Using 'is'
            students.remove(student)
            print(f"Student {name} removed.")
            break
    else:
        print("Student not found!")

# Function using 'yield' to generate student marks
def marks_generator():
    for student in students:
        yield student.marks  # Using 'yield' to return values one at a time

# Function using 'with' for file handling
def save_students_to_file():
    with open("students.txt", "w") as file:
        for student in students:
            file.write(f"Name : {student.name}, Age: {student.age}, Grade: {student.grade}, Marks: {student.marks}\n")
    print("Student data saved!")

# Function to demonstrate 'nonlocal' keyword
def counter_demo():
    count = 0
    def increment():
        nonlocal count  # Using 'nonlocal' inside nested function
        count += 1
        return count
    return increment()

# Main function
def main():
    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Delete Student")
        print("4. Save to File")
        print("5. Show Marks (Using Generator)")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            get_student_info()
        elif choice == "2":
            display_students()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            save_students_to_file()
        elif choice == "5":
            print("Marks List:", list(marks_generator()))
        elif choice == "6":
            print("Exiting program...")
            break  # Exit loop
        else:
            print("Invalid choice. Try again.")

# Run the program
if __name__ == "__main__":
    main()
