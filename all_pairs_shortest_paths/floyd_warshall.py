import sys


def floyd_warshall(W):
    n = len(W)

    D = W.copy()
    PI = [[None for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j and W[i][j] == sys.maxsize:
                PI[i][j] = None
            elif i != j and W[i][j] < sys.maxsize:
                PI[i][j] = i

    for k in range(n):
        print(f"--- k = {k} ---")
        print("--- D ---")
        print_matrix(D)
        print("--- PI ---")
        print_matrix(PI)

        old_D = D.copy()
        old_PI = PI.copy()
        for i in range(n):
            result = sys.maxsize
            for j in range(n):
                if old_D[i][j] > old_D[i][k] + old_D[k][j]:
                    D[i][j] = old_D[i][k] + old_D[k][j]
                    PI[i][j] = old_PI[k][j]
                else:
                    D[i][j] = old_D[i][j]
                    PI[i][j] = old_PI[i][j]

    return D, PI


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

    print("--- Floyd-Warshall algorithm ---")
    D, PI = floyd_warshall(W)

    print("--- result ---")
    print("--- D ---")
    print_matrix(D)
    print("--- PI ---")
    print_matrix(PI)
