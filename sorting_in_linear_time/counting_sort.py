import random


def sort(data):
    table = [0 for _ in range(max(data) + 1)]

    for d in data:
        table[d] += 1

    for i in range(1, len(table)):
        table[i] += table[i - 1]

    print("--- auxiliary table ---")
    print(table)

    temp = [-1 for _ in data]
    for _, d in enumerate(reversed(data)):
        idx_to_replace = table[d] - 1
        temp[idx_to_replace] = d
        table[d] -= 1

    print("--- temporary data ---")
    print(temp)

    data.clear()
    data.extend(temp)


if __name__ == '__main__':
    data = [random.randint(0, 15) for _ in range(30)]

    print("--- before ---")
    print(data)

    print("--- sort ---")
    sort(data)

    print("--- after ---")
    print(data)
