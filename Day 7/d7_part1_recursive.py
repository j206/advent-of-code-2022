import re
with open("./Day 7/d7_input.txt") as f:
    inputs = f.readlines()


def part1():
    root = Tree("/")
    total_size = 0

    for i, input in enumerate(inputs):
        input = input.strip()

        if input[:7] == "$ cd ..":
            handle_move_out()
        elif input[:4] == "$ cd":
            name = input.split("$ cd ")[1]
            handle_move_in(name, root, i)
        elif input[:4] == "$ ls":
            handle_list()

    return print(total_size)


def handle_move_in(name, root, i):
    size = get_size(i)
    root.add_child(name, size)
    return


def handle_move_out():
    return


def handle_list():
    return

def get_size(i):
    i += 1
    size = 0

    while i < len(inputs) and inputs[i][:4] != "$ cd":
        if inputs[i][0].isnumeric():
            size += int(re.findall('\d+', inputs[i])[0])
        i += 1
    return size


class Tree(object):
    def __init__(self, name='root', size=0, children=None):
        self.name = name
        self.size = size
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)

    def __repr__(self):
        return self.name

    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)


part1()
