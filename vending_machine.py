PENNY = "PENNY"
NICKEL = "NICKEL"
DIME = "DIME"
QUARTER = "QUARTER"

class VendingMachine():
    def __init__(self):
        self._inserted_coin_bin = {NICKEL : 0, DIME : 0, QUARTER : 0}
        self.coin_return = []

    def insert_coin(self, coin):
        if coin in self._inserted_coin_bin:
            self._inserted_coin_bin[coin] += 1
        else:
            self.coin_return.append(coin)

    def return_coins(self):
        for coin in self._inserted_coin_bin:
            if self._inserted_coin_bin[coin] > 0:
                self.coin_return.append(coin)
                self._inserted_coin_bin[coin] -= 1
