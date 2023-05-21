from graph import Edge
from graph import Graph
from graph import Vertex

from graph import trace_vertices
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

    for _ in vertices:
        for edge in edges:
            u = vertices[edge.start]
            v = vertices[edge.end]
            weight = edge.weight

            relax(u, v, weight)


if __name__ == '__main__':
    vertices = {}
    vertices['s'] = Vertex('s')
    vertices['t'] = Vertex('t')
    vertices['y'] = Vertex('y')
    vertices['x'] = Vertex('x')
    vertices['z'] = Vertex('z')

    edges = []
    edges.append(Edge('s', 't', 6))
    edges.append(Edge('s', 'y', 7))
    edges.append(Edge('t', 'y', 8))
    edges.append(Edge('t', 'x', 5))
    edges.append(Edge('t', 'z', -4))
    edges.append(Edge('y', 'x', -3))
    edges.append(Edge('y', 'z', 9))
    edges.append(Edge('x', 't', -2))
    edges.append(Edge('z', 's', 2))
    edges.append(Edge('z', 'x', 7))

    graph = Graph(vertices, edges)

    print("--- graph ---")
    graph.print_graph()

    print("--- bellman-ford algorithm ---")
    bellman_ford(graph, vertices['s'])

    print("--- result ---")
    for v in vertices.values():
        print(f"name = {v.name}, distance = {v.distance}", end=' (')

        path = trace_vertices(v, vertices['s'])
        for i, v in enumerate(path):
            print(v.name, end=' -> ' if i < len(path) - 1 else '')

        print(')')
