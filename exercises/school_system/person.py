# Methods:

# get_info(self) -> str: Returns a string with the person's name and age.


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        if isinstance(name, str) and (len(name) > 2):
            self._name = name
        else:
            raise ValueError(
                "Name must be a string an have a length of at least two characters"
            )

    @property
    def age(self):
        return self._age

    @name.setter
    def age(self, age: int):
        if isinstance(age, int) and age > 4:
            self._age = age
        else:
            raise ValueError("Age must be a number and greater than 4")

    def __str__(self) -> str:
        return f"<{self.name}>"
