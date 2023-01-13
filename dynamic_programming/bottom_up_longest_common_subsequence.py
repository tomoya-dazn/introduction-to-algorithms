import enum
import sys


class Direction(enum.Enum):

    UP = "up"
    LEFT = "left"
    DIAGONAL = "diagonal"


def lcs_length(x, y):
    results = [[sys.maxsize for _ in range(
        max(len(x), len(y)) + 1)] for _ in range(max(len(x), len(y)) + 1)]
    directions = [[None for _ in range(max(len(x), len(y)) + 1)]
                  for _ in range(max(len(x), len(y)) + 1)]

    for i, _x in enumerate(x):
        result = sys.maxsize
        for j, _y in enumerate(y):
            if i == 0 and j == 0:
                if _x == _y:
                    directions[i][j] = Direction.DIAGONAL
                    result = 1
                else:
                    directions[i][j] = Direction.UP
                    result = 0
            elif i == 0:
                if _x == _y:
                    directions[i][j] = Direction.DIAGONAL
                    result = 1
                else:
                    directions[i][j] = Direction.LEFT
                    result = results[i][j - 1]
            elif j == 0:
                if _x == _y:
                    directions[i][j] = Direction.DIAGONAL
                    result = 1
                else:
                    directions[i][j] = Direction.UP
                    result = results[i - 1][j]
            else:
                if _x == _y:
                    directions[i][j] = Direction.DIAGONAL
                    result = results[i - 1][j - 1] + 1
                else:
                    if results[i - 1][j] >= results[i][j - 1]:
                        directions[i][j] = Direction.UP
                        result = results[i - 1][j]
                    else:
                        directions[i][j] = Direction.LEFT
                        result = results[i][j - 1]

            results[i][j] = result

    return results, directions


def print_optimal_strategy(directions, x, i, j):
    if i < 0 or j < 0:
        return

    if directions[i][j] == Direction.DIAGONAL:
        print_optimal_strategy(directions, x, i - 1, j - 1)
        print(x[i], end='')
    elif directions[i][j] == Direction.UP:
        print_optimal_strategy(directions, x, i - 1, j)
    else:
        print_optimal_strategy(directions, x, i, j - 1)


if __name__ == '__main__':
    x = "ABCBDAB"
    y = "BDCABA"

    results, directions = lcs_length(x, y)
    for i in range(len(x)):
        print(f"--- i = {i} ---")
        for j in range(len(y)):
            print(
                f"i = {i}, j = {j} / x = {x[:i + 1]}, y = {y[:j + 1]} / result = {results[i][j]}", end=' (')
            print_optimal_strategy(directions, x, i, j)
            print(')')
