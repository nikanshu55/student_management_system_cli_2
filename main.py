from models.student import Student
from models.teacher import Teacher
from models.course import Course
from models.department import Department


def create_department():
    # Create the starting department data.

    department = Department(
        "D001",
        "Computer Science"
    )

    # Create teachers
    teacher1 = Teacher(
        "T001",
        "Anita Sharma",
        35
    )

    teacher2 = Teacher(
        "T002",
        "Rohit Verma",
        38
    )

    # Create courses
    python_course = Course(
        "C001",
        "Python Programming",
        department
    )

    database_course = Course(
        "C002",
        "Database Management",
        department
    )

    # Add teachers to the department
    department.add_teacher(teacher1)
    department.add_teacher(teacher2)

    # Add courses to the department
    department.add_course(python_course)
    department.add_course(database_course)

    # Assign teachers to courses
    teacher1.assign_course(python_course)
    teacher2.assign_course(database_course)

    return department


def find_student(students, student_id):
    # Find a student by ID.

    for student in students:

        if student.student_id == student_id:
            return student

    return None


def add_student(students, department):

    print("\n--- Add Student ---")

    student_id_text = input(
        "Enter student ID: "
    ).strip()

    # Check the ID
    try:
        student_id = int(student_id_text)
    except ValueError:
        print("Student ID must be a positive number.")
        return

    if student_id <= 0:
        print("Student ID must be a positive number.")
        return

    # Check for duplicate IDs
    if find_student(students, student_id):
        print(
            "Duplicate student ID. "
            "Student already exists."
        )
        return

    # Get the name
    name = input(
        "Enter student name: "
    ).strip()

    if not name:
        print(
            "Student name cannot be empty."
        )
        return

    # Get the age
    try:
        age = int(
            input(
                "Enter student age: "
            ).strip()
        )

    except ValueError:
        print(
            "Invalid age. "
            "Please enter a number."
        )
        return

    if not Student.validate_age(age):
        print(
            "Age must be greater than 0."
        )
        return

    # Show the available courses
    print("\nAvailable Courses:")

    for course in department.courses:
        print(
            f"{course.course_id} - "
            f"{course.name}"
        )

    course_id = input(
        "Enter course ID: "
    ).strip()

    course = department.find_course(course_id)

    if course is None:
        print("Course not found.")
        return

    # Create the student
    try:
        student = Student(
            student_id,
            name,
            age
        )

    except ValueError as error:
        print(error)
        return

    # Enroll the student
    student.enroll(course)

    # Save the student
    students.append(student)

    print(
        "Student added successfully."
    )


def view_students(students):

    print("\n--- All Students ---")

    if not students:
        print("No students found.")
        return

    for student in students:

        print(
            f"ID: {student.student_id} | "
            f"Name: {student.name} | "
            f"Age: {student.age}"
        )


def search_student(students):

    print("\n--- Search Student ---")

    student_id = input(
        "Enter student ID: "
    ).strip()

    student = find_student(
        students,
        student_id
    )

    if student is None:
        print("Student not found.")
        return

    student.display_details()


def update_student(students):

    print("\n--- Update Student ---")

    student_id = input(
        "Enter student ID: "
    ).strip()

    student = find_student(
        students,
        student_id
    )

    if student is None:
        print("Student not found.")
        return

    print(
        "Press Enter to keep "
        "the current value."
    )

    new_name = input(
        f"Enter new name [{student.name}]: "
    ).strip()

    age_input = input(
        f"Enter new age [{student.age}]: "
    ).strip()

    new_age = None

    # Only check the age when one was entered
    if age_input:

        try:
            new_age = int(age_input)

        except ValueError:
            print(
                "Invalid age. "
                "Please enter a number."
            )
            return

    try:

        student.update_details(
            name=new_name
            if new_name
            else None,

            age=new_age
        )

    except ValueError as error:
        print(error)
        return

    print(
        "Student updated successfully."
    )


def delete_student(students):

    print("\n--- Delete Student ---")

    student_id = input(
        "Enter student ID: "
    ).strip()

    student = find_student(
        students,
        student_id
    )

    if student is None:
        print("Student not found.")
        return

    # Remove the student from their courses
    for course in student.courses:
        student.drop_course(course)

    # Remove the student from the list
    students.remove(student)

    print(
        "Student deleted successfully."
    )


def student_details(students):

    print("\n--- Student Details ---")

    student_id = input(
        "Enter student ID: "
    ).strip()

    student = find_student(
        students,
        student_id
    )

    if student is None:
        print("Student not found.")
        return

    student.display_details()


def view_courses(department):

    print("\n--- Courses ---")

    if not department.courses:
        print("No courses found.")
        return

    for course in department.courses:

        print(
            f"\nCourse ID   : "
            f"{course.course_id}"
        )

        print(
            f"Course Name : "
            f"{course.name}"
        )

        if course.teacher:
            print(
                f"Teacher     : "
                f"{course.teacher.name}"
            )

        else:
            print(
                "Teacher     : Not assigned"
            )

        print(
            f"Students    : "
            f"{len(course.students)}"
        )


def department_details(department):

    department.display_details()


def main():

    # Keep students in a list
    students = []

    # Set up the department
    department = create_department()

    while True:

        print("\n")
        print("=" * 50)
        print("       STUDENT MANAGEMENT SYSTEM")
        print("=" * 50)

        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Student Details")
        print("7. View Courses")
        print("8. Department Details")
        print("9. Exit")

        print("=" * 50)

        choice = input(
            "Enter your choice: "
        ).strip()

        if choice == "1":

            add_student(
                students,
                department
            )

        elif choice == "2":

            view_students(
                students
            )

        elif choice == "3":

            search_student(
                students
            )

        elif choice == "4":

            update_student(
                students
            )

        elif choice == "5":

            delete_student(
                students
            )

        elif choice == "6":

            student_details(
                students
            )

        elif choice == "7":

            view_courses(
                department
            )

        elif choice == "8":

            department_details(
                department
            )

        elif choice == "9":

            print(
                "\nThank you for using "
                "Student Management System."
            )

            break

        else:

            print(
                "Invalid choice. "
                "Please select 1-9."
            )


if __name__ == "__main__":
    main()