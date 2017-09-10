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
        self._display = ""
        self._inserted_coin_bin = {}

        for coin in self._VALID_COINS:
            self._coin_inventory[coin] = 0
            self._inserted_coin_bin[coin] = 0

        self._product_inventory = {}
        for product in self._PRODUCTS:
            self._product_inventory[product] = 0

        self._selected_product = ""

        self.coin_return = {}
        self.product_dispense_bin = ""

    def _can_make_change_for_product(self, product):
        if product == "":
            return True

        if product == COLA or product == CHIPS:
            if self._coin_inventory[NICKEL] > 0:
                return True
            else:
                return False

        if product == CANDY:
            if self._coin_inventory[NICKEL] >= 2 or self._coin_inventory[DIME] > 0:
                return True
            else:
                return False

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

    def _no_coins(self):
        for coin_quantity in self._coin_inventory.values():
            if coin_quantity > 0:
                return False

        return True

    def _return_coin(self, coin, quantity=1, remove_from_inventory=False):
        if coin in self.coin_return:
            self.coin_return[coin] += quantity
        else:
            self.coin_return[coin] = quantity

        if remove_from_inventory:
            self._coin_inventory[coin] -= quantity

    def _sold_out(self):
        for quantity in self._product_inventory.values():
            if quantity > 0:
                return False

        return True

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

        if self._display:
            temp_display = self._display
            self._display = ""
            return temp_display

        if (self._no_coins() or (self._can_make_change_for_product(self._selected_product)
                                 is False)):
            return "EXACT CHANGE ONLY"

        amount_entered = self._get_current_amount()
        if amount_entered > 0:
            return "$%.2f" % (amount_entered / 100.0)

        return "INSERT COIN"

    def return_coins(self):
        for coin in self._inserted_coin_bin:
            if self._inserted_coin_bin[coin] > 0:
                self._return_coin(coin, self._inserted_coin_bin[coin])
                self._inserted_coin_bin[coin] -= 1

        self._selected_product = ""

    def select_product(self, product):
        self._selected_product = product

        if self._product_inventory[product] == 0:
            self._display = "SOLD OUT"
            return

        inserted_amount = self._get_current_amount()
        if inserted_amount < self._PRODUCTS[product]:
            self._display = "PRICE $%.2f" % (self._PRODUCTS[product] / 100.0)
            return

        self.product_dispense_bin = product
        self._product_inventory[product] -= 1
        for coin in self._inserted_coin_bin:
            self._coin_inventory[coin] += self._inserted_coin_bin[coin]
            self._inserted_coin_bin[coin] = 0

        change_needed = inserted_amount - self._PRODUCTS[product]
        self._make_change(change_needed)

        self._display = "THANK YOU"
        self._selected_product = ""

    def vendor_load_coin(self, coin, quantity=1):
        self._coin_inventory[coin] += quantity

    def vendor_load_product(self, product, quantity=1):
        if product in self._product_inventory:
            self._product_inventory[product] += quantity
