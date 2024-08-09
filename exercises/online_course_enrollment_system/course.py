from student import Student


class Course:
    def __init__(
        self,
        course_name: str,
        course_code: str,
        max_students: int,
        students_enrolled=None,
    ) -> None:
        self.course_name = course_name
        self.course_code = course_code
        self.max_students = max_students
        if students_enrolled is None:
            self.students_enrolled = []
        else:
            self.students_enrolled = students_enrolled

    @property
    def course_name(self):
        return self._course_name

    @course_name.setter
    def course_name(self, name: str):
        if isinstance(name, str) and (len(name) > 0):
            self._course_name = name
        else:
            raise ValueError(
                "Course name must be a string and have at least one character"
            )

    @property
    def course_code(self):
        return self._course_code

    @course_code.setter
    def course_code(self, code: str):
        if isinstance(code, str) and (len(code) > 0):
            self._course_code = code
        else:
            raise ValueError(
                "Course code must be a string and have at least one character"
            )

    @property
    def max_students(self):
        return self._max_students

    @max_students.setter
    def max_students(self, students: int):
        if isinstance(students, int) and students >= 0:
            self._max_students = students
        else:
            raise ValueError("Max students must be a number and at leat zero")

    # enrolls a student if there is space.
    def enroll_student(self, student: Student):
        self.students_enrolled.append(student)

    # removes a student by ID.
    def remove_student(self, student_id: str):
        self.students_enrolled = [
            student
            for student in self.enroll_student
            if student.student_id != student_id
        ]

    # prints all enrolled students.
    def list_students(self):
        students = [str(student) for student in self.students_enrolled]
        return "\n".join(students)

    def __str__(self) -> str:
        return f"Course Name: {self.course_name} - {self.course_code} \nStudents Enrolled: {self.list_students()}"


student1 = Student("Jon", "1")
student2 = Student("Jane", "2")
student3 = Student("Smith", "3")
student4 = Student("Rose", "4")
student5 = Student("Peter", "5")
course1 = Course("Software Engineering", "101", 30)
course2 = Course("Data Science", "102", 25)

course1.enroll_student(student1)
course1.enroll_student(student4)
course1.enroll_student(student2)
course2.enroll_student(student5)
course2.enroll_student(student3)

print(course1.list_students())
print(course2.list_students())
print(course2)