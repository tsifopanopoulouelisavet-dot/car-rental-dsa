from car import Car
from searching import binary_search

# Check an empty list.
assert binary_search([], 40) is None

# Check a list containing one car.
single = [Car("AAA-111", "Toyota", "Yaris", 40)]
assert binary_search(single, 40) is single[0]
assert binary_search(single, 35) is None

# Check first, middle and last prices in a sorted list.
cars = [
    Car("BBB-222", "Nissan", "Micra", 35),
    Car("CCC-333", "Toyota", "Yaris", 40),
    Car("DDD-444", "Ford", "Focus", 50),
]

for car in cars:
    assert binary_search(cars, car.daily_price) is car

# Check missing prices below, between and above stored prices.
for price in [20, 45, 60]:
    assert binary_search(cars, price) is None

print("Binary Search edge tests: PASS")