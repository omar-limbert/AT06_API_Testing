from OmarHuanca.SingletonLogger import SingletonLogger
from OmarHuanca.python.session5.practice_3.Item import Item


class Purchase:
    def __init__(self):
        self.logger = SingletonLogger.__call__().get_logger()
        self.total = 0
        self.products = []

    def add_product(self, product_id, product, price, quantity):
        self.logger.info("Selling Product: {}, {}, {}, {}".format(product_id, product, price, quantity))
        self.products.append(Item(product_id, product, price, quantity, float(price) * int(quantity)))
        self.total += float(price) * int(quantity)

    def show_balance(self):
        self.logger.info("Show current balance")
        print("====================== CURRENT BALANCE ======================".format(self.total))
        for item in self.products:
            print("Id: {} Product: {} Quantity: {} Price: {} Total: {}".format(item.get_id(),
                                                                               item.get_item(),
                                                                               item.get_quantity(),
                                                                               item.get_price(),
                                                                               item.get_total()))
        print("==================== TOTAL AMOUNT: {} ====================".format(self.total))

#
# if __name__ == "__main__":
#     purchase = Purchase()
#     purchase.add_product("1", "Item 3", "1", "100")
#     purchase.add_product("2", "Item 3", "2", "50")
#     purchase.add_product("3", "Item 3", "3", "30")
#     purchase.add_product("4", "Item 3", "4", "10")
#
#     purchase.show_balance()
