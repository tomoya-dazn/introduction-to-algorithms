import enum


class Color(enum.Enum):

    WHITE = 'white'
    GRAY = 'gray'
    BLACK = 'black'


class Vertex:

    def __init__(self, name, distance=0):
        self.name = name
        self.predecessor = None


class Edge:

    def __init__(self, start, finish, weight=1):
        self.start = start
        self.finish = finish
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight


class Graph:

    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.adjacency_list = {}
        self.__initialize_adjacency_list()

    def print_graph(self):
        for v_name, adjacencies in self.adjacency_list.items():
            print(v_name, ':', end=' ')

            for i, edge in enumerate(adjacencies):
                print(f"{edge.finish}({edge.weight})", end=' -> ' if i !=
                      len(adjacencies) - 1 else '\n')

    def __initialize_adjacency_list(self):
        for v in self.vertices.values():
            name = v.name
            self.adjacency_list[name] = []

        for edge in self.edges:
            self.adjacency_list[edge.start].append(edge)
