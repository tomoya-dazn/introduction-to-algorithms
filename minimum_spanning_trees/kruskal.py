from collections import defaultdict
from graph import Edge
from graph import Graph
from graph import Vertex


def find_set(disjoint_sets, u):
    for k, disjoint_set in disjoint_sets.items():
        if u in disjoint_set:
            return k


def union_set(disjoint_sets, u, v):
    disjoint_sets[u] = disjoint_sets[u].union(disjoint_sets[v])
    disjoint_sets[v].clear()


def kruskal(graph):
    vertices = graph.vertices
    edges = graph.edges

    disjoint_sets = defaultdict(set)
    for vertex in vertices.values():
        disjoint_sets[vertex.name].add(vertex.name)

    print("--- initialize disjoint set ---")
    for k, v in disjoint_sets.items():
        print(k, ': ', v)

    edges.sort()

    print("--- look for the `safe edge`---")
    results = []
    for edge in edges:
        start = edge.start
        finish = edge.finish
        weight = edge.weight
        print(
            f"target edge: start = {start}, finish = {finish}, weight = {weight}")

        representative_of_start = find_set(disjoint_sets, start)
        representative_of_finish = find_set(disjoint_sets, finish)
        if representative_of_start != representative_of_finish:
            print("This edge is safe.")

            results.append((start, finish, weight))
            union_set(disjoint_sets, representative_of_start,
                      representative_of_finish)

    return results


if __name__ == '__main__':
    vertices = {}
    for name in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']:
        vertices[name] = Vertex(name)

    edges = []
    edges.append(Edge('a', 'b', 4))
    edges.append(Edge('a', 'h', 8))
    edges.append(Edge('b', 'a', 4))
    edges.append(Edge('b', 'c', 8))
    edges.append(Edge('b', 'h', 8))
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

    print("--- Graph ---")
    graph.print_graph()

    print("--- Kruskal's algorithm ---")
    results = kruskal(graph)

    print("--- minimal spanning tree ---")
    total = 0
    for (u, v, weight) in results:
        print(f"({u}, {v}) / weight = {weight}")
        total += weight
    print(f"total weight = {total}")
