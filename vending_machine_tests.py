import unittest
import vending_machine
from vending_machine import VendingMachine

class VendingMachineTests(unittest.TestCase):
    def setUp(self):
        self.machine = VendingMachine()

    def test_when_a_penny_is_inserted_it_is_placed_in_the_coin_return(self):
        self.machine.insert_coin(vending_machine.PENNY)
        self.assertListEqual([vending_machine.PENNY], self.machine.coin_return)

    def test_when_a_nickel_is_inserted_it_is_not_placed_in_the_coin_return(self):
        self.machine.insert_coin(vending_machine.NICKEL)
        self.assertListEqual([], self.machine.coin_return)

    def test_when_a_dime_is_inserted_it_is_not_placed_in_the_coin_return(self):
        self.machine.insert_coin(vending_machine.DIME)
        self.assertListEqual([], self.machine.coin_return)

    def test_when_a_quarter_is_inserted_it_is_not_placed_in_the_coin_return(self):
        self.machine.insert_coin(vending_machine.QUARTER)
        self.assertListEqual([], self.machine.coin_return)

    def test_when_nickel_is_inserted_and_coin_return_button_is_pressed_it_is_placed_in_coin_return(self):
        self.machine.insert_coin(vending_machine.NICKEL)
        self.machine.return_coins()
        self.assertListEqual([vending_machine.NICKEL], self.machine.coin_return)

if __name__ == '__main__':
    unittest.main()
