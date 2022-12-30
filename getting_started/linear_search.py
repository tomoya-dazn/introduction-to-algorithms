import random


def search(key, data):
    for i, d in enumerate(data):
        if d == key:
            return i

    return -1


if __name__ == '__main__':
    data = [random.randint(1, 20) for _ in range(20)]

    print(data)

    print("input key > ", end='')
    key = int(input())

    result = search(key, data)
    if result == -1:
        print(f"{key} is not found.")
    else:
        print(f"result = {result}")
