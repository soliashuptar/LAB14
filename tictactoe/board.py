import random
import copy
from btree import Tree
from btnode import Node


class NotValidMoveError(Exception):
    pass


class NotEmptyCellError(Exception):
    pass


def generate_winning_combinations():
    all = []
    for i in range(3):
        combination_1 = []
        combination_2 = []
        for j in range(3):
            combination_1.append((i, j))
            combination_2.append((j, i))
        all.append(combination_1)
        all.append(combination_2)

    all.append([(0, 0), (1, 1), (2, 2)])
    all.append([(0, 2), (1, 1), (2, 0)])
    return all


class Board:
    NOUGHT = 1
    CROSS = -1
    EMPTY = 0

    NOUGHT_WINNER = 1
    CROSS_WINNER = -1
    DRAW = 2
    NOT_FINISHED = 0

    WINNING_COMBINATIONS = generate_winning_combinations()

    POSSIBLE_MOVES = [(i, j) for i in range(3) for j in range(3)]

    def __init__(self):
        self.cells = [[0] * 3 for _ in range(3)]
        self.last_move = Board.NOUGHT
        self.number_of_moves = 0

    def make_random_move(self):
        possible_moves = []
        for i in range(3):
            for j in range(3):
                if self.cells[i][j] == Board.EMPTY:
                    possible_moves.append((i, j))
        if len(possible_moves) != 0:
            cell = random.choice(possible_moves)
            self.last_move = -self.last_move
            self.cells[cell[0]][cell[1]] = self.last_move
            self.number_of_moves += 1
            return True

    @staticmethod
    def valid_move(cell):
        if (cell[0], cell[1]) not in Board.POSSIBLE_MOVES:
            return False
        for i in cell:
            if not 0 <= i <= 2:
                return False
        return True

    def make_move(self, cell):
        cell = cell.split(",")
        cell = [int(i) for i in cell]
        if not Board.valid_move(cell):
            raise NotValidMoveError

        if self.cells[cell[0]][cell[1]] != 0:
            raise NotEmptyCellError

        self.last_move = -self.last_move
        self.cells[cell[0]][cell[1]] = self.last_move
        Board.POSSIBLE_MOVES.remove((cell[0], cell[1]))
        self.number_of_moves += 1
        return True

    def __str__(self):
        transform = {0: " ", 1: "O", -1: "X"}
        return "\n".join([" ".join(map(lambda x: transform[x], row)) for row in self.cells])

    def has_winner(self):
        for combination in self.WINNING_COMBINATIONS:
            lst = []
            for cell in combination:
                lst.append(self.cells[cell[0]][cell[1]])
            if max(lst) == min(lst) and max(lst) != Board.EMPTY:
                return max(lst)
        if self.number_of_moves == 9:
            return Board.DRAW

        return Board.NOT_FINISHED

    def compute_score(self):
        has_winner = self.has_winner()
        if has_winner:
            winner_scores = {Board.NOUGHT_WINNER: 1, Board.CROSS_WINNER: -1, Board.DRAW: 0}
            return winner_scores[has_winner]
        n1 = Node(self)
        board = Tree()
        board.root = n1
        right_board = left_board = copy.deepcopy(self)
        left_move, right_move = left_board.make_random_move(), right_board.make_random_move()
        board.root.left = Node(left_move)
        board.root.right = Node(right_move)
        return left_board.compute_score() + right_board.compute_score()
