PENNY = "PENNY"
NICKEL = "NICKEL"
DIME = "DIME"
QUARTER = "QUARTER"

COLA = "COLA"
CHIPS = "CHIPS"
CANDY = "CANDY"

class VendingMachine:
    _PRODUCTS = {COLA : 100, CHIPS : 50, CANDY : 65}

    def __init__(self):
        self._inserted_coin_bin = {NICKEL : 0, DIME : 0, QUARTER : 0}
        self._product_inventory = {}
        for product in self._PRODUCTS:
            self._product_inventory[product] = 0

        self.coin_return = {}
        self.product_dispense_bin = ""

    def _return_coin(self, coin, quantity):
        if coin in self.coin_return:
            self.coin_return[coin] += quantity
        else:
            self.coin_return[coin] = quantity

    def insert_coin(self, coin):
        if coin in self._inserted_coin_bin:
            self._inserted_coin_bin[coin] += 1
        else:
            self._return_coin(coin, 1)

    def get_product_quantity(self, product):
        return self._product_inventory[product]

    def return_coins(self):
        for coin in self._inserted_coin_bin:
            if self._inserted_coin_bin[coin] > 0:
                self._return_coin(coin, self._inserted_coin_bin[coin])
                self._inserted_coin_bin[coin] -= 1

    def select_product(self, product):
        if self._product_inventory[product] == 0:
            return

    def vendor_load_product(self, product, quantity):
        if product in self._product_inventory:
            self._product_inventory[product] += quantity
