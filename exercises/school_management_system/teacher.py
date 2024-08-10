from validate_type import validate_type
from person import Person
from course import Course


class Teacher(Person):
    def __init__(
        self,
        name: str,
        age: int,
        address: str,
        teacher_id: str,
        courses: list[Course] = None,
    ) -> None:
        super().__init__(name, age, address)
        self.teacher_id = validate_type(teacher_id, str, "teacher_id")
        self.courses: list[Course] = courses or []

    def assign_course(self, course: Course) -> None:
        if course not in self.courses:
            self.courses.append(course)
        else:
            raise ValueError(
                f"Course {course.name} is already assigned to this teacher."
            )

    def list_courses(self) -> list[str]:
        return [course.name for course in self.courses]

    def __str__(self) -> str:
        return super().__str__()
