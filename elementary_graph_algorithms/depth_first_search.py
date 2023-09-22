from graph import Color
from graph import Edge
from graph import Graph
from graph import Vertex


time = 0


def depth_first_search(graph):
    vertices = graph.vertices

    for u in vertices.values():
        if u.color == Color.WHITE:
            depth_first_search_internal(graph, u)


def depth_first_search_internal(graph, u):
    global time

    time += 1
    u.start_time = time
    u.color = Color.GRAY
    print(f"{u.name} color WHITE -> GRAY time = {time}")

    vertices = graph.vertices
    adjacency_list = graph.adjacency_list[u.name]
    for v_name in adjacency_list:
        v = vertices[v_name]
        if v.color == Color.WHITE:
            v.predecessor = u
            depth_first_search_internal(graph, v)

    time += 1
    u.finish_time = time
    u.color = Color.BLACK
    print(f"{u.name} color GRAY -> BLACK time = {time}")


def calculate_path(u):
    result = []
    result.append(u.name)

    while u.predecessor:
        u = u.predecessor
        result.append(u.name)

    result.sort()

    return result


if __name__ == '__main__':
    vertex_names = ['u', 'v', 'x', 'y', 'w', 'z']
    vertices = {}
    for v_name in vertex_names:
        vertices[v_name] = Vertex(v_name)

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
    for v in vertices.values():
        print(f"{v.name} ({v.start_time} / {v.finish_time}) : ", end='')

        path = calculate_path(v)
        for i, u in enumerate(path):
            print(u, end=' -> ' if i < len(path) - 1 else '')

        print('')
