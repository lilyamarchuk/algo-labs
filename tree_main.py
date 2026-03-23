import os

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def load(filename):

    with open(filename, 'r', encoding='utf-8') as f:
        return f.read().split()

def build(tokens):
    stack = list(tokens)
    def _b():

        if not stack: return None
        v = stack.pop()
        if v == '#': return None
        node = Node(v)
        node.right = _b()
        node.left = _b()
        return node
    return _b()

def count(root):

    if not root: return 0
    return 1 + count(root.left) + count(root.right)

def draw(root):
    canvas = {}
    DX = 7

    def _draw(node, x, y, dy, side, is_root=False):


        if not node: return
        canvas[(x, y)] = node.val
        if is_root:

            if node.left:
                for i in range(2, DX): canvas[(x - i, y)] = '-'
                _draw(node.left, x - DX, y, dy, 'L')
            if node.right:
                for i in range(2, DX): canvas[(x + i, y)] = '-'
                _draw(node.right, x + DX, y, dy, 'R')
        else:
            ndy = max(1, dy // 2)
            if side == 'L':
                if node.left:
                    canvas[(x - DX // 2, y - dy)] = '\\'
                    _draw(node.left, x - DX, y - dy * 2, ndy, 'L')
                if node.right:
                    canvas[(x - DX // 2, y + dy)] = '/'
                    _draw(node.right, x - DX, y + dy * 2, ndy, 'L')
            else:
                if node.left:
                    canvas[(x + DX // 2, y - dy)] = '/'
                    _draw(node.left, x + DX, y - dy * 2, ndy, 'R')
                if node.right:
                    canvas[(x + DX // 2, y + dy)] = '\\'
                    _draw(node.right, x + DX, y + dy * 2, ndy, 'R')

    _draw(root, 0, 0, 2, 'L', is_root=True)


    if not canvas: return

    min_x = min(x for x, y in canvas)
    max_x = max(x + len(str(v)) for (x, y), v in canvas.items())
    min_y = min(y for x, y in canvas)
    max_y = max(y for x, y in canvas)

    W = max_x - min_x + 2
    H = max_y - min_y + 1
    grid = [[' '] * W for _ in range(H)]

    for (x, y), v in canvas.items():
        s = str(v)
        r = y - min_y

        for i, ch in enumerate(s):

            c = x - min_x + i
            if 0 <= r < H and 0 <= c < W:
                grid[r][c] = ch

    for row in grid:

        line = ''.join(row).rstrip()
        if line: print(line)

if __name__ == '__main__':

    filename = 'data.txt'
    tokens = load(filename)
    root = build(tokens)
    if root:
        print(f"Вузлів: {count(root)}\n")
        draw(root)
    else:
        print("Дерево порожнє")
