from vehicle import Vehicle
from validate_type import validate_type


class Customer:
    def __init__(self, customer_id: str, name: str, rented_vehicles=None) -> None:
        self.customer_id = validate_type(customer_id, str, "customer_id")
        self.name = validate_type(name, str, "name")
        self.rented_vehicles = rented_vehicles or []


    def rent_vehicle(self, vehicle: Vehicle) -> None:
        self.rented_vehicles.append(vehicle)

    def return_vehicle(self, vehicle: Vehicle) -> None:
        if vehicle in self.rented_vehicles:
            self.rented_vehicles.remove(vehicle)
            vehicle.return_vehicle()

    def __str__(self) -> str:
        rented = ", ".join([str(v) for v in self.rented_vehicles])
        return f"Customer: {self.name}\nRented Vehicles: [{rented}]"
