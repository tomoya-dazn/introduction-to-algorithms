def lcs_length(x, y, i, j):
    if i == 0 and j == 0:
        if x[i] == y[j]:
            return 1
        else:
            return 0
    elif i == 0:
        if x[i] == y[j]:
            return 1
        else:
            return lcs_length(x, y, i, j - 1)
    elif j == 0:
        if x[i] == y[j]:
            return 1
        else:
            return lcs_length(x, y, i - 1, j)
    else:
        if x[i] == y[j]:
            return lcs_length(x, y, i - 1, j - 1) + 1
        else:
            return max(lcs_length(x, y, i - 1, j), lcs_length(x, y, i, j - 1))


if __name__ == '__main__':
    x = "ABCBDAB"
    y = "BDCABA"

    for i in range(len(x)):
        print(f"--- i = {i} ---")
        for j in range(len(y)):
            result = lcs_length(x, y, i, j)

            print(
                f"i = {i}, j = {j} / x = {x[:i + 1]}, y = {y[:j + 1]} / result = {result}")
