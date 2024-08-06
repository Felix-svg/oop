# inheritance

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Employee(Person):
    def __init__(self, first_name, last_name, age, salary, employment_year):
        super().__init__(first_name, last_name)
        self.age = age
        self.salary = salary
        self.employment_year = employment_year

    def employee(self):
        return f"{self.first_name} {self.last_name} joined this organization in the year {self.employment_year}, and earns a salary of Ksh.{self.salary}."


felix = Employee(
    first_name="John", last_name="Doe", age=30, salary=410000, employment_year=2020
)
print(felix.employee())
