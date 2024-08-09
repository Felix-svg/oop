from product import Product


class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_product(self, product:Product):
        self.cart.append(product)

    def remove_product(self, product_name:str):
        self.cart = [product for product in self.cart if product.name != product_name]

    def total_cost(self):
        total = 0
        for product in self.cart:
            at = product.price * product.quantity
            total += at
        return total

    def display_cart(self):
        if not self.cart:
            return "Cart is empty"
        cart = [str(cart) for cart in self.cart]
        return "\n".join(cart)


cart = ShoppingCart()
product1 = Product(name="Milk", price=65.0, quantity=2)
product2 = Product(name="Peanut", price=465.0, quantity=1)
product3 = Product(name="Bread", price=60, quantity=3)

cart.add_product(product1)
cart.add_product(product2)
cart.add_product(product3)

cart.remove_product(product2.name)

print("Cart Contents:")
print(cart.display_cart())
print("\nTotal Cost:")
print(f"\t{cart.total_cost()}")
