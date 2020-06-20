class Board:
    def __init__(self, pieces):
        self.pieces = pieces

    @classmethod
    def init(cls):  
        pieceOrder=['R','N','B','Q','K','B','N','R']
        pieces=[[0 for _ in range(8)] for _ in range(8)]
        for i in range(8):
            pieces[i][0]=Piece(i, 0, 'w', pieceOrder[i])
            pieces[i][1]=Piece(i, 0, 'w','p')
            pieces[i][7]=Piece(i, 0, 'b', pieceOrder[i])
            pieces[i][6]=Piece(i, 0, 'b','p')
        return cls(pieces)

    def copy(self):
        return self.clone(self)

    @classmethod
    def clone(cls, board):
        pieces = [[0 for _ in range(8)] for _ in range(8)]
        for x in range(8):
            for y in range(8):
                piece = board.pieces[x][y]
                if piece != 0:
                    pieces[x][y] = piece.copy()
        return cls(pieces)

    def allPossibleMove(self, side):
        pass

    def makeMove(self):
        pass

    def getPieceAt(self, x, y):
        pass

    def inside(self, x ,y):
        pass


class Piece:
    def __init__(self, x, y, side, name):
        self.x= x
        self.y= y
        self.side= side
        self.name= name

    def display(self):
        return self.side +self.name

    def copy(self):
        return Piece(self.x, self.y, self.side, self.name)

    def possibleMoves(self, board):
        if self.name=='p':
            return moveOfPiece.pawn(self, board)  
        elif self.name=='N':
            return moveOfPiece.Knight(self, board)
        elif self.name=='B':
            return moveOfPiece.Bishop(self, board)
        elif self.name=='Q':
            return moveOfPiece.Queen(self, board)  
        elif self.name=='R':
            return moveOfPiece.Rook(self, board)   
        elif self.name=='K':
            return moveOfPiece.King(self, board)  
        else:
            return 0    


class moveOfPiece:
    @staticmethod
    def pawn(piece, board):
        pass

    @staticmethod    
    def Knight(piece, board):
        pass

    @staticmethod 
    def Bishop(piece, board):
        pass

    @staticmethod 
    def Queen(piece, board):
        pass

    @staticmethod 
    def Rook(piece, board):
        return 'DKM'

    @staticmethod 
    def King(piece, board):
        pass   
    pass



