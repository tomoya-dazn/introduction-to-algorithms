import enum

from collections import defaultdict


class Color(enum.Enum):

    WHITE = "white"
    GRAY = "gray"
    BLACK = "black"


class Vertex:

    __slots__ = ['name', 'color', 'distance', 'predecessor']

    def __init__(self, name, distance=1, color=Color.WHITE):
        self.name = name
        self.distance = distance
        self.color = color
        self.predecessor = None


class Edge:

    __slots__ = ['start', 'finish', 'distance']

    def __init__(self, start, finish, distance=1):
        self.start = start
        self.finish = finish
        self.distance = distance


class Graph:

    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.adjacency_list = defaultdict(list)

        self.__initialize_adjacency_list(edges)

    def print_graph(self):
        for vertex in self.vertices.values():
            print(vertex.name, ':', end='')

            adjacencies = self.adjacency_list[vertex.name]
            for i, v_name in enumerate(adjacencies):
                print(v_name, end=' -> ' if i !=
                      len(adjacencies) - 1 else '\n')

    def __initialize_adjacency_list(self, edges):
        for edge in edges:
            u_name = edge.start
            v_name = edge.finish

            self.adjacency_list[u_name].append(v_name)
