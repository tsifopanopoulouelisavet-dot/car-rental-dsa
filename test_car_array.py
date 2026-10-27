from car_array import CarArray

# Check searching and removing from an empty array.
fleet = CarArray()

assert fleet.size == 0
assert fleet.linear_search("ABC-123") is None
assert fleet.remove("ABC-123") is False

print("Empty array tests: PASS")
from car import Car

# Check adding and finding a car.
car1 = Car("ABC-123", "Toyota", "Yaris", 40)
fleet.add(car1)

assert fleet.size == 1
assert fleet.linear_search("ABC-123") is car1
assert fleet.linear_search("XYZ-999") is None

print("Add and search tests: PASS")

# Check removal and the position of the remaining car.
car2 = Car("DEF-456", "Ford", "Focus", 50)
fleet.add(car2)

assert fleet.remove("ABC-123") is True
assert fleet.size == 1
assert fleet.cars[0] is car2
assert fleet.cars[1] is None
assert fleet.linear_search("ABC-123") is None
assert fleet.remove("XYZ-999") is False
assert fleet.size == 1

print("Removal tests: PASS")

# Fill all 25 positions.
full_fleet = CarArray()

for i in range(25):
    full_fleet.add(Car(f"CAR-{i}", "Toyota", "Yaris", 40))

assert full_fleet.size == 25

# Check that adding a 26th car raises an error.
try:
    full_fleet.add(Car("EXTRA-1", "Ford", "Focus", 50))
except OverflowError:
    pass
else:
    raise AssertionError("A 26th car was incorrectly accepted")

assert full_fleet.size == 25
assert full_fleet.linear_search("EXTRA-1") is None

print("Full array tests: PASS")

# Check that removing a car frees space for another.
assert full_fleet.remove("CAR-12") is True

replacement = Car("NEW-123", "Nissan", "Micra", 35)
full_fleet.add(replacement)

assert full_fleet.size == 25
assert full_fleet.linear_search("CAR-12") is None
assert full_fleet.linear_search("NEW-123") is replacement

# Check that the other cars are still stored correctly.
for i in range(25):
    if i != 12:
        assert full_fleet.linear_search(f"CAR-{i}") is not None

print("Reuse space tests: PASS")