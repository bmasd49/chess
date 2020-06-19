import pieceMove
import visual
class Piece:
    def __init__(self, side= "*", name="*"):
        self.side=side
        self.name=name

pieceorder=['R','N','B','Q','K','B','N','R']
def boardGenerate():
    board=[['' for _ in range(8)] for _ in range(8)]
    for i in range(8):
        board[i][0]=Piece('w',pieceorder[i])
        board[i][1]=Piece('w','p')
        board[i][7]=Piece('b',pieceorder[i])
        board[i][6]=Piece('b','p')
    # white=[Piece('w','K',4,0), Piece('w','Q',3,0), Piece('w','B',2,0), Piece('w','B',5,0),
    #        Piece('w','N',1,0), Piece('w','N',6,0), Piece('w','R',0,0), Piece('w','R',7,0)]+[
    #        Piece('w','p',i,1) for i in range(8)]
    # black=[Piece('b','K',4,7), Piece('b','Q',3,7), Piece('b','B',2,7), Piece('b','B',5,7),
    #        Piece('b','N',1,7), Piece('b','N',6,7), Piece('b','R',0,7), Piece('b','R',7,7)]+[
    #        Piece('b','p',i,6) for i in range(8)]
    return board

def pieceValue(piece):
    name= piece.name
    if   name=="K":
        val=100
    elif name=="Q":
        val=9
    elif name=="R":
        val=5
    elif name=="B" or name=="N":
        val=3
    elif name=="p":
        val=1
    else:
        val=0

    if   piece.side=='w':
        return val
    elif piece.side=='b':
        return -val

def totalValue(board):
    sum=0
    for i in range(8):
        for j in range(8):
            if board[i][j]!='':
                sum+=pieceValue(board[i][j])
    return sum

def pieceLegalMove(x, y, board):
    if board[x][y]=='':
        return ''
    piece=board[x][y]    
    side=piece.side
    if piece.name=='R':
        return pieceMove.Rook(side,x,y,board)            
    
board=boardGenerate()
print(totalValue(board))
board[5][3]=Piece('w','R')
print(pieceLegalMove(5,3,board))

visual.drawBoard(board)


