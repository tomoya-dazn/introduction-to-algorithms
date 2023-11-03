import sys


class Vertex:

    def __init__(self, name):
        self.name = name
        self.distance = 0
        self.predecessor = None


class Edge:

    def __init__(self, start, finish, weight=1):
        self.start = start
        self.finish = finish
        self.weight = weight


class Graph:

    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.adjacency_list = {}
        self.__initialize_adjacency_list()

    def print_graph(self):
        for v_name, adjacencies in self.adjacency_list.items():
            print(v_name, ':', end=' ')

            for i, adjacency in enumerate(adjacencies):
                finish, weight = adjacency[0], adjacency[1]
                print(f"{finish}({weight})", end=' -> ' if i !=
                      len(adjacencies) - 1 else '\n')

    def __initialize_adjacency_list(self):
        for v in self.vertices.values():
            name = v.name
            self.adjacency_list[name] = []

        for edge in self.edges:
            start = edge.start
            finish = edge.finish
            weight = edge.weight
            self.adjacency_list[start].append((finish, weight))


def initialize_single_source(graph, s):
    vertices = graph.vertices
    for v in vertices.values():
        v.distance = sys.maxsize
        v.predecessor = None

    s.distance = 0


def relax(u, v, weight):
    if v.distance > u.distance + weight:
        print(
            f"Relax: (u, v) = ({u.name}, {v.name}) before = {v.distance}, after = {u.distance + weight})")

        v.distance = u.distance + weight
        v.predecessor = u
