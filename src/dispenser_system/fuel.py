
class Fuel:
    def __init__(self, fuel_name: str, price: float,quantity:float):
        self.__fuel_name = fuel_name
        self.__price_per_liters = price
        self.__quantity = quantity

    def set_fuel_name(self, fuel_name):
        self.__fuel_name = fuel_name

    def set_price(self, price_per_liters):
        self.__price_per_liters = price_per_liters

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def get_fuel_name(self):
        return self.__fuel_name

    def get_price(self):
        return self.__price_per_liters

    def get_quantity(self):
        return self.__quantity






