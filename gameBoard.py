import gamePlay
class Board:
    
    def __init__(self, pieces, moveCounter, moves, enPassantPawn, whiteKing, blackKing):
        self.pieces= pieces
        self.moveCounter= moveCounter
        self.moves= moves
        self.enPassantPawn= enPassantPawn
        self.whiteKing= whiteKing
        self.blackKing= blackKing

    @classmethod
    def init(cls):                          #Initialize the board
        pieceOrder=['R','N','B','Q','K','B','N','R']
        pieces=[[0 for _ in range(8)] for _ in range(8)]
        for i in range(8):
            pieces[i][0]=Piece(i, 0, 'w', pieceOrder[i])
            pieces[i][1]=Piece(i, 1, 'w','p')
            pieces[i][7]=Piece(i, 7, 'b', pieceOrder[i])
            pieces[i][6]=Piece(i, 6, 'b','p')
        whiteKing= King(4, 0, True, True)
        blacKing= King(4, 7, True, True)    
        return cls(pieces, 0, [], None, whiteKing, blacKing)

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
        # moves= []
        # for move in board.moves:
        #     moves.append(move.copy())
        return cls(pieces, board.moveCounter, [], board.enPassantPawn, board.whiteKing.copy(), board.blackKing.copy())

    def allPossibleNonCastleMove(self, side):
        move= []
        for x in range(8):
            for y in range(8):
                if self.pieces[x][y] != 0 and self.pieces[x][y].side == side:
                    move.extend(self.pieces[x][y].legalMoves(self))
        return move

    def allCastleMove(self, side):
        move= []
        if side == 'w':
            if self.whiteKing.kingSideCastle and (self.pieces[5][0] == 0) and (self.pieces[6][0] == 0):
                subBoard= self.copy()
                subBoard.pieces[5][0]= Piece(5, 0, 'w', 'K')
                subBoard.pieces[6][0]= Piece(6, 0, 'w', 'K')
                moves= subBoard.allPossibleNonCastleMove('b')
                if (not subBoard.isControlled(4, 0, moves)) and (not subBoard.isControlled(5, 0, moves)) and (not subBoard.isControlled(6, 0, moves)):
                    move.append(gamePlay.Move('K', 4, 0, 6, 0, False))
            
            if self.whiteKing.queenSideCastle and (self.pieces[3][0] == 0) and (self.pieces[2][0] == 0) and (self.pieces[1][0] == 0):
                subBoard= self.copy()
                subBoard.pieces[3][0]= Piece(3, 0, 'w', 'K')
                subBoard.pieces[2][0]= Piece(2, 0, 'w', 'K')
                moves= subBoard.allPossibleNonCastleMove('b')
                if (not subBoard.isControlled(4, 0, moves)) and (not subBoard.isControlled(3, 0, moves)) and (not subBoard.isControlled(2, 0, moves)):
                    move.append(gamePlay.Move('K', 4, 0, 2, 0, False))

        elif side == 'b':
            if self.blackKing.kingSideCastle and (self.pieces[5][7] == 0) and (self.pieces[6][7] == 0):
                subBoard= self.copy()
                subBoard.pieces[5][7]= Piece(5, 7, 'b', 'K')
                subBoard.pieces[6][7]= Piece(6, 7, 'b', 'K')
                moves= subBoard.allPossibleNonCastleMove('w')
                if (not subBoard.isControlled(4, 7, moves)) and (not subBoard.isControlled(5, 7, moves)) and (not subBoard.isControlled(6, 7, moves)):
                    move.append(gamePlay.Move('K', 4, 7, 6, 7, False)) 
            
            if self.blackKing.queenSideCastle and (self.pieces[3][7] == 0) and (self.pieces[2][7] == 0) and (self.pieces[1][7] == 0):
                subBoard= self.copy()
                subBoard.pieces[3][7]= Piece(3, 7, 'b', 'K')
                subBoard.pieces[2][7]= Piece(2, 7, 'b', 'K')
                moves= subBoard.allPossibleNonCastleMove('w')
                if (not subBoard.isControlled(4, 7, moves)) and (not subBoard.isControlled(3, 7, moves)) and (not subBoard.isControlled(2, 7, moves)):
                    move.append(gamePlay.Move('K', 4, 7, 2, 7, False))             
        return move

    def allPossibleMove(self, side):
        return self.allPossibleNonCastleMove(side) + self.allCastleMove(side)

    def allLegalMove(self, side):
        moves= []
        for move in self.allPossibleNonCastleMove(side):
            subBoard= self.copy()
            subBoard.makeMove(move)
            if not subBoard.isChecked(side):
                moves.append(move)
        return moves + self.allCastleMove(side)

    def makeMove(self, move):             #Literally move a Piece object with information from the class object "Move".
        self.moveCounter += 1
        self.moves.append(move)
        x0= move.x0
        y0= move.y0 
        x1= move.x1
        y1= move.y1
       
        if self.enPassantPawn != None:                                  #Remove previous en passant
            if self.pieces[x0][y0].name == 'p':
                if self.pieces[x0][y0].side == 'w' and y0 == 4 and x1 == self.enPassantPawn:                #Remove pawn taken en passant
                    self.pieces[x1][4]= 0
                elif self.pieces[x0][y0].side == 'b' and y0 == 3 and x1 == self.enPassantPawn:
                    self.pieces[x1][3]= 0    

            self.enPassantPawn= None

        if self.pieces[x0][y0].name == 'p':                                 
            if   y0 == 1 and y1 == 3:                                       #Creating a new en passant square if a pawn moved two squares
                self.enPassantPawn= move.x0
            elif y0 == 6 and y1 == 4:
                self.enPassantPawn= move.x0

            

        if self.pieces[x0][y0].name == 'K':                   
            if   self.pieces[x0][y0].side == 'w':                           #Update white king position
                self.whiteKing.x= x1
                self.whiteKing.y= y1
                if self.whiteKing.kingSideCastle:
                    self.whiteKing.kingSideCastle= False
                    if   x1 == 6 and y1 == 0:                                                   #Castle king side
                        self.pieces[5][y0]= self.pieces[7][y0].moveTo(5, y0)
                        self.pieces[7][y0]= 0
                if self.whiteKing.queenSideCastle:  
                    self.whiteKing.queenSideCastle= False
                    if x1 == 2 and y1 == 0:                                                     #Castle queen side
                        self.pieces[3][y0]= self.pieces[0][y0].moveTo(3, y0)
                        self.pieces[0][y0]= 0  
                    

            elif self.pieces[x0][y0].side == 'b':                           #Update black king position
                self.blackKing.x= x1
                self.blackKing.y= y1
                if self.blackKing.kingSideCastle:                           #If king moved then cannot castle anymore
                    self.blackKing.kingSideCastle= False
                    if x1 == 6 and y1 == 7:                                                   #Castle king side
                        self.pieces[5][y0]= self.pieces[7][y0].moveTo(5, y0)
                        self.pieces[7][y0]= 0
                if self.blackKing.queenSideCastle:    
                    self.blackKing.queenSideCastle= False
                    if x1 == 2 and y1 == 0:                                                   #Castle queen side
                        self.pieces[3][y0]= self.pieces[0][y0].moveTo(3, y0)
                        self.pieces[0][y0]= 0     


        if self.pieces[x0][y0].name == 'R':                                 #If rook moved then cannot castle anymore
            if x0 == 0:
                if y0 == 0:
                    self.whiteKing.queenSideCastle= False
                elif y0 == 7:
                    self.blackKing.queenSideCastle= False
            elif x0 == 7:
                if y0 == 0:
                    self.whiteKing.kingSideCastle= False
                elif y0 == 7:
                    self.blackKing.kingSideCastle= False 

        if x1 == 0:
            if y1 == 0:
                self.whiteKing.queenSideCastle= False
            elif y1 == 7:
                self.blackKing.queenSideCastle= False   
        elif x1 ==7:
            if y1 == 0:
                self.whiteKing.kingSideCastle= False
            elif y1 == 7:
                self.blackKing.kingSideCastle= False                      

        self.pieces[x1][y1]= self.pieces[x0][y0].moveTo(x1, y1)
        self.pieces[x0][y0]= 0    

        if self.pieces[x1][y1].name == 'p' and y1 in [0, 7]:                                                #Pawn promotion
            self.pieces[x1][y1].promote()  

    @staticmethod
    def inside(x ,y):         #Check if the value x, y is inside the board.
        if (x>-1) and (x<8) and (y>-1) and (y<8):
            return True
        else:
            return False    

    def isControlled(self, x, y, moves):
        for move in moves:
            if move.x1 == x and move.y1 == y:
                return True
        return False

    def isChecked(self, side):
        if side == 'w':
            if self.isControlled(self.whiteKing.x, self.whiteKing.y, self.allPossibleNonCastleMove('b')):
                return True
        elif side == 'b':
            if self.isControlled(self.blackKing.x, self.blackKing.y, self.allPossibleNonCastleMove('w')):
                return True        
        return False


