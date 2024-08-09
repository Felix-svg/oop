from shape import Shape


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        super().__init__()
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * ((self.width) + (self.height))
    
    def __str__(self):
        return f"Rectangle with width {self.width} and height {self.height} has area {self.area()} and perimeter {self.perimeter()}"

    


rectangle = Rectangle(2.0,3.0)
print(rectangle.area())
print(rectangle.perimeter())
print(rectangle)
