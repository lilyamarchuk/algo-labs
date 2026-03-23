class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def find_successor(_, node):
    if node.right:
        current = node.right
        while current.left:
            current = current.left
        return current

    current = node
    while current.parent:
        if current.parent.left == current:
            return current.parent
        current = current.parent

    return None