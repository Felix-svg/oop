from customer import Customer
from vehicle import Vehicle


class Rental:
    def __init__(
        self,
        rental_id: str,
        customer: Customer,
        vehicle: Vehicle,
        rental_days: int,
        total_cost:float = 0.0
    ) -> None:
        self.rental_id = rental_id
        self.customer = customer
        self.vehicle = vehicle
        self.rental_days = rental_days
        self.total_cost = total_cost

    @property
    def rental_id(self):
        return self._rental_id

    @rental_id.setter
    def rental_id(self, id: str):
        if not isinstance(id, str):
            raise ValueError("rental_id must be a string")
        else:
            self._rental_id = id

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer: Customer):
        if not isinstance(customer, Customer):
            raise ValueError("customer must be an instance of Customer")
        else:
            self._customer = customer

    @property
    def vehicle(self):
        return self._vehicle

    @vehicle.setter
    def vehicle(self, vehicle: Vehicle):
        if not isinstance(vehicle, Vehicle):
            raise ValueError("vehicle must be an instance of Vehicle")
        else:
            self._vehicle = vehicle

    @property
    def rental_days(self):
        return self._rental_days

    @rental_days.setter
    def rental_days(self, days: int):
        if not isinstance(days, int):
            raise ValueError("rental_days must be a number")
        else:
            self._rental_days = days

    @property
    def total_cost(self):
        return self._total_cost

    @total_cost.setter
    def total_cost(self, cost: float):
        if not isinstance(cost, float):
            raise ValueError("total_cost must be a floating number")
        else:
            self._total_cost = cost

    def calculate_total_cost(self) -> float:
        self.total_cost = self.vehicle.rental_rate * self.rental_days
        return self.total_cost

    def __str__(self) -> str:
        return f"Total Cost: {self.calculate_total_cost()}"



customer1 = Customer("2", "Jon")
vehicle1 = Vehicle("1", "Ford", "Mustang", 3000.0,True)
rental = Rental("1",customer1,vehicle1,4)
print(rental.calculate_total_cost())