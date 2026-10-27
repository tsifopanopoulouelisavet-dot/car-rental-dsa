# Store cars in buckets based on their plates.
class CarHashTable:
    def __init__(self):
        self.buckets = [[] for _ in range(25)]

    # Convert a plate into a bucket index.
    def hash_function(self, plate):
        total = 0

        for character in plate:
            total += ord(character)

        return total % len(self.buckets)
        # Add a car to its bucket and reject duplicate plates.
    def insert(self, car):
        index = self.hash_function(car.plate)
        bucket = self.buckets[index]

        for stored_car in bucket:
            if stored_car.plate == car.plate:
                raise ValueError("Plate already exists")

        bucket.append(car)
        # Search for a car inside its bucket.
    def search(self, plate):
        index = self.hash_function(plate)

        for car in self.buckets[index]:
            if car.plate == plate:
                return car

        return None    