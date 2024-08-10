from validate_type import validate_type
from product import Product


class ShoppingCart:
    def __init__(self, items: dict[Product, int]) -> None:
        self.items: dict[Product, int] = items or {}

    # Adds a product to the cart.
    def add_item(self, product: Product, quantity: int) -> None:
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

    # Removes a product from the cart.
    def remove_item(self, product: Product) -> None:
        if product in self.items:
            del self.items[product]
        else:
            raise ValueError(f"Product {product.name} not in cart.")

    # Returns the total cost of items in the cart.
    def calculate_total(self) -> float:
        total = sum(
            product.price * quantity for product, quantity in self.items.items()
        )
        return total

    def __str__(self) -> str:
        cart_details = "\n".join(
            f"{product.name}: {quantity}" for product, quantity in self.items.items()
        )
        return f"Shopping Cart:\n{cart_details}"
