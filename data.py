class Board:
    
    def __init__(self, pieces, moveCounter, enPassantPawn, canWhiteCastle, canBlackCastle):
        self.pieces= pieces
        self.moveCounter= moveCounter
        self.enPassantPawn= enPassantPawn
        self.canWhiteCastle= canWhiteCastle
        self.canBlackCastle= canBlackCastle
    @classmethod
    def init(cls):                          #Initialize the board
        pieceOrder=['R','N','B','Q','K','B','N','R']
        pieces=[[0 for _ in range(8)] for _ in range(8)]
        for i in range(8):
            pieces[i][0]=Piece(i, 0, 'w', pieceOrder[i])
            pieces[i][1]=Piece(i, 0, 'w','p')
            pieces[i][7]=Piece(i, 0, 'b', pieceOrder[i])
            pieces[i][6]=Piece(i, 0, 'b','p')
        return cls(pieces, 0, None, True, True)

    def copy(self):                         #Copy the board, useful for recursion.
        return self.makeCloneOf(self)

    @classmethod
    def makeCloneOf(cls, board):                  
        pieces = [[0 for _ in range(8)] for _ in range(8)]
        for x in range(8):
            for y in range(8):
                piece = board.pieces[x][y]
                if piece != 0:
                    pieces[x][y] = piece.copy()
        return cls(pieces, board.moveCounter, board.enPassantPawn, board.canWhiteCastle, board.canBlackCastle)

    def allPossibleMove(self, side):
        pass

    def makeMove(self, move):             #Literally move an Piece object with information from the class object "Move".
        self.moveCounter += 1

        if self.enPassantPawn != None:                                  #Remove previous en passant
            self.enPassantPawn= None

        if self.pieces[move.x0][move.y0].name == 'p':                   #Creating a new en passant square if a pawn moved two squares
            if   move.y0 == 1 and move.y1 == 3:
                self.enPassantPawn= move.x0
            elif move.y0 == 6 and move.y1 == 4:
                self.enPassantPawn= move.x0

        self.pieces[move.x1][move.y1]= self.pieces[move.x0][move.y0]
        self.pieces[move.x0][move.y0]= 0

        if move.castle == True:
            if   move.x1 == 6:
                self.pieces[5][move.y0]= self.pieces[7][move.y0]
                self.pieces[7][move.y0]= 0
            elif move.x1 == 2:
                self.pieces[3][move.y0]= self.pieces[0][move.y0]
                self.pieces[0][move.y0]= 0

    def inside(self, x ,y):         #Check if the value x, y is inside the board.
        if (x>-1) and (x<8) and (y>-1) and (y<8):
            return True
        else:
            return False    


class Piece:
    def __init__(self, x, y, side, name):
        self.x= x
        self.y= y
        self.side= side
        self.name= name

    def display(self):              #Show side and name of a Piece
        if self.name == 'ep':
            return '  '
        else:    
            return self.side +self.name

    def copy(self):
        return Piece(self.x, self.y, self.side, self.name)              #Copy the piece

    def legalMoves(self, board):                                     #Get all possible moves of a Piece
        if   self.name=='p':
            return legalMoveOf.pawn(self, board)  
        elif self.name=='N':
            return legalMoveOf.Knight(self, board)
        elif self.name=='B':
            return legalMoveOf.Bishop(self, board)
        elif self.name=='Q':
            return legalMoveOf.Queen(self, board)  
        elif self.name=='R':
            return legalMoveOf.Rook(self, board)   
        elif self.name=='K':
            return legalMoveOf.King(self, board)  
        else:
            return 0    


class legalMoveOf:                                              #How a piece move, will be finished later
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
        pass

    @staticmethod 
    def King(piece, board):
        pass   
    pass



