class MenuItem:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        if isinstance(name, str) and (len(name) > 2):
            self._name = name
        else:
            raise ValueError("Name must be a string and at least two charaters long")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price: float):
        if isinstance(price, float) and price > 0:
            self._price = price
        else:
            raise ValueError("Price must be a floating number and greater that zero")

    def __str__(self) -> str:
        return f"Item: {self.name} \nPrice: {self.price}\n"