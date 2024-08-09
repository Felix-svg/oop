class Product:
    def __init__(self, name: str, price: float, quantity: int = 1):
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name:str):
        if isinstance(name, str) and (len(name) > 2):
            self._name = name
        else:
            raise ValueError("Name must be a string and have at least two characters")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price:float):
        if isinstance(price, float) and price > 0:
            self._price = price
        else:
            raise ValueError("Price must be a floating number nad greater than zero")

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity:int):
        if isinstance(quantity, int) and quantity > 1:
            self._quantity = quantity
        else:
            raise ValueError("Quantity must be a number and at least one")

    def __str__(self):
        return (
            f"Product(name='{self.name}', price={self.price}, quantity={self.quantity})"
        )
