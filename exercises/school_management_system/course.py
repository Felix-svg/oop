from typing import TYPE_CHECKING, List
from validate_type import validate_type
if TYPE_CHECKING:
    from teacher import Teacher
    from student import Student



class Course:
    def __init__(
        self,
        course_id: str,
        name: str,
        teacher: 'Teacher',
        students: List['Student'] = None,
    ) -> None:
        self.course_id = validate_type(course_id, str, "course_id")
        self.name = validate_type(name, str, "name")
        self.teacher = validate_type(teacher, Teacher, "teacher")
        self.students: List['Student'] = students or []

    def add_student(self, student: 'Student') -> None:
        if student not in self.students:
            self.students.append(student)
        else:
            raise ValueError(
                f"Student {student.name} is already enrolled in the course {self.name}."
            )

    def list_students(self) -> list[str]:
        students = [str(student) for student in self.students]
        return "\n".join(students)

    def __str__(self) -> str:
        students = ", ".join([student.name for student in self.students])
        return f"Course ID: {self.course_id}\nCourse Name: {self.name}\nTeacher: {self.teacher.name}\nEnrolled Students: {students if students else 'None'}"


from teacher import Teacher

mwalimu = Teacher("Mwalimu", 30, "123 Main St", "T01")
software_engineering = Course("1", "Software Engineering", mwalimu)
mwalimu.assign_course(software_engineering)

for course in mwalimu.courses:
    print(course.name)
