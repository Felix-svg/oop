from person import Person
from student import Student


# Methods:

# assign_grade(self, student: Student, grade: float): Assigns a grade to a student for the teacher's subject.
# get_subject(self) -> str: Returns the subject the teacher teaches.


class Teacher(Person):
    def __init__(self, name: str, age: int, teacher_id: str, subject: str) -> None:
        super().__init__(name, age)
        self.teacher_id = teacher_id
        self.subject = subject

    @property
    def teacher_id(self):
        return self._teacher_id

    @teacher_id.setter
    def teacher_id(self, id: str):
        if isinstance(id, str) and len(id) > 0:
            self._teacher_id = id
        else:
            raise ValueError("Teacher id must be a string")

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, subject: str):
        if isinstance(subject, str) and (len(subject) > 2):
            self._subject = subject
        else:
            raise ValueError(
                "Subject must be a string and have at least two characters"
            )

    def assign_grade(self, student: Student, grade: float):
        student.add_grade(self.subject, grade)

    def get_subject(self) -> str:
        return self.subject

    def __str__(self) -> str:
        return f"{self.name} teaches {self.subject}"


teacher = Teacher("Mwalimu", 45, "1", "Maths")
student = Student("Felix", 25, "1")
student.add_grade("English", 4.0)
student.add_grade("Science", 3.0)
student.add_grade("Maths", 5.0)

print(student.get_grades())
print(student.calculate_gpa())

print(teacher.get_subject())
print(teacher)

teacher.assign_grade(student, 4.6)
print(student.get_grades())
print(student.calculate_gpa())
