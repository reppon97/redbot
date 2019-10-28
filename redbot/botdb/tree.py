class Tree:
    def __init__(self):
        self.root = Node('botdb')

    def populate_structure(self, structure, parent_node):
        for key, branch in structure.items():
            current_node = Node(key)

            if isinstance(branch, dict) and 'handler' in branch:
                current_node.handler = branch['handler']
                current_node.morph = branch['morph']
            else:
                current_node = self.populate_structure(branch, current_node)

            parent_node.append_child(current_node)

        return parent_node

    def populate(self, structure):
        self.populate_structure(structure, self.root)


class Node:
    def __init__(self, value):
        self.value = value
        self.handler = None
        self.morph = False
        self.children = []

    def append_child(self, node):
        self.children.append(node)

    def has_child(self, value):
        for child in self.children:
            if child.value == value:
                return child

        return None
