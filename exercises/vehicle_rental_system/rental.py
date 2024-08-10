from customer import Customer
from vehicle import Vehicle
from validate_type import validate_type


class Rental:
    def __init__(
        self,
        rental_id: str,
        customer: Customer,
        vehicle: Vehicle,
        rental_days: int,
        total_cost: float = 0.0,
    ) -> None:
        self.rental_id = validate_type(rental_id, str, "rental_id")
        self.customer = validate_type(customer, Customer, "customer")
        self.vehicle = validate_type(vehicle, Vehicle, "vehicle")
        self.rental_days = validate_type(rental_days, int, "rental_days")
        self.total_cost = validate_type(total_cost, float, "total_cost")

    def calculate_total_cost(self) -> float:
        self.total_cost = self.vehicle.rental_rate * self.rental_days
        return self.total_cost

    def __str__(self) -> str:
        return f"Total Cost: {self.calculate_total_cost()}"


customer1 = Customer("2", "Jon")
vehicle1 = Vehicle("1", "Ford", "Mustang", 3000.0, True)
rental = Rental("1", customer1, vehicle1, 4)
print(rental.calculate_total_cost())