import sys


def extend_shortest_paths(L, W):
    row = len(W)
    new_L = [[0 for _ in range(row)] for _ in range(row)]

    for i in range(row):
        for j in range(row):
            new_L[i][j] = sys.maxsize
            for k in range(row):
                new_L[i][j] = min(new_L[i][j], L[i][k] + W[k][j])

    return new_L


def slow_all_pairs_shortest_paths(W):
    row = len(W)
    old_L = [[0 for _ in range(row)] for _ in range(row)]

    for i in range(row):
        for j in range(row):
            old_L[i][j] = W[i][j]

    for m in range(row - 1):
        L = [[0 for _ in range(row)] for _ in range(row)]
        L = extend_shortest_paths(old_L, W)

        print(f"--- m = {m} ---")
        print_matrix(L)

        old_L = L

    return L


def print_matrix(matrix):
    for row in matrix:
        print("[", end='')

        for i, column in enumerate(row):
            if column == sys.maxsize:
                print("∞", end='')
            else:
                print(column, end='')

            if i != len(row) - 1:
                print(", ", end='')

        print("]")


if __name__ == '__main__':
    W = [
        [0, 3, 8, sys.maxsize, -4],
        [sys.maxsize, 0, sys.maxsize, 1, 7],
        [sys.maxsize, 4, 0, sys.maxsize, sys.maxsize],
        [2, sys.maxsize, -5, 0, sys.maxsize],
        [sys.maxsize, sys.maxsize, sys.maxsize, 6, 0]
    ]

    print("--- adjacency matrix ---")
    print_matrix(W)

    print("--- calculate all pairs shortest paths ---")
    L = slow_all_pairs_shortest_paths(W)
