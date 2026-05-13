import unittest
import subprocess
import sys
import os


def run_solution(input_str):
    f = open('ijones.in', 'w')
    f.write(input_str)
    f.close()

    subprocess.run([sys.executable, 'lab8.py'])

    f = open('ijones.out', 'r')
    result = f.read().strip()
    f.close()

    os.remove('ijones.in')
    os.remove('ijones.out')

    return result


class TestIJones(unittest.TestCase):

    def test_example1(self):
        result = run_solution("3 3\naaa\ncab\ndef")
        self.assertEqual(result, "5")

    def test_example2(self):
        result = run_solution("10 1\nabcdefaghi")
        self.assertEqual(result, "2")

    def test_example3(self):
        result = run_solution("7 6\naaaaaaa\naaaaaaa\naaaaaaa\naaaaaaa\naaaaaaa\naaaaaaa")
        self.assertEqual(result, "201684")

    def test_single_cell(self):
        result = run_solution("1 1\na")
        self.assertEqual(result, "1")

    def test_single_row_no_jumps(self):
        result = run_solution("4 1\nabcd")
        self.assertEqual(result, "1")

    def test_single_column(self):
        result = run_solution("1 3\na\nb\nc")
        self.assertEqual(result, "2")

    def test_all_same_two_cols_one_row(self):
        result = run_solution("2 1\naa")
        self.assertEqual(result, "1")

    def test_two_rows_all_same(self):
        result = run_solution("3 2\naaa\naaa")
        self.assertEqual(result, "12")

    def test_no_jumps_possible(self):
        result = run_solution("3 2\nabc\ndef")
        self.assertEqual(result, "2")

    def test_three_rows_unique_letters(self):
        result = run_solution("2 3\nab\ncd\nef")
        self.assertEqual(result, "2")


if __name__ == '__main__':
    unittest.main()