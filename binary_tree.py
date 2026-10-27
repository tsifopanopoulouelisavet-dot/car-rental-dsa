# Store a category with up to two child nodes.
class CategoryNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


# Create a sample binary tree of car categories.
class CategoryTree:
    def __init__(self):
        self.root = CategoryNode("Cars")
        self.root.left = CategoryNode("Economy")
        self.root.right = CategoryNode("Premium")
        # Visit left child, current node, then right child.
    def in_order(self):
        result = []

        def visit(node):
            if node is not None:
                visit(node.left)
                result.append(node.name)
                visit(node.right)

        visit(self.root)
        return result    
        # Visit current node, left child, then right child.
    def pre_order(self):
        result = []

        def visit(node):
            if node is not None:
                result.append(node.name)
                visit(node.left)
                visit(node.right)

        visit(self.root)
        return result
        # Visit left child, right child, then current node.
    def post_order(self):
        result = []

        def visit(node):
            if node is not None:
                visit(node.left)
                visit(node.right)
                result.append(node.name)

        visit(self.root)
        return result