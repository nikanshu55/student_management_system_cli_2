from .person import Person


class Teacher(Person):
    # Store teacher details and assigned courses.

    def __init__(self, teacher_id, name, age):
        teacher_id = teacher_id.strip()
        name = name.strip()

        if not teacher_id:
            raise ValueError("Teacher ID cannot be empty.")

        if not name:
            raise ValueError("Teacher name cannot be empty.")

        if not self.validate_age(age):
            raise ValueError("Age must be greater than 0.")

        super().__init__(name, age)

        self._teacher_id = teacher_id
        self._courses = []

    @property
    def teacher_id(self):
        return self._teacher_id

    @property
    def courses(self):
        return self._courses.copy()

    def assign_course(self, course):
        # Assign a course to the teacher.

        if course not in self._courses:
            self._courses.append(course)

        course._set_teacher(self)

    def display_details(self):
        # Show the teacher details.

        print("\n--- Teacher Details ---")
        print(f"Teacher ID : {self._teacher_id}")
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
            print("Courses    : No course assigned")