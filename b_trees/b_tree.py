class Element:

    def __init__(self, is_leaf=True):
        self.n = 0
        self.keys = []
        self.is_leaf = is_leaf
        self.children = []


class Tree:

    def __init__(self, min_degree=2):
        self.root = Element()
        self.min_degree = min_degree

    def insert_key(self, key):
        r = self.root

        if r.n == 2 * self.min_degree - 1:
            s = Element()
            s.is_leaf = False
            s.children.append(r)

            self.root = s
            self.__split_child(s, 0)

            self.__insert_key_non_full(s, key)
        else:
            self.__insert_key_non_full(r, key)

    def contains(self, key):

        def contains_internal(x, key):
            i = 0
            while i <= x.n - 1 and x.keys[i] < key:
                i += 1

            if i <= x.n - 1 and x.keys[i] == key:
                return x
            elif x.is_leaf:
                return None
            else:
                return contains_internal(x.children[i], key)

        return contains_internal(self.root, key)

    def remove(self, key):

        def remove_internal(x, key):
            i = 0
            while i <= x.n - 1 and x.keys[i] < key:
                i += 1

            if i <= x.n - 1 and x.keys[i] == key:
                # case 1
                if x.is_leaf:
                    x.keys.remove(key)
                    x.n -= 1
                else:
                    if x.children[i].n >= self.min_degree:
                        # case 2 - a
                        y = x.children[i]
                        key_to_up = y.keys[-1]

                        y.keys = y.keys[:-1]
                        y.keys.append(x.keys[i])
                        x.keys[i] = key_to_up

                        remove_internal(y, key)
                    elif x.children[i + 1].n >= self.min_degree:
                        # case 2 - b
                        y = x.children[i + 1]
                        key_to_up = y.keys[0]

                        y.keys = y.keys[1:]
                        y.keys.insert(0, x.keys[i])
                        x.keys[i] = key_to_up

                        remove_internal(y, key)
                    else:
                        # case 2 - c
                        y = x.children[i]
                        z = x.children[i + 1]

                        y.keys.append(x.keys[i])
                        y.n += 1
                        y.keys.extend(z.keys)
                        y.n += z.n

                        if not y.is_leaf:
                            y.children.extend(z.children)

                        x.keys.pop(i)
                        x.n -= 1
                        x.children.pop(i + 1)

                        if x.n == 0:
                            self.root = y

                        remove_internal(y, key)
            else:
                if x.children[i].n == self.min_degree - 1:
                    if i > 0 and x.children[i - 1].n >= self.min_degree:
                        # case 3 - a - (1)
                        y = x.children[i - 1]
                        z = x.children[i]
                        key_to_up = y.keys[-1]
                        key_to_down = x.keys[i - 1]

                        x.keys[i - 1] = key_to_up
                        y.keys = y.keys[:-1]
                        y.n -= 1
                        z.keys.insert(0, key_to_down)
                        z.n += 1

                        if not z.is_leaf:
                            children_to_move = y.children[-1]
                            y.children = y.children[:-1]
                            z.children.insert(0, children_to_move)

                        remove_internal(z, key)
                    elif i < x.n and x.children[i + 1].n >= self.min_degree:
                        # case 3 - a - (2)
                        y = x.children[i]
                        z = x.children[i + 1]
                        key_to_up = z.keys[0]
                        key_to_down = x.keys[i]

                        x.keys[i] = key_to_up
                        y.keys.append(key_to_down)
                        y.n += 1
                        z.keys = z.keys[1:]
                        z.n -= 1

                        if not z.is_leaf:
                            children_to_move = z.children[0]
                            y.children.append(children_to_move)
                            z.children = z.children[1:]

                        remove_internal(y, key)
                    elif i > 0 and x.children[i - 1].n == self.min_degree - 1:
                        # case 3 - b - (1)
                        y = x.children[i]
                        z = x.children[i - 1]
                        key_to_down = x.keys[i - 1]

                        z.keys.append(key_to_down)
                        z.n += 1
                        z.keys.extend(y.keys)
                        z.n += y.n

                        if not z.is_leaf:
                            z.children.extend(y.keys)

                        x.keys.pop(i - 1)
                        x.n -= 1
                        x.children.pop(i)

                        if x.n == 0:
                            self.root = z

                        remove_internal(z, key)
                    elif i < x.n and x.children[i + 1].n == self.min_degree - 1:
                        # case 3 - b - (2)
                        y = x.children[i]
                        z = x.children[i + 1]
                        key_to_down = x.keys[i]

                        y.keys.append(key_to_down)
                        y.n += 1
                        y.keys.extend(z.keys)
                        y.n += z.n

                        if not y.is_leaf:
                            y.children.extend(z.children)

                        x.keys.pop(i)
                        x.n -= 1
                        x.children.pop(i + 1)

                        if x.n == 0:
                            self.root = y

                        remove_internal(y, key)
                else:
                    remove_internal(x.children[i], key)

        remove_internal(self.root, key)

    def __insert_key_non_full(self, x, key):
        i = x.n - 1

        if x.is_leaf:
            while i >= 0 and x.keys[i] > key:
                i -= 1

            i += 1
            x.keys.insert(i, key)
            x.n += 1
        else:
            while i >= 0 and x.keys[i] > key:
                i -= 1

            i += 1
            if x.children[i].n == 2 * self.min_degree - 1:
                self.__split_child(x, i)

                if key > x.keys[i]:
                    i += 1

            self.__insert_key_non_full(x.children[i], key)

    def __split_child(self, x, i):
        y = x.children[i]
        z = Element()
        z.keys = y.keys[self.min_degree:]
        z.n = self.min_degree - 1
        z.is_leaf = y.is_leaf
        key_to_up = y.keys[self.min_degree - 1]
        y.keys = y.keys[:self.min_degree - 1]
        y.n = self.min_degree - 1

        if not y.is_leaf:
            z.children = y.children[self.min_degree:]
            y.children = y.children[:self.min_degree]

        x.keys.insert(i, key_to_up)
        x.n += 1
        x.children.insert(i + 1, z)

    def print_tree(self):

        def print_tree_internal(r, space_size=0):
            print('  ' * space_size, r.keys)

            if not r.is_leaf:
                for c in r.children:
                    print_tree_internal(c, space_size=space_size+1)

        if self.root.keys:
            print_tree_internal(self.root)


if __name__ == '__main__':
    t = Tree()

    # Reference: https://www.cs.utexas.edu/users/djimenez/utsa/cs3343/lecture17.html
    t.insert_key(5)
    t.insert_key(9)
    t.insert_key(3)
    t.insert_key(7)
    t.insert_key(1)
    t.insert_key(2)
    t.insert_key(8)
    t.insert_key(6)
    t.insert_key(0)
    t.insert_key(4)

    while True:
        print("1:insert 2:remove 3:print > ", end='')
        op = int(input())

        if op == 1:
            print("input key > ", end='')
            key = int(input())

            t.insert_key(key)
        elif op == 2:
            print("input key > ", end='')
            key = int(input())

            x = t.contains(key)
            if not x:
                print(f"{key} is not found in the tree.")
            else:
                t.remove(key)
        elif op == 3:
            t.print_tree()
        else:
            print("invalid operation")
