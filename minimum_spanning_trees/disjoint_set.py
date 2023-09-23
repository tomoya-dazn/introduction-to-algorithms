from collections import defaultdict


class DisjointSet:

    def __init__(self):
        self.sets = defaultdict(set)

    def initialize(self, ch):
        self.sets[ch].add(ch)

    def find_set(self, ch):
        for k, v in self.sets.items():
            if ch in v:
                return k

        return None

    def union(self, x, y):
        root_of_x = self.find_set(x)
        root_of_y = self.find_set(y)

        if root_of_x < root_of_y:
            self.sets[root_of_x] = self.sets[root_of_x].union(
                self.sets[root_of_y])
            self.sets[root_of_y].clear()
        else:
            self.sets[root_of_y] = self.sets[root_of_y].union(
                self.sets[root_of_x])
            self.sets[root_of_x].clear()

    def print_disjoint_set(self):
        for k, v in self.sets.items():
            print(k, ':', v)
