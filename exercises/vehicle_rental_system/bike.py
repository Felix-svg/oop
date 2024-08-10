from vehicle import Vehicle
from validate_type import validate_type


class Bike(Vehicle):
    def __init__(
        self,
        vehicle_id: str,
        make: str,
        model: str,
        rental_rate: float,
        is_rented: bool,
        type: str,
    ) -> None:
        super().__init__(vehicle_id, make, model, rental_rate, is_rented)
        self.type = validate_type(type, str, "type")

    def get_details(self) -> str:
        return f"Make: {self.make}\nModel: {self.model}\nRental Rate: {self.rental_rate}\nType: {self.type}"

    def __str__(self) -> str:
        return f"{super().__str__()}, Type: {self.type}"
