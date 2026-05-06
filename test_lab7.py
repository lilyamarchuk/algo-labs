import unittest
import os
import csv

from lab7 import read_adjacency_matrix, minimum_spanning_tree


class TestMinimumSpanningTree(unittest.TestCase):

    def _write_csv(self, filename, matrix):
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            for row in matrix:
                writer.writerow(row)

    def tearDown(self):
        if os.path.exists('test_islands.csv'):
            os.remove('test_islands.csv')

    def test_single_island(self):
        self.assertEqual(minimum_spanning_tree([[0]]), 0)

    def test_two_islands(self):
        matrix = [
            [0, 5],
            [5, 0],
        ]
        self.assertEqual(minimum_spanning_tree(matrix), 5)

    def test_three_islands_triangle(self):
        matrix = [
            [0, 1, 4],
            [1, 0, 2],
            [4, 2, 0],
        ]
        self.assertEqual(minimum_spanning_tree(matrix), 3)

    def test_four_islands(self):
        matrix = [
            [0, 2, 0, 6],
            [2, 0, 3, 8],
            [0, 3, 0, 7],
            [6, 8, 7, 0],
        ]
        self.assertEqual(minimum_spanning_tree(matrix), 11)

    def test_complete_graph_equal_weights(self):
        matrix = [
            [0, 10, 10],
            [10, 0, 10],
            [10, 10, 0],
        ]
        self.assertEqual(minimum_spanning_tree(matrix), 20)

    def test_empty_matrix(self):
        self.assertEqual(minimum_spanning_tree([]), 0)

    def test_five_islands(self):
        matrix = [
            [0, 2, 3, 0, 0],
            [2, 0, 0, 4, 5],
            [3, 0, 0, 0, 6],
            [0, 4, 0, 0, 7],
            [0, 5, 6, 7, 0],
        ]
        self.assertEqual(minimum_spanning_tree(matrix), 14)

    def test_symmetric_matrix(self):
        matrix = [
            [0, 7, 0, 5],
            [7, 0, 8, 9],
            [0, 8, 0, 11],
            [5, 9, 11, 0],
        ]
        self.assertEqual(minimum_spanning_tree(matrix), 20)

    def test_read_csv_simple(self):
        matrix = [[0, 3], [3, 0]]
        self._write_csv('test_islands.csv', matrix)
        result = read_adjacency_matrix('test_islands.csv')
        self.assertEqual(result, matrix)

    def test_read_csv_3x3(self):
        matrix = [
            [0, 1, 4],
            [1, 0, 2],
            [4, 2, 0],
        ]
        self._write_csv('test_islands.csv', matrix)
        result = read_adjacency_matrix('test_islands.csv')
        self.assertEqual(result, matrix)

    def test_read_and_compute(self):
        matrix = [
            [0, 1, 4],
            [1, 0, 2],
            [4, 2, 0],
        ]
        self._write_csv('test_islands.csv', matrix)
        loaded = read_adjacency_matrix('test_islands.csv')
        self.assertEqual(minimum_spanning_tree(loaded), 3)


if __name__ == '__main__':
    unittest.main()