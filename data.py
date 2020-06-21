import gameplay
class Board:
    
    def __init__(self, pieces, moveCounter, moves, enPassantPawn, canWhiteCastle, canBlackCastle):
        self.pieces= pieces
        self.moveCounter= moveCounter
        self.moves= moves
        self.enPassantPawn= enPassantPawn
        self.canWhiteCastle= canWhiteCastle
        self.canBlackCastle= canBlackCastle

    @classmethod
    def init(cls):                          #Initialize the board
        pieceOrder=['R','N','B','Q','K','B','N','R']
        pieces=[[0 for _ in range(8)] for _ in range(8)]
        for i in range(8):
            pieces[i][0]=Piece(i, 0, 'w', pieceOrder[i])
            pieces[i][1]=Piece(i, 1, 'w','p')
            pieces[i][7]=Piece(i, 7, 'b', pieceOrder[i])
            pieces[i][6]=Piece(i, 6, 'b','p')
        return cls(pieces, 0, [], None, True, True)

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
        return cls(pieces, board.moveCounter, board.moves, board.enPassantPawn, board.canWhiteCastle, board.canBlackCastle)

    def allPossibleMove(self, side):
        pass

    def makeMove(self, move):             #Literally move a Piece object with information from the class object "Move".
        self.moveCounter += 1
        self.moves.append(move)
        x0= move.x0
        y0= move.y0 
        x1= move.x1
        y1= move.y1

        if self.enPassantPawn != None:                                  #Remove previous en passant
            self.enPassantPawn= None

        if self.pieces[x0][y0].name == 'p':                   #Creating a new en passant square if a pawn moved two squares
            if   y0 == 1 and y1 == 3:
                self.enPassantPawn= move.x0
            elif y0 == 6 and y1 == 4:
                self.enPassantPawn= move.x0

        if self.pieces[x0][y0].name == 'K':                   #Castling move
            if   x1 == 6:
                self.pieces[5][y0]= self.pieces[7][y0].moveTo(5, y0)
                self.pieces[7][y0]= 0
            elif x1 == 2:
                self.pieces[3][y0]= self.pieces[0][y0].moveTo(3, y0)
                self.pieces[0][y0]= 0

        self.pieces[x1][y1]= self.pieces[x0][y0].moveTo(x1, y1)
        self.pieces[x0][y0]= 0        

    @staticmethod
    def inside(x ,y):         #Check if the value x, y is inside the board.
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
        #return self.side +self.name
        return self.side+self.name
    def copy(self):
        return Piece(self.x, self.y, self.side, self.name)              #Copy the piece

    def moveTo(self, x1, y1):
        self.x= x1 
        self.y= y1
        return self

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


