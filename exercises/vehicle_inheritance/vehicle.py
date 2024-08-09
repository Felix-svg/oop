class Vehicle:
    def __init__(self, make: str, model: str, year: int) -> None:
        self.make = make
        self.model = model
        self.year = year

    @property
    def make(self):
        return self._make

    @make.setter
    def type(self, make):
        if isinstance(make, str) and len(type) > 2:
            self._make = make
        else:
            raise ValueError("Make must be a string and have at least three characters")

    @property
    def model(self):
        return self._model

    @model.setter
    def type(self, model):
        if isinstance(model, str) and len(model) > 2:
            self._model = model
        else:
            raise ValueError(
                "Model must be a string and have at least three characters"
            )

    @property
    def year(self):
        return self._year

    @year.setter
    def type(self, year):
        if isinstance(year, int) and len(year) == 4:
            self._year = year
        else:
            raise ValueError("Year must be a number and have four characters")

    def display_info(self) -> str:
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}"

    def __str__(self) -> str:
        return self.display_info()
