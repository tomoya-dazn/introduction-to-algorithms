import enum


class Color(enum.Enum):

    WHITE = 'white'
    GRAY = 'gray'
    BLACK = 'black'


class Vertex:

    def __init__(self, name, color=Color.WHITE):
        self.name = name
        self.color = color
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
                print(adjacency, end=' -> ' if i !=
                      len(adjacencies) - 1 else '\n')

    def __initialize_adjacency_list(self):
        for v in self.vertices.values():
            name = v.name
            self.adjacency_list[name] = []

        for edge in self.edges:
            start = edge.start
            finish = edge.finish
            self.adjacency_list[start].append(finish)
