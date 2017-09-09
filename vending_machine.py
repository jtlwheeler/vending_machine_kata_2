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

    def _make_change(self, amount_needed):
        if amount_needed == 0:
            return

        if amount_needed == 5 and self._coin_inventory[NICKEL] > 0:
            self._return_coin(NICKEL, remove_from_inventory=True)
            return

        if amount_needed == 10 and self._coin_inventory[DIME] > 0:
            self._return_coin(DIME, remove_from_inventory=True)
            return

        if amount_needed == 10 and self._coin_inventory[NICKEL] > 1:
            self._return_coin(NICKEL, 2, True)
            return

        if (amount_needed == 15 and self._coin_inventory[DIME] > 0 and
                self._coin_inventory[NICKEL] > 0):
            self._return_coin(NICKEL, remove_from_inventory=True)
            self._return_coin(DIME, remove_from_inventory=True)
            return

        if amount_needed == 15 and self._coin_inventory[NICKEL] > 2:
            self._return_coin(NICKEL, 3, True)
            return

        if amount_needed == 20 and self._coin_inventory[DIME] > 1:
            self._return_coin(DIME, 2, True)

        if (amount_needed == 20 and self._coin_inventory[DIME] > 0
                and self._coin_inventory[NICKEL] > 1):
            self._return_coin(DIME, remove_from_inventory=True)
            self._return_coin(NICKEL, 2, True)

    def _return_coin(self, coin, quantity=1, remove_from_inventory=False):
        if coin in self.coin_return:
            self.coin_return[coin] += quantity
        else:
            self.coin_return[coin] = quantity

        if remove_from_inventory:
            self._coin_inventory[coin] -= quantity

    def _sold_out(self):
        for quantity in self._PRODUCTS.values():
            if quantity > 0:
                return True

        return False

    def insert_coin(self, coin):
        if coin in self._inserted_coin_bin:
            self._inserted_coin_bin[coin] += 1
        else:
            self._return_coin(coin, 1)

    def get_coin_quantity(self, coin):
        return self._coin_inventory[coin]

    def get_product_quantity(self, product):
        return self._product_inventory[product]

    def read_display(self):
        if self._sold_out():
            return "SOLD OUT"

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

        change_needed = inserted_amount - self._PRODUCTS[product]
        self._make_change(change_needed)

    def vendor_load_coin(self, coin, quantity=1):
        self._coin_inventory[coin] += quantity

    def vendor_load_product(self, product, quantity=1):
        if product in self._product_inventory:
            self._product_inventory[product] += quantity
