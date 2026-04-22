import unittest
from lab6 import solve, dijkstra, build_graph

class TestBuildGraph(unittest.TestCase):
    def test_single_edge(self):
        graph = build_graph(2, [(1, 2, 10)])
        self.assertIn((2, 10), graph[1])
        self.assertIn((1, 10), graph[2])

    def test_bidirectional(self):
        graph = build_graph(3, [(1, 2, 5), (2, 3, 7)])
        self.assertEqual(len(graph[2]), 2)

    def test_empty_edges(self):
        graph = build_graph(3, [])
        self.assertEqual(len(graph[1]), 0)


class TestDijkstra(unittest.TestCase):
    def test_direct_connection(self):
        graph = build_graph(2, [(1, 2, 42)])
        dist = dijkstra(1, graph, 2)
        self.assertEqual(dist[2], 42)

    def test_shortest_path(self):
        graph = build_graph(3, [(1, 2, 10), (2, 3, 10), (1, 3, 100)])
        dist = dijkstra(1, graph, 3)
        self.assertEqual(dist[3], 20)

    def test_start_node_zero(self):
        graph = build_graph(3, [(1, 2, 5)])
        dist = dijkstra(1, graph, 3)
        self.assertEqual(dist[1], 0)

    def test_unreachable_node(self):
        graph = build_graph(3, [(1, 2, 5)])
        dist = dijkstra(1, graph, 3)
        self.assertEqual(dist[3], float("inf"))


class TestSolve(unittest.TestCase):
    def test_example_1(self):
        n = 6
        clients = [1, 2, 6]
        edges = [
            (1, 3, 10),
            (3, 4, 80),
            (4, 5, 50),
            (5, 6, 20),
            (2, 3, 40),
            (2, 4, 100),
        ]
        self.assertEqual(solve(n, clients, edges), 100)

    def test_example_2(self):
        n = 9
        clients = [2, 4, 6]
        edges = [
            (1, 2, 20),
            (2, 3, 20),
            (3, 6, 20),
            (6, 9, 20),
            (9, 8, 20),
            (8, 7, 20),
            (7, 4, 20),
            (4, 1, 20),
            (5, 2, 10),
            (5, 4, 10),
            (5, 6, 10),
            (5, 8, 10),
        ]
        self.assertEqual(solve(n, clients, edges), 10)

    def test_example_3(self):
        n = 3
        clients = [1, 3]
        edges = [(1, 2, 50), (2, 3, 1000000000)]
        self.assertEqual(solve(n, clients, edges), 1000000000)

    def test_single_router_between_two_clients(self):
        n = 3
        clients = [1, 3]
        edges = [(1, 2, 5), (2, 3, 5)]
        self.assertEqual(solve(n, clients, edges), 5)

    def test_server_placement_matters(self):
        n = 4
        clients = [1, 3]
        edges = [(1, 2, 10), (2, 3, 100), (2, 4, 5), (4, 3, 5)]
        result = solve(n, clients, edges)
        self.assertLessEqual(result, 15)

    def test_all_equal_latency(self):
        n = 5
        clients = [1, 2, 3, 4]
        edges = [(5, 1, 10), (5, 2, 10), (5, 3, 10), (5, 4, 10)]
        self.assertEqual(solve(n, clients, edges), 10)

    def test_large_latency(self):
        n = 3
        clients = [1, 2]
        edges = [(3, 1, 10**9), (3, 2, 10**9)]
        self.assertEqual(solve(n, clients, edges), 10**9)

    def test_chain_topology(self):
        n = 5
        clients = [1, 5]
        edges = [(1, 2, 1), (2, 3, 1), (3, 4, 1), (4, 5, 1)]
        self.assertEqual(solve(n, clients, edges), 2)

    def test_star_topology(self):
        n = 5
        clients = [1, 2, 3, 4]
        edges = [(5, 1, 3), (5, 2, 7), (5, 3, 1), (5, 4, 5)]
        self.assertEqual(solve(n, clients, edges), 7)

    def test_multiple_paths_uses_shortest(self):
        n = 4
        clients = [1, 4]
        edges = [(2, 1, 5), (2, 3, 100), (3, 4, 5), (2, 4, 1000)]
        self.assertEqual(solve(n, clients, edges), 105)


if __name__ == "__main__":
    unittest.main()