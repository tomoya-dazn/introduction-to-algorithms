import sys


def lcs_length(x, y, i, j):
    results = [[sys.maxsize for _ in range(
        max(i, j) + 1)] for _ in range(max(i, j) + 1)]

    return lcs_length_internal(x, y, i, j, results)


def lcs_length_internal(x, y, i, j, results):
    if results[i][j] < sys.maxsize:
        return results[i][j]

    result = sys.maxsize
    if i == 0 and j == 0:
        if x[i] == y[j]:
            result = 1
        else:
            result = 0
    elif i == 0:
        if x[i] == y[j]:
            result = 1
        else:
            result = lcs_length_internal(x, y, i, j - 1, results)
    elif j == 0:
        if x[i] == y[j]:
            result = 1
        else:
            result = lcs_length_internal(x, y, i - 1, j, results)
    else:
        if x[i] == y[j]:
            result = lcs_length_internal(x, y, i - 1, j - 1, results) + 1
        else:
            result = max(lcs_length_internal(x, y, i, j - 1, results),
                         lcs_length_internal(x, y, i - 1, j, results))

    results[i][j] = result

    return result


if __name__ == '__main__':
    x = "ABCBDAB"
    y = "BDCABA"

    for i in range(len(x)):
        print(f"--- i = {i} ---")
        for j in range(len(y)):
            result = lcs_length(x, y, i, j)

            print(
                f"i = {i}, j = {j} / x = {x[:i + 1]}, y = {y[:j + 1]} / result = {result}")
