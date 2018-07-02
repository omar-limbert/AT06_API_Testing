from OmarHuanca.SingletonLogger import SingletonLogger


class Item:
    def __init__(self, id, item, price, quantity, total):
        self.logger = SingletonLogger.__call__().get_logger()
        self.id = id
        self.item = item
        self.price = price
        self.quantity = quantity
        self.total = total

    def get_id(self):
        return self.id

    def get_item(self):
        return self.item

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    def get_total(self):
        return self.total
