# the __init__.py method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person(name="Jon", age=40)
print(person1.age)
print(person1.name)