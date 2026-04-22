def build_graph(n, edges):
    graph = {i: [] for i in range(1, n + 1)}
    for u, v, w in edges:
        graph[u].append(( v, w))
        graph[v].append((u, w))
    return graph


def dijkstra(start, graph, n):
    dist = {i: float("inf") for i in range(1, n + 1)}
    dist[start] = 0
    visited = set()

    for _ in range(n):
        u = None
        for node in range(1, n + 1):
            if node not in visited and (u is None or dist[node] < dist[u]):
                u = node
        if dist[u] == float("inf"):
            break
        visited.add(u)
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    return dist


def solve(n, clients, edges):
    client_set = set(clients)
    non_clients = [i for i in range(1, n + 1) if i not in client_set]
    graph = build_graph(n, edges)
    best = float("inf")
    for candidate in non_clients:
        dist = dijkstra(candidate, graph, n)
        max_latency = max(dist[c] for c in clients)
        if max_latency < best:
            best = max_latency
    return best
