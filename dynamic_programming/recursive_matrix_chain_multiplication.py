import sys


def matrix_chain_order(p, idx_of_start, idx_of_end):
    if idx_of_start == idx_of_end:
        return 0

    result = sys.maxsize
    for k in range(idx_of_start, idx_of_end):
        result = min(result, matrix_chain_order(p, idx_of_start, k) + matrix_chain_order(
            p, k + 1, idx_of_end) + p[idx_of_start] * p[k + 1] * p[idx_of_end + 1])

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