class Piece:
    def __init__(self, x, y, side, name):
        self.x= x
        self.y= y
        self.side= side
        self.name= name

    def display(self):              #Show side and name of a Piece
        # return f'{self.x}{self.y}'
        if self.side == 'w':
            if self.name == 'p':
                return '\u2659 '
            elif self.name == 'N':
                return '\u2658 '
            elif self.name == 'B':    
                return '\u2657 '
            elif self.name == 'R':
                return '\u2656 '
            elif self.name == 'Q':
                return '\u2655 '
            elif self.name == 'K':
                return '\u2654 '  
        elif self.side == 'b':
            if self.name == 'p':
                return '\u265F '
            elif self.name == 'N':
                return '\u265E '
            elif self.name == 'B':    
                return '\u265D '
            elif self.name == 'R':
                return '\u265C '
            elif self.name == 'Q':
                return '\u265B '
            elif self.name == 'K':
                return '\u265A '                  



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

    def promote(self):
        self.name= 'Q'

class King:
    def __init__(self, x, y, kingSideCastle, queenSideCastle):
        self.x= x
        self.y= y
        self.kingSideCastle= kingSideCastle
        self.queenSideCastle= queenSideCastle

    def copy(self):
        return King(self.x, self.y, self.kingSideCastle, self.queenSideCastle)    


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
                move.append(gamePlay.Move('p', x0, y0, x0, y0 +direction, False))
                if   y0==1 and direction == 1 and board.pieces[x0][3] == 0:           #Double move
                    move.append(gamePlay.Move('p',x0, y0, x0, 3, False))
                elif y0==6 and direction == -1 and board.pieces[x0][4] == 0:
                    move.append(gamePlay.Move('p',x0, y0, x0, 4, False))

        for i in [-1, 1]:                                                           #Normal take
            if board.inside(x0 +i, y0 +direction):
                if board.pieces[x0 +i][y0 +direction] != 0 and board.pieces[x0 +i][y0 +direction].side != piece.side:
                    move.append(gamePlay.Move('p',x0, y0, x0 +i, y0 +direction, True))


        if   y0 == 4:                                                                 #En passant take for white
            if direction == 1  and board.enPassantPawn in [x0-1, x0+1]:
                    move.append(gamePlay.Move('p', x0, y0, board.enPassantPawn, y0 +direction, True))
        elif y0 == 3:                                                                   #En passant take for black
            if direction == -1 and board.enPassantPawn in [x0-1, x0+1]:
                    move.append(gamePlay.Move('p', x0, y0, board.enPassantPawn, y0 +direction, True))

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
                    move.append(gamePlay.Move('N', x0, y0, x0 +x, y0 +y, False))
                elif board.pieces[x0+x][y0+y].side != piece.side:
                    move.append(gamePlay.Move('N', x0, y0, x0 +x, y0 +y, True))
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
                        move.append(gamePlay.Move('B', x0, y0, x0 +step*i[0], y0 +step*i[1], False))
                    elif board.pieces[x0 +step*i[0]][y0 +step*i[1]].side == piece.side:
                        break
                    else: 
                        move.append(gamePlay.Move('B', x0, y0, x0 +step*i[0], y0 +step*i[1], True))
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
                        move.append(gamePlay.Move('Q', x0, y0, x0 +step*i[0], y0 +step*i[1], False))
                    elif board.pieces[x0 +step*i[0]][y0 +step*i[1]].side == piece.side:
                        break
                    else: 
                        move.append(gamePlay.Move('Q', x0, y0, x0 +step*i[0], y0 +step*i[1], True))
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
                        move.append(gamePlay.Move('R', x0, y0, x0 +step*i[0], y0 +step*i[1], False))
                    elif board.pieces[x0 +step*i[0]][y0 +step*i[1]].side == piece.side:
                        break
                    else: 
                        move.append(gamePlay.Move('R', x0, y0, x0 +step*i[0], y0 +step*i[1], True))
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
                    move.append(gamePlay.Move('K', x0, y0, x0 +i[0], y0 +i[1], False))
                elif board.pieces[x0 +i[0]][y0 +i[1]].side != piece.side:
                    move.append(gamePlay.Move('K', x0, y0, x0 +i[0], y0 +i[1], True))
        return move  




