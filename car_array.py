# Store up to 25 cars in a fixed-capacity array.
class CarArray:
    def __init__(self, capacity=25):
        self.cars = [None] * capacity
        self.size = 0

    # Add a car to the next free position.
    def add(self, car):
        if self.size == len(self.cars):
            raise OverflowError("Car array is full")

        self.cars[self.size] = car
        self.size += 1
        # Find a car by checking each plate in order.
    def linear_search(self, plate):
        for i in range(self.size):
            if self.cars[i].plate == plate:
                return self.cars[i]

        return None  
        # Remove a car and shift the remaining cars left.
    def remove(self, plate):
        for i in range(self.size):
            if self.cars[i].plate == plate:
                for j in range(i, self.size - 1):
                    self.cars[j] = self.cars[j + 1]

                self.size -= 1
                self.cars[self.size] = None
                return True

        return False  