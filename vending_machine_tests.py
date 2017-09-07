import unittest
import vending_machine as vm
from vending_machine import VendingMachine

class VendingMachineTests(unittest.TestCase):
    def setUp(self):
        self.machine = VendingMachine()

    def test_when_a_penny_is_inserted_it_is_placed_in_the_coin_return(self):
        self.machine.insert_coin(vm.PENNY)
        self.assertDictEqual({vm.PENNY : 1}, self.machine.coin_return)

    def test_when_a_nickel_is_inserted_it_is_not_placed_in_the_coin_return(self):
        self.machine.insert_coin(vm.NICKEL)
        self.assertDictEqual({}, self.machine.coin_return)

    def test_when_a_dime_is_inserted_it_is_not_placed_in_the_coin_return(self):
        self.machine.insert_coin(vm.DIME)
        self.assertDictEqual({}, self.machine.coin_return)

    def test_when_a_quarter_is_inserted_it_is_not_placed_in_the_coin_return(self):
        self.machine.insert_coin(vm.QUARTER)
        self.assertDictEqual({}, self.machine.coin_return)

    def test_when_nickel_is_inserted_and_coin_return_button_is_pressed_it_is_placed_in_coin_return(self):
        self.machine.insert_coin(vm.NICKEL)
        self.machine.return_coins()
        self.assertDictEqual({vm.NICKEL : 1}, self.machine.coin_return)

    def test_when_two_nickels_are_inserted_and_coin_return_button_is_pressed_they_are_placed_in_coin_return(self):
        self.machine.insert_coin(vm.NICKEL)
        self.machine.insert_coin(vm.NICKEL)
        self.machine.return_coins()
        self.assertDictEqual({vm.NICKEL : 2}, self.machine.coin_return)

if __name__ == '__main__':
    unittest.main()
