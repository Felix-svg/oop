from employee import Employee


class Manager(Employee):
    def __init__(self, name: str, age: int, salary: float, position: str, team=None):
        super().__init__(name, age, salary, position)
        if team is None:
            self.team = []
        else:
            self.team = team

    def add_team_member(self, employee: Employee):
        self.team.append(employee)

    def remove_team_member(self, employee_name: str):
        self.team = [
            employee for employee in self.team if employee.name != employee_name
        ]

    def display_team(self):
        team = [str(employee) for employee in self.team]
        if not self.team:
            return "No team members available"
        return "\n".join(team)

    def __str__(self):
        return f"Manager Name: {self.name} \n\t Age: {self.age} \n\t Salary: {self.salary} \n\t Position: {self.position} \n\t Team Members:\n{self.display_team()}"


employee1 = Employee("Jon Doe", 28, 50000.0, "Employee")
employee2 = Employee("Jane Doe", 30, 55000.0, "Employee")
manager = Manager("Smith", 40, 110000.0, "Manager")
manager.add_team_member(employee1)
manager.add_team_member(employee2)
manager.remove_team_member(employee2.name)
# print(manager.display_team())
print(manager)
