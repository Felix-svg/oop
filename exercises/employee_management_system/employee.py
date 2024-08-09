class Employee:
    def __init__(self, name: str, age: int, salary: float, position: str):
        self.name = name
        self.age = age
        self.salary = salary
        self.position = position

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
    def age(self):
        return self._age

    @age.setter
    def age(self, age: int):
        if isinstance(age, int) and age > 17:
            self._age = age
        else:
            raise ValueError("Age must be an integer and at least 18")

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary: float):
        if isinstance(salary, float) and salary > 10000:
            self._salary = salary
        else:
            raise ValueError("Salary must be a float and reater than 10000")

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position: str):
        if isinstance(position, str) and position is not None:
            self._position = position
        else:
            raise ValueError("Position must be provided")

    def __str__(self):
        return f"Employee Name: {self.name} \n\t Age: {self.age} \n\t Salary: {self.salary} \n\t Position: {self.position}"
