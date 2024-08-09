from vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, make: str, model: str, year: int, number_of_doors: int) -> None:
        super().__init__(make, model, year)
        self.number_of_doors = number_of_doors

    @property
    def number_of_doors(self):
        return self._number_of_doors

    @number_of_doors.setter
    def doors(self, doors: int):
        if isinstance(doors, int) and doors > 0:
            self._number_of_doors = doors
        else:
            raise ValueError("Number of doors must be an integer and greater than zero")

    def display_info(self) -> str:
        vehicle_info = super().display_info()
        return f"{vehicle_info}, No. of Doors: {self.number_of_doors}"
