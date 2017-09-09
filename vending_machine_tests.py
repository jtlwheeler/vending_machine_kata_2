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

    def test_when_vendor_loads_five_colas_it_is_added_to_the_product_inventory(self):
        self.machine.vendor_load_product(vm.COLA, 5)
        self.assertEqual(5, self.machine.get_product_quantity(vm.COLA))

    def test_when_vendor_loads_one_chips_it_is_added_to_the_product_inventory(self):
        self.machine.vendor_load_product(vm.CHIPS, 1)
        self.assertEqual(1, self.machine.get_product_quantity(vm.CHIPS))

    def test_when_vendor_loads_one_candy_it_is_added_to_the_product_inventory(self):
        self.machine.vendor_load_product(vm.CANDY, 1)
        self.assertEqual(1, self.machine.get_product_quantity(vm.CANDY))

    def test_when_cola_is_selected_with_enough_money_then_it_is_dispensed_and_removed_from_inventory(self):
        self.machine.vendor_load_product(vm.COLA, 1)
        self.machine.insert_coin(vm.QUARTER)
        self.machine.insert_coin(vm.QUARTER)
        self.machine.insert_coin(vm.QUARTER)
        self.machine.insert_coin(vm.QUARTER)

        self.machine.select_product(vm.COLA)
        self.assertEqual(vm.COLA, self.machine.product_dispense_bin)
        self.assertEqual(0, self.machine.get_product_quantity(vm.COLA))

    def test_when_chips_is_selected_with_enough_money_then_it_is_dispensed_and_removed_from_inventory(self):
        self.machine.vendor_load_product(vm.CHIPS, 3)
        self.machine.insert_coin(vm.QUARTER)
        self.machine.insert_coin(vm.QUARTER)

        self.machine.select_product(vm.CHIPS)
        self.assertEqual(vm.CHIPS, self.machine.product_dispense_bin)
        self.assertEqual(2, self.machine.get_product_quantity(vm.CHIPS))

    def test_when_candy_is_selected_with_enough_money_then_it_is_dispensed_and_removed_from_inventory(self):
        self.machine.vendor_load_product(vm.CANDY, 10)
        self.machine.insert_coin(vm.NICKEL)
        self.machine.insert_coin(vm.DIME)
        self.machine.insert_coin(vm.QUARTER)
        self.machine.insert_coin(vm.QUARTER)

        self.machine.select_product(vm.CANDY)
        self.assertEqual(vm.CANDY, self.machine.product_dispense_bin)
        self.assertEqual(9, self.machine.get_product_quantity(vm.CANDY))

    def test_when_cola_is_dispensed_the_coins_are_placed_in_the_coin_inventory(self):
        self.machine.vendor_load_product(vm.COLA, 1)
        self.machine.insert_coin(vm.QUARTER)
        self.machine.insert_coin(vm.QUARTER)
        self.machine.insert_coin(vm.QUARTER)
        self.machine.insert_coin(vm.QUARTER)

        self.machine.select_product(vm.COLA)
        self.assertEqual(4, self.machine.get_coin_quantity(vm.QUARTER))

    def test_when_chips_are_dispensed_the_coins_are_placed_in_the_coin_inventory(self):
        self.machine.vendor_load_product(vm.CHIPS, 1)
        self.machine.insert_coin(vm.DIME)
        self.machine.insert_coin(vm.DIME)
        self.machine.insert_coin(vm.DIME)
        self.machine.insert_coin(vm.DIME)
        self.machine.insert_coin(vm.DIME)

        self.machine.select_product(vm.CHIPS)
        self.assertEqual(vm.CHIPS, self.machine.product_dispense_bin)
        self.assertEqual(5, self.machine.get_coin_quantity(vm.DIME))

    def test_when_candy_is_dispensed_the_coins_are_placed_in_the_coin_inventory(self):
        self.machine.vendor_load_product(vm.CANDY, 1)
        self.machine.insert_coin(vm.NICKEL)
        self.machine.insert_coin(vm.DIME)
        self.machine.insert_coin(vm.QUARTER)
        self.machine.insert_coin(vm.QUARTER)

        self.machine.select_product(vm.CANDY)
        self.assertEqual(vm.CANDY, self.machine.product_dispense_bin)
        self.assertEqual(1, self.machine.get_coin_quantity(vm.NICKEL))
        self.assertEqual(1, self.machine.get_coin_quantity(vm.DIME))
        self.assertEqual(2, self.machine.get_coin_quantity(vm.QUARTER))

    def test_when_vendor_inserts_nickel_it_is_added_to_coin_inventory(self):
        self.machine.vendor_load_coin(vm.NICKEL)
        self.assertEqual(1, self.machine.get_coin_quantity(vm.NICKEL))

    def test_when_vendor_inserts_dimes_they_are_added_to_coin_inventory(self):
        self.machine.vendor_load_coin(vm.DIME, 5)
        self.assertEqual(5, self.machine.get_coin_quantity(vm.DIME))

    def test_when_vendor_inserts_quarters_they_are_added_to_coin_inventory(self):
        self.machine.vendor_load_coin(vm.QUARTER, 100)
        self.assertEqual(100, self.machine.get_coin_quantity(vm.QUARTER))

    def test_when_vendor_loads_penny_then_key_error_should_be_thrown(self):
        with self.assertRaises(KeyError):
            self.machine.vendor_load_coin(vm.PENNY)

    def test_when_cola_is_selected_and_five_cents_is_needed_a_nickel_is_placed_in_the_coin_return(self):
        self.machine.vendor_load_product(vm.COLA, 1)
        self.machine.vendor_load_coin(vm.NICKEL)

        self.machine.insert_coin(vm.QUARTER)
        self.machine.insert_coin(vm.QUARTER)
        self.machine.insert_coin(vm.QUARTER)
        self.machine.insert_coin(vm.DIME)
        self.machine.insert_coin(vm.DIME)
        self.machine.insert_coin(vm.DIME)

        self.machine.select_product(vm.COLA)
        self.assertDictEqual({vm.NICKEL : 1}, self.machine.coin_return)

    def test_when_chips_is_selected_and_five_cents_is_needed_a_nickel_is_placed_in_the_coin_return(self):
        self.machine.vendor_load_product(vm.CHIPS, 1)
        self.machine.vendor_load_coin(vm.NICKEL)

        self.machine.insert_coin(vm.QUARTER)
        self.machine.insert_coin(vm.DIME)
        self.machine.insert_coin(vm.DIME)
        self.machine.insert_coin(vm.DIME)

        self.machine.select_product(vm.CHIPS)
        self.assertDictEqual({vm.NICKEL : 1}, self.machine.coin_return)
    
    def test_when_candy_is_selected_and_five_cents_is_needed_a_nickel_is_placed_in_the_coin_return(self):
        self.machine.vendor_load_product(vm.CANDY, 1)
        self.machine.vendor_load_coin(vm.NICKEL)

        self.machine.insert_coin(vm.QUARTER)
        self.machine.insert_coin(vm.QUARTER)
        self.machine.insert_coin(vm.DIME)
        self.machine.insert_coin(vm.DIME)

        self.machine.select_product(vm.CANDY)
        self.assertDictEqual({vm.NICKEL : 1}, self.machine.coin_return)

    def test_when_cola_is_selected_and_ten_cents_is_needed_and_machine_only_has_dimes_then_a_dime_is_placed_in_the_coin_return(self):
        self.machine.vendor_load_product(vm.COLA, 1)
        self.machine.vendor_load_coin(vm.DIME)

        self.machine.insert_coin(vm.QUARTER)
        self.machine.insert_coin(vm.QUARTER)
        self.machine.insert_coin(vm.QUARTER)
        self.machine.insert_coin(vm.NICKEL)
        self.machine.insert_coin(vm.NICKEL)
        self.machine.insert_coin(vm.QUARTER)

        self.machine.select_product(vm.COLA)
        self.assertDictEqual({vm.DIME : 1}, self.machine.coin_return)

if __name__ == '__main__':
    unittest.main()
