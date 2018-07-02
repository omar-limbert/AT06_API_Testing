import json

from OmarHuanca.SingletonLogger import SingletonLogger
from OmarHuanca.python.session5.practice_3.Item import Item


class Purchase:
    def __init__(self):
        self.logger = SingletonLogger.__call__().get_logger()
        self.total = 0
        self.products = []

    def add_product(self, product, price, quantity):
        self.products.append(Item(product, price, quantity, float(price) * int(quantity)))
        self.total += float(price) * int(quantity)


if __name__ == "__main__":
    purchase = Purchase()
    purchase.add_product("Item 3", "1", "100")
