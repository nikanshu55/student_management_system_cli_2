from .person import Person


class Student(Person):
    # Store student details and courses.

    def __init__(self, student_id, name, age):
        name = name.strip()

        if type(student_id) is not int or student_id <= 0:
            raise ValueError("Student ID must be a positive number.")

        if not name:
            raise ValueError("Student name cannot be empty.")

        if not self.validate_age(age):
            raise ValueError("Age must be greater than 0.")

        # Set the common person details
        super().__init__(name, age)

        self._student_id = student_id
        self._courses = []

    @classmethod
    def from_string(cls, data):
        # Create a student from text.

        parts = data.split(",")

        if len(parts) != 3:
            raise ValueError(
                "Invalid format. Use: ID,Name,Age"
            )

        student_id_text = parts[0].strip()
        name = parts[1].strip()
        age_text = parts[2].strip()

        try:
            student_id = int(student_id_text)
            age = int(age_text)
        except ValueError:
            raise ValueError(
                "Student ID and age must be numbers."
            )

        return cls(student_id, name, age)

    @property
    def student_id(self):
        return self._student_id

    @property
    def courses(self):
        # Return the student's courses.
        return self._courses.copy()

    def enroll(self, course):
        # Enroll the student in a course.
        if course not in self._courses:
            self._courses.append(course)

        course._add_student(self)

    def drop_course(self, course):
        # Remove the student from a course.
        if course in self._courses:
            self._courses.remove(course)

        course._remove_student(self)

    def update_details(self, name=None, age=None):
        # Update the student's details.

        if name is not None:
            name = name.strip()

            if not name:
                raise ValueError(
                    "Student name cannot be empty."
                )

            self._name = name

        if age is not None:
            if not self.validate_age(age):
                raise ValueError(
                    "Age must be greater than 0."
                )

            self._age = age

    def display_details(self):
        # Show the student's details.

        print("\n--- Student Details ---")
        print(f"Student ID : {self._student_id}")
        print(f"Name       : {self._name}")
        print(f"Age        : {self._age}")

        if self._courses:
            print("Courses    :")

            for course in self._courses:
                print(
                    f"  - {course.course_id} | "
                    f"{course.name}"
                )
        else:
            print("Courses    : No course enrolled")