# Class Board store pieces, class Piece store information of a piece.
# I am going to write a function that can return every possible move of the board (Board.allPossibleMoves())
# That function will return an array of class Move (as below)
# I think you can work with the evaluate class first, because you know more than me about how to evaluate a position in chess.
# We may work on the AI together later.


class Move:
    def __init__(self, x0, y0, x1, y1, castle):
        self.x0= x0
        self.y0= y0
        self.x1= x1
        self.y1= y1
        self.castle= castle

class Evaluate:
    @staticmethod
    def value(board):
        pass

class AI:

    pass       