# Student Management OOP

A command-line Student Management System developed in Python using Object-Oriented Programming.

## Objective

Convert the previous Student Management CLI application into an OOP-based application using classes and objects.

## Features

* Add Student
* View Students
* Search Student
* Update Student
* Delete Student
* Student Details
* View Courses
* View Department Details
* Input Validation
* Exception Handling

## Classes

* `Person` – common information for people
* `Student` – manages student details and courses
* `Teacher` – manages teacher details and courses
* `Course` – manages course and enrolled students
* `Department` – manages courses and teachers

## OOP Concepts Used

* Class and Object
* Constructor
* Attributes and Methods
* Encapsulation
* Inheritance
* Composition
* Class Method
* Static Method

## Class Relationships

```text
Person
├── Student
└── Teacher

Department
└── Course
    └── Student
```

## Project Structure

```text
student-management-oop/
│
├── main.py
├── README.md
│
└── models/
    ├── __init__.py
    ├── person.py
    ├── student.py
    ├── teacher.py
    ├── course.py
    └── department.py
```

## How to Run

Open the terminal in the project folder and run:

```bash
python main.py
```

On Windows, you can also use:

```bash
py main.py
```

## Validation and Exception Handling

The application validates student ID, name, age, course information, and menu choices. `try` and `except` are used to handle invalid input without crashing the program.


