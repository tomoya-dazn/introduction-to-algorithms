from graph import Color
from graph import Edge
from graph import Graph
from graph import Vertex


def breadth_first_search(graph, s):
    vertices = graph.vertices
    edges = graph.edges

    s.color = Color.GRAY
    s.distance = 0
    s.predecessor = None

    q = []
    q.append(s)
    while len(q):
        u = q.pop(0)

        adjacency_list = graph.adjacency_list[u.name]
        for v_name in adjacency_list:
            v = vertices[v_name]
            if v.color == Color.WHITE:
                print(f"{v.name} color: WHITE -> GRAY")
                v.color = Color.GRAY
                v.distance = u.distance + 1
                v.predecessor = u

                q.append(v)

        print(f"{u.name} color GRAY -> BLACK")
        u.color = Color.BLACK


def print_path(graph, s, v, v_name):
    if v == s:
        print(s.name, end=' -> ' if v.name != v_name else '')
    elif not v.predecessor:
        return
    else:
        print_path(graph, s, v.predecessor, v_name)
        print(v.name, end=' -> ' if v.name != v_name else '')


if __name__ == '__main__':
    vertex_names = ['s', 'r', 'w', 'v', 'x', 't', 'y', 'u']
    vertices = {}
    for v_name in vertex_names:
        vertices[v_name] = Vertex(v_name)

    edges = []
    edges.append(Edge('s', 'r'))
    edges.append(Edge('s', 'w'))
    edges.append(Edge('r', 's'))
    edges.append(Edge('r', 'v'))
    edges.append(Edge('w', 's'))
    edges.append(Edge('w', 't'))
    edges.append(Edge('w', 'x'))
    edges.append(Edge('v', 'r'))
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
    edges.append(Edge('y', 'x'))
    edges.append(Edge('y', 'u'))

    graph = Graph(vertices, edges)

    print("--- graph ---")
    graph.print_graph()

    print("--- breadth first search ---")
    breadth_first_search(graph, vertices['s'])

    print("--- result ---")
    for v in vertices.values():
        print(f"{v.name} ({v.distance}) : ", end='')

        print_path(graph, vertices['s'], v, v.name)

        print('')
