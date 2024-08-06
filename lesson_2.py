# the __init__.py method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old."
    
    def my_func(self):
        return f"Hello, my name is {self.name}"

person1 = Person(name="Jon", age=40)
print(person1.age)
print(person1.name)
person1.my_func()

#modify object properties
person1.age = 20
del person1.age # the del keyword deletes an object property