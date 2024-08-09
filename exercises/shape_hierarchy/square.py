from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_length: float) -> None:
        super().__init__(side_length, side_length)

    def __str__(self):
        return f"Square with side length {self.width} has area {self.area()} and perimeter {self.perimeter()}"
    


square = Square(4)
print(square.perimeter())
print(square.area())
print(square)
        
