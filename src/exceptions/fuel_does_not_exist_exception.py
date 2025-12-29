
class FuelDoesNotExistException(Exception):
    def __init__(self):
        super().__init__("Fuel does not exist")