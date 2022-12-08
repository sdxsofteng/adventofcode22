class Node:
    def __init__(self, name, dirs, files, last_node) -> None:
        self._name = name
        self._dirs = dirs
        self._files = files
        self._last_node = last_node
    def get_size(self):
        return sum(self._files) if self._files != None else 0

import aocd

data = aocd.get_data(day=7, year=2022).splitlines()

data.pop(0)
current_node = Node(name="/", dirs=dict(), files=list(), last_node=None)
original_node = current_node

#Data mapping
for datum in data:
    datum = datum.split(" ")
    if len(datum) == 2:
        if datum[0] != "$":
            if datum[0] == "dir":
                current_node._dirs[datum[1]] = Node(name=datum[1], dirs=dict(), files=list(), last_node=current_node)
            else:
                current_node._files.append(int(datum[0]))
    else:
        if datum[2] == "..":
            current_node = current_node._last_node
        else:
            current_node = current_node._dirs[datum[2]]

nodes_size = list()

# Get sizes of all nodes
def get_nodes_sizes(nodes_size: list, node: Node):
    size = 0
    if len(node._dirs) == 0:
        nodes_size.append(node.get_size())
        return nodes_size, node.get_size()
    else:
        for dir in node._dirs:
            nodes_size, temp_size = get_nodes_sizes(nodes_size, node._dirs[dir])
            size = size + temp_size
        nodes_size.append(size + node.get_size())
        return nodes_size, (size + node.get_size())

nodes_size, max_size = get_nodes_sizes(nodes_size, original_node)

def less_than(x):
    return x if x <= 100000 else 0

answer = sum(list(map(less_than, nodes_size)))

free = 70000000 - max_size
to_free = 30000000 - free
file_size_to_delete = 70000000

for size in nodes_size:
    if size >= to_free and size <= file_size_to_delete:
        file_size_to_delete = size

#aocd.submit(answer, day=7, year=2022, part="a")
aocd.submit(file_size_to_delete, day=7, year=2022, part="b")