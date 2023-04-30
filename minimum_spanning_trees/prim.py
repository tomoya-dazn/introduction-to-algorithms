from graph import Edge
from graph import Graph
from graph import Vertex

import heapq
import sys


def prim(graph, root):
    vertices = graph.vertices
    for u in vertices.values():
        u.predecessor = None
        u.key = sys.maxsize
    root.key = 0

    vertices_list = list(vertices.values())
    heapq.heapify(vertices_list)

    while len(vertices_list):
        u = heapq.heappop(vertices_list)
        print(f"target vertes = {u.name}")

        adjacencies = graph.adjacency_list[u.name]
        for name, weight in adjacencies:
            v = vertices[name]

            if v in vertices_list and weight < v.key:
                print(f"{u.name, name}: key = {v.key} -> {weight}")
                v.predecessor = u
                v.key = weight

                heapq.heapify(vertices_list)
                for u in vertices_list:
                    print(u)


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

    print("--- Prim's algorithm ---")
    prim(graph, vertices['a'])

    print("--- minimum spanning tree ---")
    total = 0
    for u in vertices.values():
        print(
            f"{u.name} predeccesor = {u.predecessor.name if u.predecessor else 'None'} ({u.key})")
        total += u.key
    print(f"total weight = {total}")
