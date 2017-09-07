PENNY = "PENNY"
 
class VendingMachine():
    def __init__(self):
        self.coin_return = []

    def insert_coin(self, coin):
        if coin == PENNY:
            self.coin_return.append(coin)
