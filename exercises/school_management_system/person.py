from validate_type import validate_type


class Person:
    def __init__(self, name: str, age: int, address: str) -> None:
        self.name = validate_type(name, str, "name")
        self.age = validate_type(age, int, "age")
        self.address = validate_type(address, str, "address")

    def get_details(self):
        return f"Name: {self.name}\nAge: {self.age}\n From: {self.address}"

    def __str__(self) -> str:
        return self.get_details()
