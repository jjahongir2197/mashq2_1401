class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity


class OnlineShop:
    def __init__(self):
        self.cart = []

    def add_product(self, product):
        self.cart.append(product)

    def remove_product(self, name):
        for product in self.cart:
            if product.name == name:
                self.cart.remove(product)
                return f"{name} o‘chirildi"
        return "Mahsulot topilmadi"

    def calculate_total(self):
        total = 0
        for product in self.cart:
            total += product.total_price()
        return total

    def show_cart(self):
        for product in self.cart:
            print(f"{product.name} | {product.quantity} dona | {product.price} so‘m")


shop = OnlineShop()
shop.add_product(Product("Telefon", 3000000, 1))
shop.add_product(Product("Naushnik", 250000, 2))
shop.show_cart()
print("Jami:", shop.calculate_total(), "so‘m")
