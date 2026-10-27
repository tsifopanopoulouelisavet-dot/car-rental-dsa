# Store a car and links to its left and right children.
class CarNode:
    def __init__(self, car):
        self.car = car
        self.left = None
        self.right = None


# Organize cars by plate in a binary search tree.
class CarBST:
    def __init__(self):
        self.root = None

    # Insert a car according to its plate.
    def insert(self, car):
        if self.root is None:
            self.root = CarNode(car)
            return

        current = self.root

        while True:
            if car.plate == current.car.plate:
                raise ValueError("Plate already exists")

            if car.plate < current.car.plate:
                if current.left is None:
                    current.left = CarNode(car)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = CarNode(car)
                    return
                current = current.right
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
        # Return cars in ascending plate order.
    def in_order(self):
        result = []

        def visit(node):
            if node is not None:
                visit(node.left)
                result.append(node.car)
                visit(node.right)

        visit(self.root)
        return result