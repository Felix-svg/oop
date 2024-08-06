# used in class methods where there are multiple classes with the same method name
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        return "Move!"


class Car(Vehicle):
    pass


class Boat(Vehicle):
    def move(self):
        return "Sail!"


class Plane(Vehicle):
    def move(self):
        return "Fly!"


car = Car("Ford", "Mustang")
boat = Boat("Ibiza", "Touring 20")
plane = Plane("Boeing", "747")


# polymorphism allows us to execute the same method for all classes.
for vehicle in car, boat, plane:
    print(vehicle.brand)
    print(vehicle.model)
    print(vehicle.move())
