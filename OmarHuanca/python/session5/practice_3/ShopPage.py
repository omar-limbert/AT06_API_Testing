import json

from OmarHuanca.SingletonLogger import SingletonLogger


class ShopPage:
    def __init__(self):
        self.logger = SingletonLogger.__call__().get_logger()
        self.data = {}

    def fill_products_from_data_base(self):
        self.logger.info("Loading Products from DataBase")
        with open('data.json') as json_file:
            self.data = json.load(json_file)

    def show_products(self):
        self.logger.info("Show currently Products")
        for product in self.data["product"]:
            print("Item: [{}] Price: [{}] Quantity: [{}]".format(product["item"],
                                                                 product["price"],
                                                                 product["quantity"]))

    def sell_product(self, product_to_sell, quantity_to_sell):
        for product_in_stock in self.data["product"]:
            if product_in_stock["item"] == product_to_sell:
                new_quantity = int(product_in_stock["quantity"]) - quantity_to_sell
                product_in_stock["quantity"] = new_quantity
                self.logger.info("[Sold] Product: {} Qty: {} After: {}".format(product_to_sell,
                                                                               quantity_to_sell,
                                                                               new_quantity))
                break


if __name__ == "__main__":
    shop = ShopPage()
    shop.fill_products_from_data_base()
    shop.sell_product("Item 3", 100)
    shop.show_products()
