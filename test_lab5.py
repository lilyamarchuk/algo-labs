import unittest

def flood_fill(grid, row, col, replacement_color):
    rows = len(grid)
    cols = len(grid[0])
    target_color = grid[row][col]

    if target_color == replacement_color:
        return grid

    queue = [(row, col)]
    grid[row][col] = replacement_color

    while queue:
        r, c = queue.pop(0)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == target_color:
                grid[nr][nc] = replacement_color
                queue.append((nr, nc))

    return grid


def read_input(filename):
    with open(filename) as f:
        lines = [line.strip() for line in f if line.strip()]

    h, w = map(int, lines[0].split(','))
    row, col = map(int, lines[1].split(','))
    replacement_color = lines[2].strip("'\"")

    grid = []
    for i in range(3, 3 + h):
        cells = [c.strip().strip("'\"") for c in lines[i].strip('[]').split(',')]
        grid.append(cells)

    return grid, row, col, replacement_color


def write_output(filename, grid):
    with open(filename, 'w') as f:
        for row in grid:
            f.write('[' + ', '.join(f"'{c}'" for c in row) + ']\n')


class TestFloodFill(unittest.TestCase):

    def sample_grid(self):
        return [
            ['Y','Y','Y','G','G','G','G','G','G','G'],
            ['Y','Y','Y','Y','Y','Y','G','X','X','X'],
            ['G','G','G','G','G','G','G','X','X','X'],
            ['W','W','W','W','W','G','G','G','G','X'],
            ['W','R','R','R','R','R','G','X','X','X'],
            ['W','W','W','R','R','G','G','X','X','X'],
            ['W','B','W','R','R','R','R','R','R','X'],
            ['W','B','B','B','B','R','R','X','X','X'],
            ['W','B','B','X','B','B','B','B','X','X'],
            ['W','B','B','X','X','X','X','X','X','X'],
        ]

    def expected_grid(self):
        return [
            ['Y','Y','Y','G','G','G','G','G','G','G'],
            ['Y','Y','Y','Y','Y','Y','G','C','C','C'],
            ['G','G','G','G','G','G','G','C','C','C'],
            ['W','W','W','W','W','G','G','G','G','C'],
            ['W','R','R','R','R','R','G','C','C','C'],
            ['W','W','W','R','R','G','G','C','C','C'],
            ['W','B','W','R','R','R','R','R','R','C'],
            ['W','B','B','B','B','R','R','C','C','C'],
            ['W','B','B','C','B','B','B','B','C','C'],
            ['W','B','B','C','C','C','C','C','C','C'],
        ]

    def test_example_from_task(self):
        result = flood_fill(self.sample_grid(), 3, 9, 'C')
        self.assertEqual(result, self.expected_grid())

    def test_same_color_no_change(self):
        grid = [['R','R'],['R','G']]
        self.assertEqual(flood_fill(grid, 0, 0, 'R'), [['R','R'],['R','G']])

    def test_single_cell(self):
        self.assertEqual(flood_fill([['A']], 0, 0, 'B'), [['B']])

    def test_entire_grid_same_color(self):
        grid = [['A','A'],['A','A']]
        self.assertEqual(flood_fill(grid, 0, 0, 'Z'), [['Z','Z'],['Z','Z']])

    def test_barrier_not_crossed(self):
        grid = [['A','B','A'],['A','B','A'],['A','B','A']]
        result = flood_fill(grid, 0, 0, 'Z')
        self.assertEqual(result, [['Z','B','A'],['Z','B','A'],['Z','B','A']])

    def test_diagonal_not_connected(self):
        grid = [['A','B'],['B','A']]
        self.assertEqual(flood_fill(grid, 0, 0, 'Z'), [['Z','B'],['B','A']])

    def test_top_left_corner(self):
        grid = [['X','X','O'],['X','O','O'],['O','O','O']]
        self.assertEqual(flood_fill(grid, 0, 0, 'F'), [['F','F','O'],['F','O','O'],['O','O','O']])

    def test_bottom_right_corner(self):
        grid = [['O','X'],['X','X']]
        self.assertEqual(flood_fill(grid, 1, 1, 'Z'), [['O','Z'],['Z','Z']])

    def test_read_input(self):
        with open('_test_input.txt', 'w') as f:
            f.write(
                "10,10\n3,9\n'C'\n"
                "['Y','Y','Y','G','G','G','G','G','G','G']\n"
                "['Y','Y','Y','Y','Y','Y','G','X','X','X']\n"
                "['G','G','G','G','G','G','G','X','X','X']\n"
                "['W','W','W','W','W','G','G','G','G','X']\n"
                "['W','R','R','R','R','R','G','X','X','X']\n"
                "['W','W','W','R','R','G','G','X','X','X']\n"
                "['W','B','W','R','R','R','R','R','R','X']\n"
                "['W','B','B','B','B','R','R','X','X','X']\n"
                "['W','B','B','X','B','B','B','B','X','X']\n"
                "['W','B','B','X','X','X','X','X','X','X']\n"
            )
        grid, row, col, color = read_input('_test_input.txt')
        self.assertEqual(row, 3)
        self.assertEqual(col, 9)
        self.assertEqual(color, 'C')
        self.assertEqual(len(grid), 10)
        self.assertEqual(grid[0][0], 'Y')
        self.assertEqual(grid[3][9], 'X')

    def test_write_output(self):
        write_output('_test_output.txt', [['A','B'],['C','D']])
        with open('_test_output.txt') as f:
            lines = f.read().splitlines()
        self.assertEqual(lines[0], "['A', 'B']")
        self.assertEqual(lines[1], "['C', 'D']")

    def test_full_pipeline(self):
        with open('_test_input.txt', 'w') as f:
            f.write(
                "10,10\n3,9\n'C'\n"
                "['Y','Y','Y','G','G','G','G','G','G','G']\n"
                "['Y','Y','Y','Y','Y','Y','G','X','X','X']\n"
                "['G','G','G','G','G','G','G','X','X','X']\n"
                "['W','W','W','W','W','G','G','G','G','X']\n"
                "['W','R','R','R','R','R','G','X','X','X']\n"
                "['W','W','W','R','R','G','G','X','X','X']\n"
                "['W','B','W','R','R','R','R','R','R','X']\n"
                "['W','B','B','B','B','R','R','X','X','X']\n"
                "['W','B','B','X','B','B','B','B','X','X']\n"
                "['W','B','B','X','X','X','X','X','X','X']\n"
            )
        grid, row, col, color = read_input('_test_input.txt')
        write_output('_test_output.txt', flood_fill(grid, row, col, color))
        with open('_test_output.txt') as f:
            lines = f.read().splitlines()
        self.assertEqual(lines, [
            "['Y', 'Y', 'Y', 'G', 'G', 'G', 'G', 'G', 'G', 'G']",
            "['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'G', 'C', 'C', 'C']",
            "['G', 'G', 'G', 'G', 'G', 'G', 'G', 'C', 'C', 'C']",
            "['W', 'W', 'W', 'W', 'W', 'G', 'G', 'G', 'G', 'C']",
            "['W', 'R', 'R', 'R', 'R', 'R', 'G', 'C', 'C', 'C']",
            "['W', 'W', 'W', 'R', 'R', 'G', 'G', 'C', 'C', 'C']",
            "['W', 'B', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'C']",
            "['W', 'B', 'B', 'B', 'B', 'R', 'R', 'C', 'C', 'C']",
            "['W', 'B', 'B', 'C', 'B', 'B', 'B', 'B', 'C', 'C']",
            "['W', 'B', 'B', 'C', 'C', 'C', 'C', 'C', 'C', 'C']",
        ])


if __name__ == '__main__':
    unittest.main()