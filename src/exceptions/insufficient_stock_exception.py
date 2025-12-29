class InsufficientStockException(Exception):
    def __init__(self):
        super().__init__("Available Liters Is Insufficient For The Quantity To Be Bought")