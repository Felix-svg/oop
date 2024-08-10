from validate_type import validate_type


class Product:
    def __init__(self, product_id: str, name: str, price: float, stock: int) -> None:
        self.product_id = product_id
        self.name = validate_type(name, str, "name")
        self.price = validate_type(price, float, "price")
        self.stock = validate_type(stock, int, "stock")

    # Returns the available stock for the product.
    def check_stock(self) -> int:
        return self.stock

    # Reduces the stock by the specified quantity.
    def reduce_stock(self, quantity: int) -> None:
        if quantity > self.stock:
            raise ValueError(
                f"Cannot reduce stock by {quantity}. Only {self.stock} left."
            )
        self.stock -= quantity

    def __str__(self) -> str:
        return f"Product: {self.name}\nPrice: {self.price}\nStock: {self.stock}"
