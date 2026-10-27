from car import Car
from car_bst import CarBST

# Check searching in an empty tree.
tree = CarBST()
assert tree.search("BBB-222") is None

# Insert a root, a left child and a right child.
car1 = Car("BBB-222", "Toyota", "Yaris", 40)
car2 = Car("AAA-111", "Nissan", "Micra", 35)
car3 = Car("CCC-333", "Ford", "Focus", 50)

tree.insert(car1)
tree.insert(car2)
tree.insert(car3)

# Check placement and searching.
assert tree.root.car is car1
assert tree.root.left.car is car2
assert tree.root.right.car is car3

assert tree.search("BBB-222") is car1
assert tree.search("AAA-111") is car2
assert tree.search("CCC-333") is car3
assert tree.search("ZZZ-999") is None

print("Car BST tests: PASS")
from car import Car
from car_bst import CarBST

# Check searching in an empty tree.
tree = CarBST()
assert tree.search("BBB-222") is None

# Insert a root, a left child and a right child.
car1 = Car("BBB-222", "Toyota", "Yaris", 40)
car2 = Car("AAA-111", "Nissan", "Micra", 35)
car3 = Car("CCC-333", "Ford", "Focus", 50)

tree.insert(car1)
tree.insert(car2)
tree.insert(car3)

# Check placement and searching.
assert tree.root.car is car1
assert tree.root.left.car is car2
assert tree.root.right.car is car3

assert tree.search("BBB-222") is car1
assert tree.search("AAA-111") is car2
assert tree.search("CCC-333") is car3
assert tree.search("ZZZ-999") is None

print("Car BST tests: PASS")
# Check that a duplicate plate is rejected.
duplicate = Car("BBB-222", "Honda", "Civic", 60)

try:
    tree.insert(duplicate)
except ValueError:
    pass
else:
    raise AssertionError("Duplicate plate was accepted")

# Check that the original car is still stored.
assert tree.search("BBB-222") is car1

print("Duplicate plate test: PASS")
# Check that in-order traversal sorts cars by plate.
ordered = tree.in_order()

assert [car.plate for car in ordered] == [
    "AAA-111",
    "BBB-222",
    "CCC-333",
]

# Check traversal of an empty tree.
assert CarBST().in_order() == []

print("BST traversal tests: PASS")