from graph import Edge
from graph import Graph
from graph import Vertex
from graph import initialize_single_source
from graph import relax

import heapq


def dijkstra(graph, s):
    vertices = graph.vertices
    edges = graph.edges

    initialize_single_source(graph, s)

    vertices_list = list(vertices.values())
    heapq.heapify(vertices_list)

    while len(vertices_list) != 0:
        u = heapq.heappop(vertices_list)

        adjacency = graph.adjacency_list[u.name]
        for v_name, weight in adjacency:
            v = vertices[v_name]

            relax(u, v, weight)

            heapq.heapify(vertices_list)


def collect_predecessors(v):
    results = []

    results.append(v)

    p = v
    while p.predecessor:
        p = p.predecessor

        results.append(p)

    return results[::-1]


if __name__ == '__main__':
    vertices = {}
    vertices['s'] = Vertex('s')
    vertices['t'] = Vertex('t')
    vertices['y'] = Vertex('y')
    vertices['x'] = Vertex('x')
    vertices['z'] = Vertex('z')

    edges = []
    edges.append(Edge('s', 't', 10))
    edges.append(Edge('s', 'y', 5))
    edges.append(Edge('t', 'y', 2))
    edges.append(Edge('t', 'x', 1))
    edges.append(Edge('y', 't', 3))
    edges.append(Edge('y', 'x', 9))
    edges.append(Edge('y', 'z', 2))
    edges.append(Edge('x', 'z', 4))
    edges.append(Edge('z', 's', 7))
    edges.append(Edge('z', 'x', 6))

    graph = Graph(vertices, edges)

    print("--- graph ---")
    graph.print_graph()

    print("--- Dijkstra's algorithm ---")
    dijkstra(graph, vertices['s'])

    print("--- result ---")
    for v in vertices.values():
        print(f"name = {v.name}, distance = {v.distance}", end=' ')

        paths = collect_predecessors(v)
        print('(', end='')
        for i, p in enumerate(paths):
            print(p.name, end=' -> ' if i < len(paths) - 1 else ')\n')
