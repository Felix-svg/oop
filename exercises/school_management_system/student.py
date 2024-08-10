from validate_type import validate_type
from person import Person
from course import Course


class Student(Person):
    def __init__(
        self,
        name: str,
        age: int,
        address: str,
        student_id: str,
        courses: list[Course] = None,
    ) -> None:
        super().__init__(name, age, address)
        self.student_id = validate_type(student_id, str, "student_id")
        self.courses:list[Course] = courses or []

    def enroll(self, course: Course) -> None:
        self.courses.append(course)

    def list_courses(self) -> list[str]:
        return [course.name for course in self.courses]

    def __str__(self) -> str:
        return super().__str__()
