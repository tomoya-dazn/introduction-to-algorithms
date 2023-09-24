from graph import Edge
from graph import Graph
from graph import Vertex

import heapq
import sys


def prim(graph):
    vertices = graph.vertices
    edges = graph.edges

    for u in vertices.values():
        u.key = sys.maxsize
        u.predecessor = None

    vertices['a'].key = 0

    vertices_list = list(vertices.values())
    heapq.heapify(vertices_list)

    while vertices_list:
        u = heapq.heappop(vertices_list)

        adjacencies = graph.adjacency_list[u.name]
        for edge in adjacencies:
            v = vertices[edge.finish]
            weight = edge.weight
            if v in vertices_list and weight < v.key:
                print(f"v = {v.name} before = {v.key} after = {weight}")

                v.key = weight
                v.predecessor = u

                heapq.heapify(vertices_list)


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

    print("--- Prim's algorithm ---")
    prim(graph)

    print("--- result ---")
    total = 0
    for v in vertices.values():
        print(
            f"name = {v.name} key = {v.key} predecessor = {v.predecessor.name if v.predecessor else 'None'}")
        total += v.key
    print(f"total = {total}")
