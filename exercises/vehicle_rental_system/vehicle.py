from validate_type import validate_type


class Vehicle:
    def __init__(
        self,
        vehicle_id: str,
        make: str,
        model: str,
        rental_rate: float,
        is_rented: bool,
    ) -> None:
        self.vehicle_id = validate_type(vehicle_id, str, "vehicle_id")
        self.make = validate_type(make, str, "make")
        self.model = validate_type(model, str, "model")
        self.rental_rate = validate_type(rental_rate, float, "rental_rate")
        self.is_rented = validate_type(is_rented, bool, "is_rented")

    def rent_vehicle(self) -> None:
        self.is_rented = True

    def return_vehicle(self) -> None:
        self.is_rented = False

    def __str__(self) -> str:
        return f"{self.make} {self.model} - Daily Rate: {self.rental_rate}, Rented: {self.is_rented}"
