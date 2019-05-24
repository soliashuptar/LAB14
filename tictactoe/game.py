from board import Board, NotValidMoveError, NotEmptyCellError
import copy


def main():
    board = Board()
    print("Start game")
    while not board.has_winner():
        move = input("Make your move: ")
        try:
            board.make_move(move)
        except NotValidMoveError as e:
            board.last_move = -board.last_move
            print("\n{} caught because you've entered wrong move. You`ve missed your turn.".format(e.__class__.__name__))
        except NotEmptyCellError as e:
            board.last_move = -board.last_move
            print("\n{} caught because this cell is already taken. You`ve missed your turn.".format(e.__class__.__name__))
        print(board)
        print("Move of the computer: ")

        variant_1, variant_2 = copy.deepcopy(board), copy.deepcopy(board)
        variant_1.make_random_move()
        variant_2.make_random_move()
        score_1, score_2 = variant_1.compute_score(), variant_2.compute_score()
        board = variant_1 if score_1 >= score_2 else variant_2

        print(board)
        if board.has_winner() != Board.DRAW and board.has_winner():
            return "Player1 won" if board.has_winner() == Board.CROSS else "Computer won"
    return "DRAW"


if __name__ == "__main__":
    print(main())


