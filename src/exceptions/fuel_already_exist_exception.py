class FuelAlreadyExistException(Exception):
    def __init__(self):
        super().__init__("Fuel already exist")