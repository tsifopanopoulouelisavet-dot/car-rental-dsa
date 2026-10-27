# Stores each car's details and availability.
class Car:
    def __init__(self, plate, brand, model, daily_price):
        self.plate = plate
        self.brand = brand
        self.model = model
        self.daily_price = daily_price
        self.available = True