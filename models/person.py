class Person:
    # Store common person details.

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @staticmethod
    def validate_age(age):
        # Check whether the age is valid.
        return isinstance(age, int) and age > 0

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    def update_name(self, name):
        # Update the person's name.
        name = name.strip()

        if not name:
            raise ValueError("Name cannot be empty.")

        self._name = name

    def display_info(self):
        # Show the person's details.
        print(f"Name: {self._name}")
        print(f"Age: {self._age}")