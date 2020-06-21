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

    # @staticmethod
    # def castle(cls, side, direction):
    #     if side == 'w':
    #         if direction == 'K':
    #             return cls(4, 0, 6, 0), cls(7, 0, 5, 0)
    #         elif direction == 'Q':
    #             return cls(4, 0, 2, 0), cls(0, 0, 3, 0)   
    #     elif side == 'b':
    #         if direction == 'K':
    #             return cls(4, 7, 6, 7), cls(7, 7, 5, 7)
    #         elif direction == 'Q':
    #             return cls(4, 7, 2, 7), cls(7, 7, 3, 7)          


class Evaluate:
    @staticmethod
    def value(board):
        pass

class AI:

    pass       