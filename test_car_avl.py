from car import Car
from car_avl import CarAVL

# Trigger right, left and both double rotations.
cases = [
    ["CCC-333", "BBB-222", "AAA-111"],
    ["AAA-111", "BBB-222", "CCC-333"],
    ["CCC-333", "AAA-111", "BBB-222"],
    ["AAA-111", "CCC-333", "BBB-222"],
]

for plates in cases:
    tree = CarAVL()

    for plate in plates:
        tree.insert(Car(plate, "Toyota", "Yaris", 40))

    # All four cases should produce the same balanced tree.
    assert tree.root.car.plate == "BBB-222"
    assert tree.root.left.car.plate == "AAA-111"
    assert tree.root.right.car.plate == "CCC-333"
    assert tree.root.height == 2

    for plate in plates:
        assert tree.search(plate).plate == plate

    assert tree.search("ZZZ-999") is None

print("AVL rotation tests: PASS")
# Check searching in an empty AVL tree.
empty_tree = CarAVL()
assert empty_tree.search("AAA-111") is None

# Check that a duplicate plate is rejected.
original = tree.search("BBB-222")

try:
    tree.insert(Car("BBB-222", "Honda", "Civic", 60))
except ValueError:
    pass
else:
    raise AssertionError("Duplicate plate was accepted")

assert tree.search("BBB-222") is original

print("AVL empty and duplicate tests: PASS")
# Insert 25 cars in ascending plate order.
large_tree = CarAVL()

for i in range(25):
    plate = f"CAR-{i:03d}"
    large_tree.insert(Car(plate, "Toyota", "Yaris", 40))


# Check balance and stored height at every node.
def check_balance(node):
    if node is None:
        return 0

    left_height = check_balance(node.left)
    right_height = check_balance(node.right)

    assert abs(left_height - right_height) <= 1
    assert node.height == 1 + max(left_height, right_height)

    return node.height


check_balance(large_tree.root)

for i in range(25):
    plate = f"CAR-{i:03d}"
    assert large_tree.search(plate).plate == plate

print("AVL 25 cars tests: PASS")