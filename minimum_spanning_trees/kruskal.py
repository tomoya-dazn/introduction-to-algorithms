from disjoint_set import DisjointSet
from graph import Edge
from graph import Graph
from graph import Vertex


def kruskal(graph):
    vertices = graph.vertices
    edges = graph.edges

    disjoint_set = DisjointSet()
    for ch in vertices.keys():
        disjoint_set.initialize(ch)

    edges.sort()
    results = []
    s = set()
    for edge in edges:
        start = edge.start
        finish = edge.finish
        weight = edge.weight

        s = disjoint_set.find_set(start)
        t = disjoint_set.find_set(finish)
        if s != t:
            print(f"start = {start}, finish = {finish}, weight = {weight}")

            disjoint_set.union(start, finish)
            results.append(edge)

    return results


if __name__ == '__main__':
    vertices = {}
    vertices['a'] = Vertex('a')
    vertices['b'] = Vertex('b')
    vertices['c'] = Vertex('c')
    vertices['d'] = Vertex('d')
    vertices['e'] = Vertex('e')
    vertices['f'] = Vertex('f')
    vertices['g'] = Vertex('g')
    vertices['h'] = Vertex('h')
    vertices['i'] = Vertex('i')

    edges = []
    edges.append(Edge('a', 'b', 4))
    edges.append(Edge('a', 'h', 8))
    edges.append(Edge('b', 'a', 4))
    edges.append(Edge('b', 'c', 8))
    edges.append(Edge('b', 'h', 11))
    edges.append(Edge('c', 'b', 8))
    edges.append(Edge('c', 'd', 7))
    edges.append(Edge('c', 'f', 4))
    edges.append(Edge('c', 'i', 2))
    edges.append(Edge('d', 'c', 7))
    edges.append(Edge('d', 'e', 9))
    edges.append(Edge('d', 'f', 14))
    edges.append(Edge('e', 'd', 9))
    edges.append(Edge('e', 'f', 10))
    edges.append(Edge('f', 'c', 4))
    edges.append(Edge('f', 'd', 14))
    edges.append(Edge('f', 'e', 10))
    edges.append(Edge('f', 'g', 2))
    edges.append(Edge('g', 'f', 2))
    edges.append(Edge('g', 'h', 1))
    edges.append(Edge('g', 'i', 6))
    edges.append(Edge('h', 'a', 8))
    edges.append(Edge('h', 'b', 11))
    edges.append(Edge('h', 'g', 1))
    edges.append(Edge('h', 'i', 7))
    edges.append(Edge('i', 'c', 2))
    edges.append(Edge('i', 'g', 6))
    edges.append(Edge('i', 'h', 7))

    graph = Graph(vertices, edges)

    print("--- graph ---")
    graph.print_graph()

    print("--- Kruskal's algorithm ---")
    results = kruskal(graph)

    print("--- result ---")
    total = 0
    for edge in results:
        print(
            f"start = {edge.start}, finish = {edge.finish}, weight = {edge.weight}")
        total += edge.weight
    print(f"total = {total}")
