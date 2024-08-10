from vehicle import Vehicle


class Customer:
    def __init__(self, customer_id: str, name: str, rented_vehicles=None) -> None:
        self.customer_id = customer_id
        self.name = name
        if rented_vehicles is None:
            self.rented_vehicles = []
        else:
            self.rented_vehicles = rented_vehicles

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, id: str):
        if not isinstance(id, str):
            raise ValueError("customer_id must be a string")
        else:
            self._customer_id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        if not isinstance(name, str):
            raise ValueError("name must be a string")
        else:
            self._name = name


    def rent_vehicle(self, vehicle: Vehicle) -> None:
        self.rented_vehicles.append(vehicle)

    def return_vehicle(self, vehicle: Vehicle) -> None:
        if vehicle in self.rented_vehicles:
            self.rented_vehicles.remove(vehicle)
            vehicle.return_vehicle()

    def __str__(self) -> str:
        rented = ", ".join([str(v) for v in self.rented_vehicles])
        return f"Customer: {self.name}\nRented Vehicles: [{rented}]"
