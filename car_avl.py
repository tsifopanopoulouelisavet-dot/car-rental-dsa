# Store a car, child links and the node's height.
class AVLNode:
    def __init__(self, car):
        self.car = car
        self.left = None
        self.right = None
        self.height = 1


# Organize cars by plate in a balanced search tree.
class CarAVL:
    def __init__(self):
        self.root = None

    # Return zero for an empty branch.
    def height(self, node):
        if node is None:
            return 0
        return node.height

    # Compare the heights of the left and right branches.
    def balance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)
        # Rotate a branch to the right and update node heights.
    def rotate_right(self, node):
        new_root = node.left
        middle = new_root.right

        new_root.right = node
        node.left = middle

        node.height = 1 + max(
            self.height(node.left), self.height(node.right)
        )
        new_root.height = 1 + max(
            self.height(new_root.left), self.height(new_root.right)
        )

        return new_root
        # Rotate a branch to the left and update node heights.
    def rotate_left(self, node):
        new_root = node.right
        middle = new_root.left

        new_root.left = node
        node.right = middle

        node.height = 1 + max(
            self.height(node.left), self.height(node.right)
        )
        new_root.height = 1 + max(
            self.height(new_root.left), self.height(new_root.right)
        )

        return new_root
        # Insert a car and update the tree's root.
    def insert(self, car):
        self.root = self._insert(self.root, car)

    # Insert recursively and restore balance when needed.
    def _insert(self, node, car):
        if node is None:
            return AVLNode(car)

        if car.plate < node.car.plate:
            node.left = self._insert(node.left, car)
        elif car.plate > node.car.plate:
            node.right = self._insert(node.right, car)
        else:
            raise ValueError("Plate already exists")

        node.height = 1 + max(
            self.height(node.left), self.height(node.right)
        )
        difference = self.balance(node)

        # Fix a branch that is too heavy on the left.
        if difference > 1:
            if self.balance(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Fix a branch that is too heavy on the right.
        if difference < -1:
            if self.balance(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node
        # Find a car by following the appropriate branches.
    def search(self, plate):
        current = self.root

        while current is not None:
            if plate == current.car.plate:
                return current.car
            elif plate < current.car.plate:
                current = current.left
            else:
                current = current.right

        return None