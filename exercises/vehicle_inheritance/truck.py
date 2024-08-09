from vehicle import Vehicle


class Truck(Vehicle):
    def __init__(
        self, make: str, model: str, year: int, payload_capacity: float
    ) -> None:
        super().__init__(make, model, year)
        self.payload_capacity = payload_capacity

    @property
    def payload_capacity(self):
        return self._payload_capacity

    @payload_capacity.setter
    def type(self, payload_capacity: float):
        if isinstance(payload_capacity, float) and payload_capacity > 0:
            self._payload_capacity = payload_capacity
        else:
            raise ValueError("Payload must be a float and greater than zero")

    def display_info(self) -> str:
        vehicle_info = super().display_info()
        return f"{vehicle_info}, Payload Capacity: {self.payload_capacity} tons"
