import json

from OmarHuanca.SingletonLogger import SingletonLogger


class Shop:
    def __init__(self, shop_name):
        self.logger = SingletonLogger.__call__().get_logger()
        self.data = {}
        self.shop_name = shop_name
        self.fill_products_from_data_base()

    def get_shop_name(self):
        self.logger.info("Return shop name: {}".format(self.shop_name))
        return self.shop_name

    def fill_products_from_data_base(self):
        self.logger.info("Loading Products from DataBase")
        with open('data.json') as json_file:
            self.data = json.load(json_file)

    def show_products(self):
        self.logger.info("Show currently Products")
        for product in self.data["product"]:
            print("ID: [{}] Item: [{}] Price: [{}] Quantity: [{}]".format(product["id"],
                                                                          product["item"],
                                                                          product["price"],
                                                                          product["quantity"]))

    def get_products(self):
        self.logger.info("Return Product Data")
        return self.data

    def sell_product(self, product_to_sell, quantity_to_sell):
        self.logger.info("Selling Product and update stock {}, {}".format(product_to_sell, product_to_sell))
        for product_in_stock in self.data["product"]:
            if product_in_stock["id"] == product_to_sell:
                new_quantity = int(product_in_stock["quantity"]) - quantity_to_sell
                product_in_stock["quantity"] = new_quantity
                self.logger.info("[Sold] Product: {} Qty: {} After: {}".format(product_to_sell,
                                                                               quantity_to_sell,
                                                                               new_quantity))
                return product_in_stock

# if __name__ == "__main__":
#     shop = Shop("Shop Test")
#     shop.sell_product("9", 100)
#     shop.show_products()
