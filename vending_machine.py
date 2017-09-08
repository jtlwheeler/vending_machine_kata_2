PENNY = "PENNY"
NICKEL = "NICKEL"
DIME = "DIME"
QUARTER = "QUARTER"

COLA = "COLA"
CHIPS = "CHIPS"
CANDY = "CANDY"

class VendingMachine:
    _PRODUCTS = {COLA : 100, CHIPS : 50, CANDY : 65}
    _VALID_COINS = {NICKEL : 5, DIME : 10, QUARTER : 25}

    def __init__(self):
        self._coin_inventory = {}
        self._inserted_coin_bin = {}

        for coin in self._VALID_COINS:
            self._coin_inventory[coin] = 0
            self._inserted_coin_bin[coin] = 0

        self._product_inventory = {}
        for product in self._PRODUCTS:
            self._product_inventory[product] = 0

        self.coin_return = {}
        self.product_dispense_bin = ""

    def _get_current_amount(self):
        current_amount = 0
        for coin in self._inserted_coin_bin:
            current_amount += self._inserted_coin_bin[coin] * self._VALID_COINS[coin]

        return current_amount

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

    def get_coin_quantity(self, coin):
        return self._coin_inventory[coin]

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

        inserted_amount = self._get_current_amount()
        if inserted_amount < self._PRODUCTS[product]:
            return

        self.product_dispense_bin = product
        self._product_inventory[product] -= 1
        for coin in self._inserted_coin_bin:
            self._coin_inventory[coin] += self._inserted_coin_bin[coin]
            self._inserted_coin_bin[coin] = 0

    def vendor_load_product(self, product, quantity):
        if product in self._product_inventory:
            self._product_inventory[product] += quantity
