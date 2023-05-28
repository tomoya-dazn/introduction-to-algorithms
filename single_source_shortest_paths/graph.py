import sys

from collections import defaultdict


class Vertex:

    __slots__ = ['name', 'predecessor', 'distance']

    def __init__(self, name):
        self.name = name
        self.predecessor = None
        self.distance = sys.maxsize

    def __lt__(self, other):
        return self.distance < other.distance


class Edge:

    __slots__ = ['start', 'end', 'weight']

    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight


class Graph:

    __slots__ = ['vertices', 'edges', 'adjacency_list']

    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.adjacency_list = defaultdict(list)

        self.__initialize_adjacency_list()

    def print_graph(self):
        for u, adjacency in self.adjacency_list.items():
            print(u, ': ', end='')

            for i, (v, weight) in enumerate(adjacency):
                print(f"{v}({weight})", end=' -> ' if i <
                      len(adjacency) - 1 else '')

            print('')

    def __initialize_adjacency_list(self):
        for edge in self.edges:
            start = edge.start
            end = edge.end
            weight = edge.weight

            self.adjacency_list[start].append((end, weight))


def initialize_single_source(graph, s):
    vertices = graph.vertices
    for v in vertices.values():
        v.distance = sys.maxsize
        v.predecessor = None

    s.distance = 0


def relax(u, v, weight):
    if v.distance > u.distance + weight:
        print(
            f"{u.name, v.name} relax... before = {v.distance}, after = {u.distance + weight}")

        v.distance = u.distance + weight
        v.predecessor = u


def trace_vertices(v, s):
    result = []
    result.append(v)

    p = v.predecessor
    while p:
        result.append(p)
        p = p.predecessor

    return result[::-1]
