from car import Car
from car_array import CarArray

print("Car Rental Management System")

# Create an array with space for 25 cars.
fleet = CarArray()

# Add two sample cars.
fleet.add(Car("ABC-123", "Toyota", "Yaris", 40))
fleet.add(Car("DEF-456", "Ford", "Focus", 50))

# Display the cars stored in the array.
for i in range(fleet.size):
    car = fleet.cars[i]
    print(car.plate, car.brand, car.model, car.daily_price)

print("Total cars:", fleet.size)

# Test searching for an existing car.
found = fleet.linear_search("ABC-123")

if found is not None:
    print("Found:", found.brand, found.model)
else:
    print("Car not found")

# Test searching for a plate that is not stored.
missing = fleet.linear_search("XYZ-999")
print("Missing car:", missing)

# Test removing an existing car.
removed = fleet.remove("ABC-123")
print("Car removed:", removed)
print("Total cars after removal:", fleet.size)

# Check that the removed car can no longer be found.
print("Search after removal:", fleet.linear_search("ABC-123"))
from sorting import bubble_sort

# Sort sample cars from cheapest to most expensive.
cars = [
    Car("AAA-111", "Ford", "Focus", 50),
    Car("BBB-222", "Nissan", "Micra", 35),
    Car("CCC-333", "Toyota", "Yaris", 40),
]

sorted_cars = bubble_sort(cars)

for car in sorted_cars:
    print(car.brand, car.model, car.daily_price)

assert [car.daily_price for car in sorted_cars] == [35, 40, 50]
assert [car.daily_price for car in cars] == [50, 35, 40]

print("Bubble Sort tests: PASS")

from sorting import insertion_sort

# Check price order and preservation of the original list.
insertion_result = insertion_sort(cars)

assert [car.daily_price for car in insertion_result] == [35, 40, 50]
assert [car.daily_price for car in cars] == [50, 35, 40]

print("Insertion Sort tests: PASS")
from sorting import merge_sort

# Check price order and preservation of the original list.
merge_result = merge_sort(cars)

assert [car.daily_price for car in merge_result] == [35, 40, 50]
assert [car.daily_price for car in cars] == [50, 35, 40]

print("Merge Sort tests: PASS")
from searching import binary_search

# Search for a price after sorting the cars.
ordered_cars = merge_sort(cars)
found = binary_search(ordered_cars, 40)

assert found is not None
assert found.daily_price == 40

# Check a price that does not exist.
assert binary_search(ordered_cars, 99) is None

print("Binary Search tests: PASS")
from rental_history import RentalHistory

# Create and display two rental records.
history = RentalHistory()
history.add("ABC-123", "Anna", 3)
history.add("DEF-456", "Nikos", 5)

history.display()

from action_stack import ActionStack
from rental_queue import RentalQueue

# Show that the latest action is removed first.
actions = ActionStack()
actions.push("Rent ABC-123")
actions.push("Return DEF-456")

print("\nLatest action:", actions.pop())

# Show that rental requests are served in arrival order.
requests = RentalQueue()
requests.enqueue("Anna")
requests.enqueue("Nikos")

print("First customer:", requests.dequeue())
print("Next customer:", requests.dequeue())
from car_bst import CarBST
from car_avl import CarAVL
from car_hash_table import CarHashTable

# Store the same cars in three different search structures.
for structure in [CarBST(), CarAVL(), CarHashTable()]:
    for car in cars:
        structure.insert(car)

    found = structure.search("CCC-333")

    print(
        type(structure).__name__,
        "found:",
        found.brand,
        found.model,
    )
from binary_tree import CategoryTree

# Display the three ways of traversing the category tree.
categories = CategoryTree()

print("\nIn-order:", categories.in_order())
print("Pre-order:", categories.pre_order())
print("Post-order:", categories.post_order())    