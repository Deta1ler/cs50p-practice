class ShoppingCart:
    def __init__(self):
        self.items = []


    def add_item(self, title, price):
        self.items.append({"title": title, "price": price})


    def total(self):
        sum = 0
        for item in self.items:
            sum = sum + item["price"]
        return sum


cart_1 = ShoppingCart()
cart_2 = ShoppingCart()

cart_1.add_item("Хлеб", 45)
cart_1.add_item("Молоко", 45.5)


print(cart_1.total())