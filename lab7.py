import csv

def read_adjacency_matrix(filename):
    matrix = []
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            matrix.append([int(x) for x in row])
    return matrix


def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]


def union(parent, rank, x, y):
    rx, ry = find(parent, x), find(parent, y)
    if rank[rx] < rank[ry]:
        parent[rx] = ry
    elif rank[rx] > rank[ry]:
        parent[ry] = rx
    else:
        parent[ry] = rx
        rank[rx] += 1


def minimum_spanning_tree(matrix):
    n = len(matrix)
    if n == 0:
        return 0

    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] > 0:
                edges.append((matrix[i][j], i, j))

    edges.sort()

    parent = list(range(n))
    rank = [0] * n
    total = 0
    edge_count = 0

    for weight, u, v in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            total += weight
            edge_count += 1
            if edge_count == n - 1:
                break

    return total


def main():
    matrix = read_adjacency_matrix('islands.csv')
    result = minimum_spanning_tree(matrix)
    print(result)


if __name__ == '__main__':
    main()