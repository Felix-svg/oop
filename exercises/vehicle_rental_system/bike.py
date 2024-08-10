from vehicle import Vehicle


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
        self.type = type

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type:str):
        if not isinstance(type, str):
            raise ValueError("type must be a string")
        else:
            self._type = type

    def get_details(self) -> str:
        return f'Make: {self.make}\nModel: {self.model}\nRental Rate: {self.rental_rate}\nType: {self.type}'

    def __str__(self) -> str:
        return f"{super().__str__()}, Type: {self.type}"
