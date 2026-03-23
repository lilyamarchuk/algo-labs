import unittest
from lab3 import BinaryTree, find_successor


class TestFindSuccessor(unittest.TestCase):

    def setUp(self):
        self.root = BinaryTree(10)
        self.root.left = BinaryTree(5, parent=self.root)
        self.root.right = BinaryTree(15, parent=self.root)
        self.root.left.left = BinaryTree(3, parent=self.root.left)
        self.root.left.right = BinaryTree(7, parent=self.root.left)
        self.root.right.right = BinaryTree(20, parent=self.root.right)
        self.root.right.right.left = BinaryTree(12, parent=self.root.right.right)

    def test_node_with_right_subtree(self):
        result = find_successor(self.root, self.root.left)
        self.assertEqual(result.value, 7)

    def test_go_up_to_parent(self):
        result = find_successor(self.root, self.root.left.right)
        self.assertEqual(result.value, 10)

    def test_root_successor(self):
        result = find_successor(self.root, self.root)
        self.assertEqual(result.value, 15)

    def test_leftmost_node(self):
        result = find_successor(self.root, self.root.left.left)
        self.assertEqual(result.value, 5)

    def test_largest_node_returns_none(self):
        result = find_successor(self.root, self.root.right.right)
        self.assertIsNone(result)

    def test_node_with_left_child_in_right_subtree(self):
        result = find_successor(self.root, self.root.right)
        self.assertEqual(result.value, 12)


if __name__ == '__main__':
    unittest.main()