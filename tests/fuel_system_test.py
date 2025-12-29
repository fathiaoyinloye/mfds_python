import unittest

from dispenser_system.dispenser import Dispenser
from dispenser_system.fuel_attendant import FuelAttendant
from exceptions.fuel_already_exist_exception import FuelAlreadyExistException
from exceptions.fuel_does_not_exist_exception import FuelDoesNotExistException
from exceptions.insufficient_stock_exception import InsufficientStockException


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.dispenser = Dispenser()
        self.attendant = FuelAttendant("Fathia", "Oyinloye")

    def test_that_attendant_can_add_fuel(self):
        self.attendant.add_a_new_fuel("Petrol", 100, 50, self.dispenser)

        self.assertEqual(1, self.dispenser.get_number_of_fuel())  # add assertion here

    def test_attendant_attendant_same_fuel_twices_thow_fuel_already_exist_exception(self):
        self.attendant.add_a_new_fuel("Petrol", 100, 50, self.dispenser)
        self.assertRaises(FuelAlreadyExistException, self.attendant.add_a_new_fuel, "Petrol", 2, 3, self.dispenser)

    def test_that_attendant_can_get_available_fuel(self):
        self.attendant.add_a_new_fuel("Petrol", 100, 50, self.dispenser)
        self.assertEqual(1, self.dispenser.get_number_of_fuel())
        self.assertEqual(1, len(self.attendant.get_available_fuel(self.dispenser)))

    def test_that_attendant_can_update_available_fuel_price(self):
        self.attendant.add_a_new_fuel("Petrol", 100, 50, self.dispenser)
        self.assertEqual(1, self.dispenser.get_number_of_fuel())
        price = self.dispenser.get_fuel().get("Petrol").get_price()
        self.assertEqual(100, price)
        self.attendant.update_fuel_price("Petrol", 150, self.dispenser)
        price = self.dispenser.get_fuel().get("Petrol").get_price()
        self.assertEqual(150,price)


    def test_that_attendant_cannot_update_fuel_price_that_has_not_been_added(self):
        self.assertEqual(0, self.dispenser.get_number_of_fuel())
        self.assertRaises(FuelDoesNotExistException,self.attendant.update_fuel_price,"Petrol", 100, self.dispenser)

    def test_that_attendant_can_restock_available_fuel_price(self):
        self.attendant.add_a_new_fuel("Petrol", 100, 50, self.dispenser)
        self.assertEqual(1, self.dispenser.get_number_of_fuel())
        quantity = self.dispenser.get_fuel().get("Petrol").get_quantity()
        self.assertEqual(50, quantity)
        self.attendant.restock_fuel("Petrol", 10, self.dispenser)
        quantity = self.dispenser.get_fuel().get("Petrol").get_quantity()
        self.assertEqual(60, quantity)

    def test_that_attendant_cannot_retock_fuel_that_has_not_been_added(self):
        self.assertEqual(0, self.dispenser.get_number_of_fuel())
        self.assertRaises(FuelDoesNotExistException,self.attendant.restock_fuel,"Petrol", 100, self.dispenser)

    def test_that_attendant_can_dispense_fuel_by_amount(self):
        self.attendant.add_a_new_fuel("Petrol", 100, 50, self.dispenser)
        self.assertEqual(1, self.dispenser.get_number_of_fuel())
        self.attendant.dispense_fuel_by_amount("Petrol", 500,self.dispenser)
        quantity = self.dispenser.get_fuel().get("Petrol").get_quantity()
        self.assertEqual(45.0, quantity)

    def test_that_attendant_cannot_dispense_fuel_that_the_quantity_is_not_enough_for_the_order(self):
        self.attendant.add_a_new_fuel("Petrol", 100, 2, self.dispenser)
        self.assertEqual(1, self.dispenser.get_number_of_fuel())
        self.assertRaises(InsufficientStockException, self.attendant.dispense_fuel_by_amount,"Petrol", 500, self.dispenser)
        quantity = self.dispenser.get_fuel().get("Petrol").get_quantity()
        self.assertEqual(2.0, quantity)

    def test_that_attendant_cannot_dispense_fuel_by_amount_if_it_is_not_available(self):
        self.attendant.add_a_new_fuel("Petrol", 100, 2, self.dispenser)
        self.assertEqual(1, self.dispenser.get_number_of_fuel())
        self.assertRaises(FuelDoesNotExistException, self.attendant.dispense_fuel_by_amount, "kerosene", 5, self.dispenser)

    def test_that_attendant_can_dispense_fuel_by_pliter(self):
        self.attendant.add_a_new_fuel("Petrol", 100, 50, self.dispenser)
        self.assertEqual(1, self.dispenser.get_number_of_fuel())
        receipt = self.attendant.dispense_fuel_by_liter("Petrol", 5,self.dispenser)
        print(receipt)
        quantity = self.dispenser.get_fuel().get("Petrol").get_quantity()
        self.assertEqual(45.0, quantity)

    def testThatReceiptIsIssuedForEveryTransaction(self):
        self.attendant.add_a_new_fuel("Petrol", 100, 50, self.dispenser)
        self.assertEqual(1, self.dispenser.get_number_of_fuel())
        receipt = self.attendant.dispense_fuel_by_liter("Petrol", 5, self.dispenser)
        self.assertIsNotNone(receipt)

        self.assertEqual(1, len(self.dispenser.get_transactions()))



    def test_that_attendant_cannot_dispense_fuel_by_liter_that_the_quantity_is_not_enough_for_the_order(self):
        self.attendant.add_a_new_fuel("Petrol", 100, 2, self.dispenser)
        self.assertEqual(1, self.dispenser.get_number_of_fuel())
        self.assertRaises(InsufficientStockException, self.attendant.dispense_fuel_by_liter,"Petrol", 5, self.dispenser)
        quantity = self.dispenser.get_fuel().get("Petrol").get_quantity()
        self.assertEqual(2.0, quantity)

    def test_that_attendant_cannot_dispense_fuel_that_is_not_available(self):
        self.attendant.add_a_new_fuel("Petrol", 100, 2, self.dispenser)
        self.assertEqual(1, self.dispenser.get_number_of_fuel())
        self.assertRaises(FuelDoesNotExistException, self.attendant.dispense_fuel_by_liter, "kerosene", 5,self.dispenser)
