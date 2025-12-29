from exceptions.fuel_already_exist_exception import FuelAlreadyExistException
from exceptions.fuel_does_not_exist_exception import FuelDoesNotExistException
from exceptions.insufficient_stock_exception import InsufficientStockException
from exceptions.no_available_fuel import NoAvailableFuel
from .fuel import Fuel
from .receipt import Receipt


class Dispenser:
    def __init__(self):
        self.__collection_of_fuel = {}
        self.__list_of_transactions = []

    def add_fuel(self, fuel: Fuel):
        self.__validate(fuel)
        self.__collection_of_fuel[fuel.get_fuel_name()] = fuel

    def __validate(self, fuel: Fuel):
        if fuel.get_fuel_name() in self.__collection_of_fuel:
            raise FuelAlreadyExistException()

    def get_number_of_fuel(self):
        return len(self.__collection_of_fuel)

    def get_fuel(self):

        return self.__collection_of_fuel

    def update_fuel_price(self, name : str, price: float):
       self.__validate_fuel_exist(name)
       self.__collection_of_fuel.get(name).set_price(price)

    def __validate_fuel_exist(self, fuel_name: str):
        if  self.__collection_of_fuel.get(fuel_name) is None:
            raise FuelDoesNotExistException()

    def restock_fuel(self, name:str, quantity: float):
        self.__validate_fuel_exist(name)
        available_quantity = self.__collection_of_fuel.get(name).get_quantity()
        self.__collection_of_fuel.get(name).set_quantity(available_quantity  + quantity)

    def dispense_fuel_by_amount(self, name: str, amount: float):
        self.__validate_fuel_exist(name)
        liter_ordered = self.__calculate_liter(name, amount)
        self.__validate_available_fuel_quantity(name,liter_ordered)
        quantity = self.__collection_of_fuel.get(name).get_quantity()
        self.__collection_of_fuel.get(name).set_quantity(quantity - liter_ordered)


    def __calculate_liter(self, name: str, amount: float):
        liter = self.__collection_of_fuel.get(name).get_price()
        liter_bought = f"{amount / liter:.1f}"
        return float(liter_bought)

    def __validate_available_fuel_quantity(self,name, liter):
        if liter > self.__collection_of_fuel.get(name).get_quantity():
            raise InsufficientStockException

    def dispense_fuel_by_liter(self, name, liter):
        self.__validate_fuel_exist(name)
        self.__validate_available_fuel_quantity(name,liter)
        quantity = self.__collection_of_fuel.get(name).get_quantity()
        self.__collection_of_fuel.get(name).set_quantity(quantity - liter)
        price_per_liter = self.__collection_of_fuel.get(name).get_price()
        receipt = Receipt(name,price_per_liter, liter)
        self.__list_of_transactions.append(receipt)
        return receipt



    def __generate_receipt(self, name, price_per_liter,liter,):
        receipt = Receipt(name,price_per_liter, liter)
        return receipt

    def get_transactions(self):
        return self.__list_of_transactions