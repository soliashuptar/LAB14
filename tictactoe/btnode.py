class Node:
    def __init__(self, board, left=None, right=None):
        self.board = board
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.board)

    def getLeafCount(self, node):
        if node is None:
            return 0
        elif node.left is None and node.right is None:
            return 1
        else:
            return Node.getLeafCount(node.right) + Node.getLeafCount(node.left)
