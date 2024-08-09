from shape import Shape
import math


class Circle(Shape):
    def __init__(self, radius:float) -> None:
        super().__init__()
        self.radius = radius

    def area(self):
        return math.pi * (self.radius * self.radius)

    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def __str__(self):
        return f"Circle with radius {self.radius} has area {self.area()} and perimeter {self.perimeter()}"
    

circle = Circle(7.0)
print(circle.area())
print(circle.perimeter())
print(circle)
