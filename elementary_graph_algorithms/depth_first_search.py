from graph import Color
from graph import Edge
from graph import Graph
from graph import Vertex


time = 0


def depth_first_search(graph):
    vertices = graph.vertices

    for u in vertices.values():
        if u.color == Color.WHITE:
            print(f"{u.name} is discovered.")

            depth_first_search_internal(graph, u)


def depth_first_search_internal(graph, u):
    global time

    time += 1
    u.start_time = time
    print(f"{u.name} start! time = {time}")
    u.color = Color.GRAY

    adjacencies = graph.adjacency_list[u.name]
    for adjacency in adjacencies:
        v = graph.vertices[adjacency]
        if v.color == Color.WHITE:
            v.predecessor = u
            depth_first_search_internal(graph, v)

    time += 1
    u.finish_time = time
    print(f"{u.name} finish! time = {time}")
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
    vertices['u'] = Vertex('u')
    vertices['v'] = Vertex('v')
    vertices['x'] = Vertex('x')
    vertices['y'] = Vertex('y')
    vertices['w'] = Vertex('w')
    vertices['z'] = Vertex('z')

    edges = []
    edges.append(Edge('u', 'v'))
    edges.append(Edge('u', 'x'))
    edges.append(Edge('v', 'y'))
    edges.append(Edge('x', 'v'))
    edges.append(Edge('y', 'x'))
    edges.append(Edge('w', 'y'))
    edges.append(Edge('w', 'z'))
    edges.append(Edge('z', 'z'))

    graph = Graph(vertices, edges)

    print("--- graph ---")
    graph.print_graph()

    print("--- depth first search ---")
    depth_first_search(graph)

    print("--- result ---")
    for u in vertices.values():
        print(f"{u.name} ({u.start_time} / {u.finish_time}) : ", end='')

        print_path(u)
        print('')
