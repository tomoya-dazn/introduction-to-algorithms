import sys


def matrix_chain_order(p, idx_of_start, idx_of_end):
    results = [[sys.maxsize for _ in range(
        len(p) + 1)] for _ in range(len(p) + 1)]

    return matrix_chain_order_internal(p, idx_of_start, idx_of_end, results)


def matrix_chain_order_internal(p, idx_of_start, idx_of_end, results):
    if results[idx_of_start][idx_of_end] < sys.maxsize:
        return results[idx_of_start][idx_of_end]

    result = sys.maxsize
    if idx_of_start == idx_of_end:
        result = 0
    else:
        for k in range(idx_of_start, idx_of_end):
            result = min(result, matrix_chain_order_internal(p, idx_of_start, k, results) +
                         matrix_chain_order_internal(p, k + 1, idx_of_end, results) +
                         p[idx_of_start] * p[k + 1] * p[idx_of_end + 1])

    results[idx_of_start][idx_of_end] = result

    return result


if __name__ == '__main__':
    p = [30, 35, 15, 5, 10, 20, 25]

    print("  i |", end='')
    for i in range(len(p) - 1):
        print(f"{i:^7}|", end='')
    print('')
    print("A[i]|", end='')
    for i in range(len(p) - 1):
        print(f"{p[i]:>3}*{p[i + 1]:>3}|", end='')
    print('')

    diff = 0
    while diff < len(p) - 1:
        print(f"--- diff = {diff} ---")

        i, j = 0, diff
        for j in range(diff, len(p) - 1):
            result = matrix_chain_order(p, i, j)
            print(f"i = {i}, j = {j} / result = {result}")

            i += 1

        diff += 1
