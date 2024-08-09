import datetime
from menu_item import MenuItem


class Order:
    def __init__(self) -> None:
        self.order = []
        self.time_of_order = datetime.datetime.now() 

    def add_item(self, menu_item):
        self.order.append(menu_item)

    def remove_item(self, menu_item_name):
        self.order = [
            menu_item for menu_item in self.order if menu_item.name != menu_item_name
        ]

    def calculate_total(self):
        total = 0
        for item in self.order:
            total += item.price
        return total

    def display_order(self):
        order = [str(order) for order in self.order]
        return f'{"\n".join(order)}\nTotal: {self.calculate_total()}'

    def __str__(self) -> str:
        order_time = self.time_of_order.strftime("%Y-%m-%d %H:%M:%S")
        return f"Your Order: {order_time}\n{self.display_order()}"
    


item1 = MenuItem("Chicken Wings", 600.0)
item2 = MenuItem("Soda", 200.0)
order = Order()
order.add_item(item1)
order.add_item(item2)
# print(order.display_order())
# print(order.calculate_total())
# order.remove_item(item2.name)
# print(order.display_order())
print(order)
