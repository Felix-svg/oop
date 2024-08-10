class Vehicle:
    def __init__(
        self,
        vehicle_id: str,
        make: str,
        model: str,
        rental_rate: float,
        is_rented: bool,
    ) -> None:
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.rental_rate = rental_rate
        self.is_rented = is_rented

    @property
    def vehicle_id(self):
        return self._vehicle_id

    @vehicle_id.setter
    def vehicle_id(self, id):
        if not isinstance(id, str):
            raise ValueError("vehicle_id must be a string")
        else:
            self._vehicle_id = id

    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, make):
        if not isinstance(make, str):
            raise ValueError("make must be a string")
        else:
            self._make = make

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        if not isinstance(model, str):
            raise ValueError("model must be a string")
        else:
            self._model = model

    @property
    def rental_rate(self):
        return self._rental_rate

    @rental_rate.setter
    def rental_rate(self, rate: float):
        if not isinstance(rate, float):
            raise ValueError("rental rate must be a float")
        else:
            self._rental_rate = rate

    @property
    def is_rented(self):
        return self._is_rented

    @is_rented.setter
    def is_rented(self, val: bool):
        if not isinstance(val, bool):
            raise ValueError("is_rented must be a boolean")
        else:
            self._is_rented = val

    def rent_vehicle(self) -> None:
        self.is_rented = True

    def return_vehicle(self) -> None:
        self.is_rented = False

    def __str__(self) -> str:
        return f"{self.make} {self.model} - Daily Rate: {self.rental_rate}, Rented: {self.is_rented}"
