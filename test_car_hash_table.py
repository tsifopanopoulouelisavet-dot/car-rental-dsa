from car import Car
from car_hash_table import CarHashTable

# Check searching in an empty table.
table = CarHashTable()
assert table.search("ABC-123") is None

# These plates have the same character sum.
car1 = Car("ABC-123", "Toyota", "Yaris", 40)
car2 = Car("CBA-123", "Ford", "Focus", 50)

assert table.hash_function(car1.plate) == table.hash_function(car2.plate)

# Check that both cars remain searchable despite the collision.
table.insert(car1)
table.insert(car2)

assert table.search("ABC-123") is car1
assert table.search("CBA-123") is car2
assert table.search("XYZ-999") is None

print("Hash Table collision tests: PASS")
# Check that a duplicate plate is rejected.
duplicate = Car("ABC-123", "Honda", "Civic", 60)

try:
    table.insert(duplicate)
except ValueError:
    pass
else:
    raise AssertionError("Duplicate plate was accepted")

# Check that both original cars remain stored.
assert table.search("ABC-123") is car1
assert table.search("CBA-123") is car2

print("Hash Table duplicate test: PASS")