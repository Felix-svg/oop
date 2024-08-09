class Human:
    species = "Homo Sapiens"

    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if (type(age) in (int, float)) and (0 <= age <= 120):
            self._age = age
        else:
            raise ValueError("Age must be a number between 0 and 120")


felix = Human(25)