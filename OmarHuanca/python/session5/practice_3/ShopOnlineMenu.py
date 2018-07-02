import json
import sys

from OmarHuanca.SingletonLogger import SingletonLogger
from OmarHuanca.python.session5.practice_3.Shop import Shop
from OmarHuanca.python.session5.practice_3.Purchase import Purchase


class ShopOnlineMenu:
    def __init__(self, shop_name):
        self.logger = SingletonLogger.__call__().get_logger()
        self.shop = Shop(shop_name)
        self.purchase = Purchase()
        self.finish_add = 0
        self.show_menu()

    def show_menu(self):
        print("====== Welcome to: [ {} ] Shop ONLINE ======".format(self.shop.get_shop_name()))
        option = 0
        while True:
            print("(1) Show Products")
            print("(2) Add to Cart")
            print("(3) Show Balance")
            print("(4) Exit")

            try:
                option = int(input('Please insert your Option : '))
            except ValueError:
                print("Is not valid number, please try again.")
                pass

            if option == 1:
                self.shop.show_products()

            if option == 2:
                self.add_to_cart()

            if option == 3:
                self.purchase.show_balance()

            if option == 4:
                sys.exit()

    def add_to_cart(self):
        self.finish_add = self.shop.get_products()["product"].__len__() + 1
        self.show_products_in_stock()

        product_id = 0
        quantity = 0
        while True:
            try:
                product_id = int(input('Please select your product: '))
                if product_id == self.finish_add:
                    break

                quantity = int(input('Please enter your quantity: '))
            except ValueError:
                print("Is not valid number, please try again.")
                pass

            self.sell_product(product_id, quantity)
            self.show_products_in_stock()

    def sell_product(self, product_id, quantity):
        product = self.shop.sell_product(str(product_id), quantity)

        self.purchase.add_product(str(product["id"]),
                                  str(product["item"]),
                                  str(product["price"]),
                                  str(quantity))

        self.purchase.show_balance()

    def show_products_in_stock(self):
        for product in self.shop.get_products()["product"]:
            print("({}) => Product: {} Price: {} Stock: {}".format(product["id"],
                                                                   product["item"],
                                                                   product["price"],
                                                                   product["quantity"]))
        print("({}) FINISH PURCHASE".format(self.finish_add))


if __name__ == "__main__":
    shop = ShopOnlineMenu("Ebay.com")
