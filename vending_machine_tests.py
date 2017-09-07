import unittest
import vending_machine
from vending_machine import VendingMachine

class VendingMachineTests(unittest.TestCase):
    def test_when_a_penny_is_inserted_it_is_placed_in_the_coin_return(self):
        machine = VendingMachine()
        machine.insert_coin(vending_machine.PENNY)
        self.assertListEqual([vending_machine.PENNY], machine.coin_return)

    def test_when_a_nickel_is_inserted_it_is_not_placed_in_the_coin_return(self):
        machine = VendingMachine()
        machine.insert_coin(vending_machine.NICKEL)
        self.assertListEqual([], machine.coin_return)

if __name__ == '__main__':
    unittest.main()
