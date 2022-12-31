import sys


def find_maximum_subarray(data, idx_of_start, idx_of_end):
    if idx_of_start == idx_of_end:
        return idx_of_start, idx_of_end, data[idx_of_start]
    else:
        idx_of_mid = (idx_of_start + idx_of_end) // 2

        start_of_first, end_of_first, sum_of_first = find_maximum_subarray(
            data, idx_of_start, idx_of_mid)
        start_of_second, end_of_second, sum_of_second = find_maximum_subarray(
            data, idx_of_mid + 1, idx_of_end)
        start_of_crossing, end_of_crossing, sum_of_crossing = find_max_crossing_subarray(
            data, idx_of_start, idx_of_mid, idx_of_end)

        if sum_of_first > sum_of_second and sum_of_first > sum_of_crossing:
            return start_of_first, end_of_first, sum_of_first
        elif sum_of_second > sum_of_first and sum_of_second > sum_of_crossing:
            return start_of_second, end_of_second, sum_of_second
        else:
            return start_of_crossing, end_of_crossing, sum_of_crossing


def find_max_crossing_subarray(data, idx_of_start, idx_of_mid, idx_of_end):
    summary = 0
    sum_of_first = -sys.maxsize
    for i in reversed(range(idx_of_mid + 1)):
        summary += data[i]
        if sum_of_first < summary:
            sum_of_first = summary
            start_idx = i

    summary = 0
    sum_of_second = -sys.maxsize
    for i in range(idx_of_mid + 1, idx_of_end + 1):
        summary += data[i]
        if sum_of_second < summary:
            sum_of_second = summary
            end_idx = i

    return start_idx, end_idx, sum_of_first + sum_of_second


if __name__ == '__main__':
    data = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, -7]

    print("  i |", end='')
    for i in range(len(data)):
        print(f"{i:>3}|", end='')
    print('')
    print("a[i]|", end='')
    for d in data:
        print(f"{d:>3}|", end='')
    print('')

    idx_of_start, idx_of_end, summary = find_maximum_subarray(
        data, 0, len(data) - 1)
    print(f"result = {summary} [", end='')
    for i in range(idx_of_start, idx_of_end + 1):
        print(f"{data[i]}", end=', ' if i != idx_of_end else ']')
    print('')
