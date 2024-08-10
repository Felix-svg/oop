from validate_type import validate_type
from product import Product
from customer import Customer


class Order:
    def __init__(
        self,
        order_id: str,
        customer: Customer,
        total: float,
        items: dict[Product, int] = None,
    ) -> None:
        self.order_id = validate_type(order_id, str, "order_id")
        self.customer = validate_type(customer, Customer, "customer")
        self.total = validate_type(total, float, "total")
        self.items: dict[Product, int] = items or {}

    def generate_invoice(self):
        invoice_lines = [
            f"{product.name}: {quantity} x {product.price} = {quantity * product.price}"
            for product, quantity in self.items.items()
        ]
        invoice = "\n".join(invoice_lines)
        return f"Order ID: {self.order_id}\nCustomer: {self.customer.name}\nItems:\n{invoice}\nTotal: {self.total}"

    def __str__(self) -> str:
        return self.generate_invoice()
    

customer1 = Customer("C01","Jon Doe","jondoe@email.com")
order = Order("O01", customer1)
print(order)
