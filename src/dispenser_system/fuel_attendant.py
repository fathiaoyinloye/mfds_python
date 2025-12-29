from .dispenser import Dispenser
from .fuel import Fuel


class FuelAttendant:
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__transactions_on_dispenser = []


    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_transactions_on_dispenser(self):
        return self.__transactions_on_dispenser

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def add_a_new_fuel(self, fuel_name, price_per_liters, quantity, dispenser: Dispenser):
        fuel = Fuel(fuel_name, price_per_liters, quantity)
        dispenser.add_fuel(fuel)

    def get_available_fuel(self, dispenser: Dispenser):
        return dispenser.get_fuel()

    def update_fuel_price(self,name: str, price: float, dispenser: Dispenser):
        dispenser.update_fuel_price(name, price)
        return f"{name} Fuel updated successfully"

    def restock_fuel(self, name: str, quantity: float, dispenser: Dispenser):
        dispenser.restock_fuel(name, quantity)
        return f"{name} Fuel restocked successfully"

    def dispense_fuel_by_amount(self, name: str, amount: float, dispenser: Dispenser):
        dispenser.dispense_fuel_by_amount(name, amount)

    def dispense_fuel_by_liter(self, name: str, amount: float, dispenser: Dispenser):
      receipt =  dispenser.dispense_fuel_by_liter(name, amount)
      return receipt

