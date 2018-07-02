from OmarHuanca.SingletonLogger import SingletonLogger


class Item:
    def __init__(self, item, price, quantity,total):
        self.logger = SingletonLogger.__call__().get_logger()
        self.item = item
        self.price = price
        self.quantity = quantity
        self.total =total

    def get_item(self):
        return self.item

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    def get_total(self):
        return self.total
