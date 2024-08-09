from vehicle import Vehicle


class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str, year: int, type: str) -> None:
        super().__init__(make, model, year)
        self.type = type

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type: str):
        if isinstance(type, str) and len(type) > 3:
            self._type = type
        else:
            raise ValueError("Type must be a string")

    def display_info(self) -> str:
        vehicle_info = super().display_info()
        return f"{vehicle_info}, Type: {self.type}"
