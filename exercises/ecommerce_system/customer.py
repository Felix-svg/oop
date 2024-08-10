from validate_type import validate_type
from shopping_cart import ShoppingCart
from product import Product
from order import Order


class Customer:
    def __init__(self, customer_id: str, name: str, email: str) -> None:
        self.customer_id = validate_type(customer_id, str, "customer_id")
        self.name = validate_type(name, str, "name")
        self.email = validate_type(email, str, "email")
        self.cart = ShoppingCart()

    # Adds a product to the customer's cart.
    def add_to_cart(self, product: Product, quantity: int) -> None:
        self.cart.add_item(product, quantity)

    # Places an order for all items in the cart.
    def place_order(self) -> Order:
        if not self.cart.items:
            raise ValueError("Cart is empty")
        total = self.cart.calculate_total()
        order = Order(order_id="ORDER123", customer=self, total=total, items=self.cart.items.copy())
        self.cart = ShoppingCart()  # Reset cart after order is placed
        return order

    def __str__(self) -> str:
        return f"Customer: {self.name}\nEmail: {self.email}\nCart: {self.cart}"
