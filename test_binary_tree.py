from binary_tree import CategoryTree

# Check all three traversal orders.
tree = CategoryTree()

assert tree.in_order() == ["Economy", "Cars", "Premium"]
assert tree.pre_order() == ["Cars", "Economy", "Premium"]
assert tree.post_order() == ["Economy", "Premium", "Cars"]

# Check an empty tree.
tree.root = None

assert tree.in_order() == []
assert tree.pre_order() == []
assert tree.post_order() == []

print("Binary Tree tests: PASS")