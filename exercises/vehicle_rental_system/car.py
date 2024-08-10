from vehicle import Vehicle


class Car(Vehicle):
    def __init__(
        self,
        vehicle_id: str,
        make: str,
        model: str,
        rental_rate: float,
        is_rented: bool,
        num_doors: int,
    ) -> None:
        super().__init__(vehicle_id, make, model, rental_rate, is_rented)
        self.num_doors = num_doors

    @property
    def num_doors(self):
        return self._num_doors

    @num_doors.setter
    def num_doors(self, doors: int):
        if not isinstance(doors, int):
            raise ValueError("num_doors must be a number")
        else:
            self._num_doors = doors

    # Returns the make, model, rental rate, and number of doors.
    def get_details(self) -> str:
        return f"Make: {self.make}\nModel: {self.model}\nRental Rate: {self.rental_rate}\nDoors = {self._num_doors}"

    def __str__(self) -> str:
        return f"{super().__str__()}, Doors: {self.num_doors}"
