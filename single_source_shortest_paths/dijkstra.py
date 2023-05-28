from graph import Edge
from graph import Graph
from graph import Vertex
from graph import trace_vertices
from graph import initialize_single_source
from graph import relax
import heapq


def dijkstra(graph, s):
    initialize_single_source(graph, s)

    vertices = graph.vertices
    vertices_list = list(vertices.values())
    results = []
    heapq.heapify(vertices_list)

    while len(vertices_list):
        u = heapq.heappop(vertices_list)
        results.append(u)
        adjacencies = graph.adjacency_list[u.name]
        for name, weight in adjacencies:
            v = vertices[name]
            relax(u, v, weight)

            heapq.heapify(vertices_list)


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
        print(f"name = {v.name}, distance = {v.distance}", end=' (')

        path = trace_vertices(v, vertices['s'])
        for i, v in enumerate(path):
            print(v.name, end=' -> ' if i < len(path) - 1 else '')

        print(')')
