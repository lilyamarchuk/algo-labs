from collections import defaultdict


def read_input():
    f = open('ijones.in', 'r')
    data = f.read().split()
    f.close()
    idx = 0
    w = int(data[idx])
    idx += 1
    h = int(data[idx])
    idx += 1
    grid = []
    i = 0
    while i < h:
        grid.append(data[idx])
        idx += 1
        i += 1
    return w, h, grid


def solve():
    w, h, grid = read_input()

    dp = []
    r = 0
    while r < h:
        row = []
        c = 0
        while c < w:
            row.append(0)
            c += 1
        dp.append(row)
        r += 1

    r = 0
    while r < h:
        dp[r][0] = 1
        r += 1

    char_sum = defaultdict(int)
    r = 0
    while r < h:
        char_sum[grid[r][0]] = char_sum[grid[r][0]] + dp[r][0]
        r += 1

    c = 1
    while c < w:
        r = 0
        while r < h:
            ch = grid[r][c]
            jump = char_sum[ch]
            if grid[r][c - 1] == ch:
                jump = jump - dp[r][c - 1]
            dp[r][c] = dp[r][c - 1] + jump
            r += 1

        r = 0
        while r < h:
            char_sum[grid[r][c]] = char_sum[grid[r][c]] + dp[r][c]
            r += 1

        c += 1

    if h == 1:
        ans = dp[0][w - 1]
    else:
        ans = dp[0][w - 1] + dp[h - 1][w - 1]

    f = open('ijones.out', 'w')
    f.write(str(ans) + "\n")
    f.close()


solve()