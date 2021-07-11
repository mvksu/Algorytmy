class Node:
    def __init__(self, value=None, repeats=1):
        self.value = value
        self.left = None
        self.right = None
        self.repeats = repeats


class bst:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left is None:
                cur_node.left = Node(value)
            else:
                self._insert(value, cur_node.left)
        elif value > cur_node.value:
            if cur_node.right is None:
                cur_node.right = Node(value)
            else:
                self._insert(value, cur_node.right)
        else:
            cur_node.repeats = cur_node.repeats + 1

    def print_tree(self, maxdepth):
        if self.root is not None:
            self._print_tree(self.root, 0, maxdepth)

    def _print_tree(self, cur_node, space, maxdepth):
        if cur_node is not None and space < maxdepth:
            self._print_tree(cur_node.right, space + 1, maxdepth)
            print("    " * space, end="")
            print("(" + str(cur_node.value) + " " + str(cur_node.repeats) + ")")
            self._print_tree(cur_node.left, space + 1, maxdepth)

    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        if cur_node is None:
            return cur_height
        left_height = self._height(cur_node.left, cur_height + 1)
        right_height = self._height(cur_node.right, cur_height + 1)
        return max(left_height, right_height)

tree = bst()
tree.insert(50)
tree.insert(30)
tree.insert(20)
tree.insert(40)
tree.insert(70)
tree.insert(80)
tree.insert(80)

tree.print_tree(5)

print("wyskoosc drzewa: " + str(tree.height()))
print("")

with open('manpython.txt') as f:
    flat_list = [word for line in f for word in line.split()]

nexttree = bst()

for x in range(1500):
    nexttree.insert(flat_list[x])
nexttree.print_tree(5)
print("wyskoosc drzewa: " + str(nexttree.height()))
