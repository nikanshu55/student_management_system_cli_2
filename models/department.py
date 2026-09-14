class Department:
    # Store department details, courses, and teachers.

    def __init__(self, department_id, name):
        department_id = department_id.strip()
        name = name.strip()

        if not department_id:
            raise ValueError(
                "Department ID cannot be empty."
            )

        if not name:
            raise ValueError(
                "Department name cannot be empty."
            )

        self._department_id = department_id
        self._name = name

        self._courses = []
        self._teachers = []

    @property
    def department_id(self):
        return self._department_id

    @property
    def name(self):
        return self._name

    @property
    def courses(self):
        return self._courses.copy()

    @property
    def teachers(self):
        return self._teachers.copy()

    def add_course(self, course):
        # Add a course to the department.

        if course not in self._courses:
            self._courses.append(course)

    def add_teacher(self, teacher):
        # Add a teacher to the department.

        if teacher not in self._teachers:
            self._teachers.append(teacher)

    def find_course(self, course_id):
        # Find a course by ID.

        for course in self._courses:
            if course.course_id == course_id:
                return course

        return None

    def display_details(self):
        # Show the department details.

        print("\n--- Department Details ---")
        print(
            f"Department ID  : "
            f"{self._department_id}"
        )
        print(
            f"Department Name: "
            f"{self._name}"
        )

        print("\nCourses:")

        if self._courses:
            for course in self._courses:
                print(
                    f"  - {course.course_id} | "
                    f"{course.name}"
                )
        else:
            print("  No courses.")

        print("\nTeachers:")

        if self._teachers:
            for teacher in self._teachers:
                print(
                    f"  - {teacher.teacher_id} | "
                    f"{teacher.name}"
                )
        else:
            print("  No teachers.")