class legalMoveOf:
    @staticmethod
    def pawn(piece, board):
        x0= piece.x
        y0= piece.y
        move= []
        if piece.side == 'w':
            direction = 1
        elif piece.side == 'b':
            direction = -1    

                                                          
        if board.inside(x0, y0 +direction):                                         #Normal move
            if board.pieces[x0][y0 +direction] == 0:
                move.append(gameplay.Move('p', x0, y0, x0, y0 +direction))
                if   y0==1 and direction==1 and board.pieces[x0][3] == 0:           #Double move
                    move.append(gameplay.Move('p',x0, y0, x0, 3))
                elif y0==6 and direction==1 and board.pieces[x0][4] == 0:
                    move.append(gameplay.Move('p',x0, y0, x0, 4))

        for i in [-1, 1]:                                                           #Normal take
            if board.inside(x0 +i, y0 +direction):
                if board.pieces[x0 +i][y0 +direction] != 0:
                    move.append(gameplay.Move('p',x0, y0, x0 +i, y0 +direction))


        if   y0 == 4:                                                                 #En passant take for white
            if direction == 1  and board.moveCounter %2 == 0 and board.enPassantPawn in [x0-1, x0+1]:
                    move.append(gameplay.Move('p',x0, y0, board.enPassantPawn, y0 +direction))
        elif y0 == 3:                                                                   #En passant take for black
            if direction == -1 and board.moveCounter %2 == 1 and board.enPassantPawn in [x0-1, x0+1]:
                    move.append(gameplay.Move('p',x0, y0, board.enPassantPawn, y0 +direction))

        return move    

    @staticmethod
    def Knight(piece, board):
        x0= piece.x
        y0= piece.y
        move= []

        relativeMove= [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

        for (x, y) in relativeMove:
            if board.inside(x0+x, y0+y):
                if board.pieces[x0+x][y0+y] == 0:
                    move.append(gameplay.Move('K', x0, y0, x0 +x, y0 +y))
                elif board.pieces[x0+x][y0+y].side != piece.side:
                    move.append(gameplay.Move('K', x0, y0, x0 +x, y0 +y))
        return move

    @staticmethod
    def Bishop(piece, board):
        x0= piece.x
        y0= piece.y
        move= []

        direction= [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        for i in direction:
            step= 0
            while True:
                step +=1
                if board.inside(x0 +step*i[0], y0 +step*i[1]):
                    if board.pieces[x0 +step*i[0]][y0 +step*i[1]] == 0:
                        move.append(gameplay.Move('B', x0, y0, x0 +step*i[0], y0 +step*i[1]))
                    elif board.pieces[x0 +step*i[0]][y0 +step*i[1]].side == piece.side:
                        break
                    else: 
                        move.append(gameplay.Move('B', x0, y0, x0 +step*i[0], y0 +step*i[1]))
                        break
                else:
                     break    
        return move            

    @staticmethod    
    def Queen(piece, board):
        x0= piece.x
        y0= piece.y
        move= []

        direction= [(1, 1), (1, -1), (-1, -1), (-1, 1), (1, 0), (0, -1), (-1, 0), (0, 1)]
        for i in direction:
            step= 0
            while True:
                step +=1
                if board.inside(x0 +step*i[0], y0 +step*i[1]):
                    if board.pieces[x0 +step*i[0]][y0 +step*i[1]] == 0:
                        move.append(gameplay.Move('Q', x0, y0, x0 +step*i[0], y0 +step*i[1]))
                    elif board.pieces[x0 +step*i[0]][y0 +step*i[1]].side == piece.side:
                        break
                    else: 
                        move.append(gameplay.Move('Q', x0, y0, x0 +step*i[0], y0 +step*i[1]))
                        break
                else:
                     break    
        return move          


    @staticmethod    
    def Rook(piece, board):
        x0= piece.x
        y0= piece.y
        move= []

        direction= [(1, 0), (0, -1), (-1, 0), (0, 1)]
        for i in direction:
            step= 0
            while True:
                step +=1
                if board.inside(x0 +step*i[0], y0 +step*i[1]):
                    if board.pieces[x0 +step*i[0]][y0 +step*i[1]] == 0:
                        move.append(gameplay.Move('R', x0, y0, x0 +step*i[0], y0 +step*i[1]))
                    elif board.pieces[x0 +step*i[0]][y0 +step*i[1]].side == piece.side:
                        break
                    else: 
                        move.append(gameplay.Move('R', x0, y0, x0 +step*i[0], y0 +step*i[1]))
                        break
                else:
                     break    
        return move    

    @staticmethod    
    def King(piece, board):
        x0= piece.x
        y0= piece.y
        move= []

        direction= [(1, 1), (1, -1), (-1, -1), (-1, 1), (1, 0), (0, -1), (-1, 0), (0, 1)]
        for i in direction:
            if board.inside(x0 +i[0], y0 +i[1]):
                if board.pieces[x0 +i[0]][y0 +i[1]] == 0:
                    move.append(gameplay.Move('K', x0, y0, x0 +i[0], y0 +i[1]))
                elif board.pieces[x0 +i[0]][y0 +i[1]].side != piece.side:
                    move.append(gameplay.Move('K', x0, y0, x0 +i[0], y0 +i[1]))
        return move  




