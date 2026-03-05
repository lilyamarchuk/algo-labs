import unittest
from lab2 import max_hamsters


class TestHamsters(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(max_hamsters(7, 3, [[1, 2], [2, 2], [3, 1]]), 2)

    def test_example_2(self):
        self.assertEqual(max_hamsters(19, 4, [[5, 0], [2, 2], [1, 4], [5, 1]]), 3)

    def test_example_3(self):
        self.assertEqual(max_hamsters(2, 2, [[1, 50000], [1, 60000]]), 1)

    def test_example_4(self):
        self.assertEqual(max_hamsters(35, 1, [[1, 2], [3, 4], [5, 7]
        ]), 1)

if __name__ == "__main__":
    unittest.main()