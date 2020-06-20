import pieceMove
import visual
class Piece:
    def __init__(self, side= "*", name="*"):
        self.side=side
        self.name=name

pieceorder=['R','N','B','Q','K','B','N','R']
def boardGenerate():
    board=[[Piece('','__') for _ in range(8)] for _ in range(8)]
    for i in range(8):
        board[i][0]=Piece('w',pieceorder[i])
        board[i][1]=Piece('w','p')
        board[i][7]=Piece('b',pieceorder[i])
        board[i][6]=Piece('b','p')

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
    piece=board[x][y]

    if piece.side=='':
        return []
    if piece.name=='R':
        return pieceMove.Rook(piece.side,x,y,board)            
    elif piece.name=='B':
        return pieceMove.Bishop(piece.side,x,y,board)
    elif piece.name=='N':
        return pieceMove.Knight(piece.side,x,y,board)
board=boardGenerate()
xtest=5
ytest=4
board[xtest][ytest]=Piece('w','R')

legalmove=pieceLegalMove(xtest,ytest,board)
for x,y in legalmove[0]:
    board[x][y]=Piece('',' O')

for x,y in legalmove[1]:
    board[x][y]=Piece('',' X')

print(legalmove)    
visual.drawBoard(board)


