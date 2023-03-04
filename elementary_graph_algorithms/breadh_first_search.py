import sys

from graph import Color
from graph import Edge
from graph import Graph
from graph import Vertex


def breadth_first_search(graph, s):
    vertices = graph.vertices
    for u in vertices.values():
        if u.name != s.name:
            u.distance = sys.maxsize

    s.color = Color.GRAY
    s.distance = 0

    q = list()
    q.append(s)
    while len(q):
        u = q.pop()
        print(f"{u.name} is discovered.")

        adjacencies = graph.adjacency_list[u.name]
        for v_name in adjacencies:
            v = vertices[v_name]
            if v.color == Color.WHITE:
                print(v.name, " is colored WHITE -> GRAY")
                v.color = Color.GRAY
                v.distance = u.distance + 1
                v.predecessor = u

                q.append(v)

        u.color = Color.BLACK


def print_path(v):
    path = []
    p = v
    while p:
        path.append(p)

        p = p.predecessor

    path.reverse()
    for i, u in enumerate(path):
        print(u.name, end=' -> ' if i != len(path) - 1 else '')


if __name__ == '__main__':
    vertices = {}
    vertices['s'] = Vertex('s')
    vertices['r'] = Vertex('r')
    vertices['v'] = Vertex('v')
    vertices['w'] = Vertex('w')
    vertices['t'] = Vertex('t')
    vertices['x'] = Vertex('x')
    vertices['u'] = Vertex('u')
    vertices['y'] = Vertex('y')

    edges = []
    edges.append(Edge('s', 'r'))
    edges.append(Edge('s', 'w'))
    edges.append(Edge('r', 's'))
    edges.append(Edge('r', 'v'))
    edges.append(Edge('v', 'r'))
    edges.append(Edge('w', 's'))
    edges.append(Edge('w', 't'))
    edges.append(Edge('w', 'x'))
    edges.append(Edge('t', 'w'))
    edges.append(Edge('t', 'x'))
    edges.append(Edge('t', 'u'))
    edges.append(Edge('x', 'w'))
    edges.append(Edge('x', 't'))
    edges.append(Edge('x', 'u'))
    edges.append(Edge('x', 'y'))
    edges.append(Edge('u', 't'))
    edges.append(Edge('u', 'x'))
    edges.append(Edge('u', 'y'))
    edges.append(Edge('y', 'u'))
    edges.append(Edge('y', 'x'))

    graph = Graph(vertices, edges)

    print("--- graph ---")
    graph.print_graph()

    print("--- breadh first search ---")
    breadth_first_search(graph, vertices['s'])

    print("--- result ---")
    for u in vertices.values():
        print(f"{u.name} ({u.distance}): ", end='')

        print_path(u)
        print('')
