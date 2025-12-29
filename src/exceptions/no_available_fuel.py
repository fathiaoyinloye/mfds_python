class NoAvailableFuel(Exception):
    def __init__(self):
        super().__init__("No available fuel")