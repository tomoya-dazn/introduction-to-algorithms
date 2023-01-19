import heapq


class Element:

    __slots__ = ['ch', 'freq', 'left', 'right']

    def __init__(self, ch="", freq=0):
        self.ch = ch
        self.freq = freq
        self.left = self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

    def __str__(self):
        if not self.ch:
            return f"{self.freq}"
        else:
            return f"{self.ch}:{self.freq}"


def huffman(characters):
    heapq.heapify(characters)

    while len(characters) != 1:
        x = heapq.heappop(characters)
        y = heapq.heappop(characters)
        z = Element()

        z.left = x
        z.right = y
        z.freq = x.freq + y.freq
        heapq.heappush(characters, z)

    return heapq.heappop(characters)


def print_tree(root):

    def print_internal(r, space_size=0):
        if r.left:
            print_internal(r.left, space_size=space_size+1)

        print(f"{'    ' * space_size}{r}")

        if r.right:
            print_internal(r.right, space_size=space_size+1)

    print_internal(root)


if __name__ == '__main__':
    characters = [
        Element('a', 45),
        Element('b', 13),
        Element('c', 12),
        Element('d', 16),
        Element('e', 9),
        Element('f', 5)
    ]

    print(' ch |', end='')
    for elem in characters:
        print(f"{elem.ch:^3}|", end='')
    print('')
    print('freq|', end='')
    for elem in characters:
        print(f"{elem.freq:^3}|", end='')
    print('')

    root = huffman(characters)
    print_tree(root)
