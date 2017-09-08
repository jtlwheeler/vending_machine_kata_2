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

    def test_when_dime_is_inserted_and_coin_return_button_is_pressed_it_is_placed_in_coin_return(self):
        self.machine.insert_coin(vm.DIME)
        self.machine.return_coins()
        self.assertDictEqual({vm.DIME : 1}, self.machine.coin_return)

    def test_when_quarter_is_inserted_and_coin_return_button_is_pressed_it_is_placed_in_coin_return(self):
        self.machine.insert_coin(vm.QUARTER)
        self.machine.return_coins()
        self.assertDictEqual({vm.QUARTER : 1}, self.machine.coin_return)

    def test_when_coins_are_inserted_and_coin_return_button_is_pressed_they_are_placed_in_coin_return(self):
        self.machine.insert_coin(vm.NICKEL)
        self.machine.insert_coin(vm.NICKEL)
        self.machine.insert_coin(vm.PENNY)
        self.machine.insert_coin(vm.DIME)
        self.machine.insert_coin(vm.DIME)
        self.machine.insert_coin(vm.QUARTER)
        self.machine.insert_coin(vm.QUARTER)

        self.machine.return_coins()

        expected_dict = {vm.PENNY : 1, vm.NICKEL : 2, vm.DIME : 2, vm.QUARTER : 2}
        self.assertDictEqual(expected_dict, self.machine.coin_return)

    def test_when_cola_is_selected_without_enough_money_it_is_not_dispensed(self):
        self.machine.select_product(vm.COLA)
        self.assertEqual("", self.machine.product_dispense_bin)

    def test_when_vendor_loads_one_cola_it_is_added_to_the_product_inventory(self):
        self.machine.vendor_load_product(vm.COLA, 1)
        self.assertEqual(1, self.machine.get_product_quantity(vm.COLA))
   
    def test_when_vendor_loads_five_cola_it_is_added_to_the_product_inventory(self):
        self.machine.vendor_load_product(vm.COLA, 5)
        self.assertEqual(5, self.machine.get_product_quantity(vm.COLA))

if __name__ == '__main__':
    unittest.main()
