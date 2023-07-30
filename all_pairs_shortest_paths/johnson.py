import heapq
import sys

from graph import Edge
from graph import Graph
from graph import Vertex
from graph import initialize_single_source
from graph import relax


def bellman_ford(graph, s):
    initialize_single_source(graph, s)

    vertices = graph.vertices
    edges = graph.edges

    print("--- after initializing ---")
    for v in vertices.values():
        print(
            f"name = {v.name} / distance = {v.distance}, predecessor = {v.predecessor}")

    for _ in vertices.values():
        for edge in edges:
            u = vertices[edge.start]
            v = vertices[edge.end]
            weight = edge.weight

            relax(u, v, weight)

    for edge in edges:
        u = vertices[edge.start]
        v = vertices[edge.end]
        weight = edge.weight

        if v.distance > u.distance + weight:
            return True

    return False


def dijkstra(graph, s):
    initialize_single_source(graph, s)

    vertices = graph.vertices
    edges = graph.edges

    vertices_list = list(vertices.values())
    heapq.heapify(vertices_list)

    while len(vertices_list):
        u = heapq.heappop(vertices_list)
        print(f"vertex: {u.name} / distance = {u.distance}")

        adjacency_list = graph.adjacency_list[u.name]
        for name, weight in adjacency_list:
            v = vertices[name]
            relax(u, v, weight)

            heapq.heapify(vertices_list)


def johnson(graph):
    vertices = graph.vertices
    edges = graph.edges

    extended_vertices = vertices.copy()
    extended_vertices['s'] = Vertex('s')
    extended_edges = edges.copy()
    for v in extended_vertices.keys():
        extended_edges.insert(0, Edge('s', v, 0))
    extended_graph = Graph(extended_vertices, extended_edges)

    print("--- extended graph ---")
    extended_graph.print_graph()

    print("--- Bellman-Ford algortithm ---")
    has_cycle = bellman_ford(extended_graph, extended_vertices['s'])
    if has_cycle:
        print("Graph has negative cycle.")

        sys.exit(1)

    h = {}
    for v in extended_vertices.values():
        h[v.name] = v.distance

    for edge in extended_edges:
        u = extended_vertices[edge.start]
        v = extended_vertices[edge.end]

        edge.weight = edge.weight + h[u.name] - h[v.name]

    print("--- Dijkstra's algorithm ---")
    D = [[0 for _ in range(len(vertices))] for _ in range(len(vertices))]
    for s in extended_vertices.values():
        if s.name == 's':
            continue
        print(f"target vertex: {s.name}")

        dijkstra(extended_graph, s)

        for v in extended_vertices.values():
            if s.name == 's' or v.name == 's':
                continue

            i = int(s.name)
            j = int(v.name)
            D[i][j] = v.distance

    return D


def print_matrix(A):
    row = len(A)
    column = len(A[0])

    for i in range(row):
        for j in range(column):
            print(f"{A[i][j]:>3}", " ", end='')
        print("")


if __name__ == '__main__':
    vertices = {}
    for i in range(5):
        vertices[str(i)] = Vertex(str(i))

    edges = []
    edges.append(Edge('0', '1', 3))
    edges.append(Edge('0', '2', 8))
    edges.append(Edge('0', '4', -4))
    edges.append(Edge('1', '3', 1))
    edges.append(Edge('1', '4', 7))
    edges.append(Edge('2', '1', 4))
    edges.append(Edge('3', '0', 2))
    edges.append(Edge('3', '2', -5))
    edges.append(Edge('4', '3', 6))

    graph = Graph(vertices, edges)

    print("--- graph ---")
    graph.print_graph()

    print("--- Johnson's algorithm ---")
    D = johnson(graph)

    print("--- result ---")
    print_matrix(D)
