class Tree:
    def __init__(self):
        self.root = None

    def create_tree(self):
        self.root.board.make_children()
        return

    def __str__(self):

        def recurse(node, level):
            s = ""
            if node:
                s += recurse(node.right, level + 1)
                s += "| " * level
                s += str(node.board) + "\n"
                s += recurse(node.left, level + 1)
            return s

        return recurse(self.root, 0)
