import unittest
from lab1 import zigzag_traversal

class TestZigzag(unittest.TestCase):
    def test_5x5(self):
        matrix = [[(i * 5 + j + 1) for j in range(5)] for i in range(5)]
        self.assertEqual(len(zigzag_traversal(matrix)), 25)

    def test_2x4(self):
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]
        expected = [1, 2, 5, 6, 3, 4, 7, 8]
        self.assertEqual(zigzag_traversal(matrix), expected)

    def test_6x1(self):
        matrix = [[1], [2], [3], [4], [5], [6]]
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(zigzag_traversal(matrix), expected)

    def test_1x1(self):
        self.assertEqual(zigzag_traversal([[1]]), [1])

    def test_3x5_from_task(self):
        matrix = [
            [1, 2, 6, 7, 12],
            [3, 5, 8, 11, 13],
            [4, 9, 10, 14, 15]
        ]
        res = zigzag_traversal(matrix)
        self.assertEqual(len(res), 15)

if __name__ == '__main__':
    unittest.main()