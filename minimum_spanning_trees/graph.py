from collections import defaultdict


class Vertex:

    __slots__ = ['name', 'predecessor']

    def __init__(self, name):
        self.name = name
        self.predecessor = None


class Edge:

    __slots__ = ['start', 'finish', 'weight']

    def __init__(self, start, finish, weight=1):
        self.start = start
        self.finish = finish
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight


class Graph:

    __slots__ = ['vertices', 'edges', 'adjacency_list']

    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.adjacency_list = defaultdict(list)

        self.__init_adjacency_list()

    def __init_adjacency_list(self):
        for edge in self.edges:
            start = edge.start
            finish = edge.finish
            weight = edge.weight

            self.adjacency_list[start].append((finish, weight))

    def print_graph(self):
        for vertex in self.vertices.values():
            print(vertex.name, ': ', end='')

            adjacencies = self.adjacency_list[vertex.name]
            for i, (v, weight) in enumerate(adjacencies):
                print(f"{v}({weight})", end=' -> ' if i !=
                      len(adjacencies) - 1 else '\n')
