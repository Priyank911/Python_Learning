class Student:
    roll_number_counter = 1

    def __init__(self, name):
        self.name = name
        self.roll_number = Student.roll_number_counter
        Student.roll_number_counter += 1
        self.subjects = []

    def choose_subject(self, subject):
        if subject not in self.subjects:
            self.subjects.append(subject)

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print("Subjects Chosen:")
        for subject in self.subjects:
            print(f"- {subject}")


class SchoolManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self):
        name = input("Enter student name: ")
        student = Student(name)
        self.students.append(student)
        return student

    def choose_subject_for_student(self, student):
        subject = input("Enter subject name: ")
        student.choose_subject(subject)

    def display_all_students(self):
        print("\nAll Students:")
        for student in self.students:
            student.display_details()
            print()

# Main Program
school_system = SchoolManagementSystem()

while True:
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Choose Subject for a Student")
    print("3. Display All Students")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        student = school_system.add_student()
        print(f"{student.name} with Roll Number {student.roll_number} added successfully!")

    elif choice == '2':
        if school_system.students:
            roll_number = int(input("Enter the roll number of the student: "))
            student_found = None

            for student in school_system.students:
                if student.roll_number == roll_number:
                    student_found = student
                    break

            if student_found:
                school_system.choose_subject_for_student(student_found)
                print(f"Subject chosen for {student_found.name} successfully!")
            else:
                print("Student not found.")

        else:
            print("No students available. Please add a student first.")

    elif choice == '3':
        if school_system.students:
            school_system.display_all_students()
        else:
            print("No students available.")

    elif choice == '4':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
