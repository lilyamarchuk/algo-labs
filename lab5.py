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

    grid_data = []
    for i in range(3, 3 + h):
        cells = [c.strip().strip("'\"") for c in lines[i].strip('[]').split(',')]
        grid_data.append(cells)

    return grid_data, row, col, replacement_color


def write_output(filename, grid):
    with open(filename, 'w') as f:
        for row in grid:
            f.write('[' + ', '.join(f"'{c}'" for c in row) + ']\n')


if __name__ == "__main__":
    loaded_grid, start_row, start_col, new_color = read_input('_test_input.txt')
    result_grid = flood_fill(loaded_grid, start_row, start_col, new_color)
    write_output('_test_output.txt', result_grid)