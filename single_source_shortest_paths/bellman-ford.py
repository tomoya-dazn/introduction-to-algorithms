from graph import Edge
from graph import Graph
from graph import Vertex
from graph import initialize_single_source
from graph import relax


def bellman_ford(graph, s):
    verticies = graph.vertices
    edges = graph.edges

    initialize_single_source(graph, s)

    for i in range(len(vertices) - 1):
        for edge in edges:
            u = vertices[edge.start]
            v = vertices[edge.finish]
            weight = edge.weight

            relax(u, v, weight)

    for edge in edges:
        u = vertices[edge.start]
        v = vertices[edge.finish]
        weight = edge.weight

        if v.distance > u.distance + weight:
            return False

    return True


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

    print("--- bellman ford algorithm ---")
    result = bellman_ford(graph, vertices['s'])

    print("--- result ---")
    if result:
        for v in vertices.values():
            print(f"name = {v.name}, distance = {v.distance}", end=' ')

            paths = collect_predecessors(v)
            print('(', end='')
            for i, p in enumerate(paths):
                print(p.name, end=' -> ' if i < len(paths) - 1 else ')\n')
    else:
        print("Graph has a cycle.")
