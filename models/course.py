class Course:
    # Store course details and enrolled students.

    def __init__(self, course_id, name, department):
        course_id = course_id.strip()
        name = name.strip()

        if not course_id:
            raise ValueError("Course ID cannot be empty.")

        if not name:
            raise ValueError("Course name cannot be empty.")

        self._course_id = course_id
        self._name = name
        self._department = department

        self._teacher = None
        self._students = []

    @property
    def course_id(self):
        return self._course_id

    @property
    def name(self):
        return self._name

    @property
    def department(self):
        return self._department

    @property
    def teacher(self):
        return self._teacher

    @property
    def students(self):
        return self._students.copy()

    def _add_student(self, student):
        # Add a student to the course.

        if student not in self._students:
            self._students.append(student)

    def _remove_student(self, student):
        # Remove a student from the course.

        if student in self._students:
            self._students.remove(student)

    def _set_teacher(self, teacher):
        # Set the teacher for the course.

        self._teacher = teacher

        if self not in teacher._courses:
            teacher._courses.append(self)

    def display_details(self):
        # Show the course details.

        print("\n--- Course Details ---")
        print(f"Course ID  : {self._course_id}")
        print(f"Course Name: {self._name}")
        print(
            f"Department : {self._department.name}"
        )

        if self._teacher:
            print(
                f"Teacher    : {self._teacher.name}"
            )
        else:
            print("Teacher    : Not assigned")

        print("Students   :")

        if self._students:
            for student in self._students:
                print(
                    f"  - {student.student_id} | "
                    f"{student.name}"
                )
        else:
            print("  No students enrolled")