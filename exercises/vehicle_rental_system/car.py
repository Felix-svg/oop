from vehicle import Vehicle
from validate_type import validate_type


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
        self.num_doors = validate_type(num_doors, int, "num_doors")

    def get_details(self) -> str:
        return f"Make: {self.make}\nModel: {self.model}\nRental Rate: {self.rental_rate}\nDoors = {self._num_doors}"

    def __str__(self) -> str:
        return f"{super().__str__()}, Doors: {self.num_doors}"
