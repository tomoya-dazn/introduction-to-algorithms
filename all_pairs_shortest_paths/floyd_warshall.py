import sys


def floyd_warshall(W):
    n = len(W)
    PI = [[None for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j or W[i][j] == sys.maxsize:
                PI[i][j] = None
            elif i != j and W[i][j] < sys.maxsize:
                PI[i][j] = i

    print("--- k = 0 ---")
    D = W.copy()
    print("--- D ---")
    print_matrix(D)
    print("--- PI ---")
    print_matrix(PI)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][j] <= D[i][k] + D[k][j]:
                    d = D[i][j]
                    pi = PI[i][j]
                else:
                    d = D[i][k] + D[k][j]
                    pi = PI[k][j]

                D[i][j] = d
                PI[i][j] = pi

        print(f"--- k = {k} ---")
        print("--- D ---")
        print_matrix(D)
        print("--- PI ---")
        print_matrix(PI)

    return D


def print_matrix(D):
    for i in range(len(D)):
        for j in range(len(D[i])):
            print(D[i][j] if D[i][j] != sys.maxsize else '∞',
                  end=',' if j < len(D[i]) - 1 else '')
        print('')


if __name__ == '__main__':
    D = [
        [0, 3, 8, sys.maxsize, -4],
        [sys.maxsize, 0, sys.maxsize, 1, 7],
        [sys.maxsize, 4, 0, sys.maxsize, sys.maxsize],
        [2, sys.maxsize, -5, 0, sys.maxsize],
        [sys.maxsize, sys.maxsize, sys.maxsize, 6, 0]
    ]

    print("--- D0 ---")
    print_matrix(D)

    print("--- floyd warshall algorithm ---")
    floyd_warshall(D)
