class Student:
    def __init__(self, name: str, student_id: str) -> None:
        self.name = name
        self.student_id = student_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        if isinstance(name, str) and (len(name) > 0):
            self._name = name
        else:
            raise ValueError("Name must be a string and have at least one character")

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, id: str):
        if isinstance(id, str) and (len(id) > 0):
            self._student_id = id
        else:
            raise ValueError(
                "Student ID must be a string and have at least one character"
            )

    def __str__(self) -> str:
        return f"Name: {self.name} - ID: {self.student_id}"
