from statistics import median
from time import perf_counter

from binary_tree import CategoryNode, CategoryTree


# Build a balanced binary tree with the requested node count.
def create_tree(count):
    def build(start, end):
        if start >= end:
            return None

        middle = (start + end) // 2
        node = CategoryNode(f"Category-{middle}")
        node.left = build(start, middle)
        node.right = build(middle + 1, end)
        return node

    tree = CategoryTree()
    tree.root = build(0, count)
    return tree
# Compare traversal times on the same tree.
for count in [25, 100, 500]:
    tree = create_tree(count)
    expected = {f"Category-{i}" for i in range(count)}

    print(f"\nNodes: {count}")

    for traversal in [tree.in_order, tree.pre_order, tree.post_order]:
        times = []

        # Repeat each measurement to reduce timing noise.
        for repeat in range(5):
            start = perf_counter()

            for run in range(100):
                result = traversal()

            elapsed = (perf_counter() - start) / 100

            # Check that every node was visited exactly once.
            assert len(result) == count
            assert set(result) == expected
            times.append(elapsed)

        milliseconds = median(times) * 1000
        print(f"{traversal.__name__}: {milliseconds:.4f} ms")