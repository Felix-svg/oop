from person import Person

# Methods:

# add_grade(self, subject: str, grade: float): Adds or updates a grade for a specific subject.
# calculate_gpa(self) -> float: Calculates and returns the student's Grade Point Average (GPA) or average grade.
# get_grades(self) -> dict: Returns a dictionary of all grades.


class Student(Person):
    def __init__(self, name: str, age: int, student_id: str, grades=None) -> None:
        super().__init__(name, age)
        self.student_id = student_id
        if grades is None:
            self.grades = {}
        else:
            if not isinstance(grades, dict):
                raise ValueError(
                    "Grades must be a dictionary with subjects as keys and grades as values."
                )
            self.grades = grades

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, id):
        if isinstance(id, str):
            self._student_id = id
        else:
            raise ValueError("Student id must be a string")

    def add_grade(self, subject: str, grade: float):
        if grade < 0.0 or grade > 5.0:
            raise ValueError("Grade must be between 0 and 5")
        self.grades[subject] = grade

    def calculate_gpa(self) -> float:
        if not self.grades:
            return 0.0
        total = 0
        for grades in self.grades.values():
            total += grades
        return total / len(self.grades)

    def get_grades(self) -> dict:
        return self.grades
