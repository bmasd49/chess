import math
import gameData

class Move:
    def __init__(self, name, x0, y0, x1, y1, take):
        self.name= name
        self.x0= x0
        self.y0= y0
        self.x1= x1
        self.y1= y1
        self.take= take

    def display(self):
        if self.take == True:
            symbol= 'x'
        else:
            symbol= '-'    
        if self.name == 'p':
            return f'   {chr(self.x0+97)}{self.y0 +1}{symbol}{chr(self.x1+97)}{self.y1 +1}'
        if self.name == 'K' and self.x0 == 4:
            if self.x1 == 6:
                return  '   O-O   '
            elif self.x1 == 2:
                return '   O-O-O '    
        return f'  {self.name}{chr(self.x0+97)}{self.y0 +1}{symbol}{chr(self.x1+97)}{self.y1 +1}'

    def isIn(self, moves):
        for move in moves:
            if self.x0 == move.x0 and self.y0 == move.y0 and self.x1 == move.x1 and self.y1 == move.y1:
                return move
        return False

    def copy(self):
        return Move(self.name, self.x0, self.y0, self.x1, self.y1, self.take) 

class Evaluate:
 
    @staticmethod
    def materialValue(board):
        value= 0
        for x in range(8):
            for y in range(8):
                if board.pieces[x][y] != 0:
                    if board.pieces[x][y].side == 'w':
                        value += gameData.materialValueDictionary[board.pieces[x][y].name]
                    elif board.pieces[x][y].side == 'b':
                        value -= gameData.materialValueDictionary[board.pieces[x][y].name]
        return value

    @staticmethod
    def positionalValue(board, early):
        value= 0
        if early:
            for x in range(8):
                for y in range(8):
                    if board.pieces[x][y] != 0:
                        if board.pieces[x][y].side == 'w':
                            value += gameData.absoluteEarlyPositionalDictionary[board.pieces[x][y].name][7-y][x]
                        elif board.pieces[x][y].side == 'b':
                            value -= gameData.absoluteEarlyPositionalDictionary[board.pieces[x][y].name][y][x]
        else:      
            for x in range(8):
                for y in range(8):
                    if board.pieces[x][y] != 0:
                        if board.pieces[x][y].side == 'w':
                            value += gameData.absoluteLatePositionalDictionary[board.pieces[x][y].name][7-y][x]
                        elif board.pieces[x][y].side == 'b':
                            value -= gameData.absoluteLatePositionalDictionary[board.pieces[x][y].name][y][x]              
        return value
        
    @staticmethod
    def value(board):
        material= Evaluate.materialValue(board)
        early= True if material >= 1100 else False
        return material + Evaluate.positionalValue(board, early)

class AI:
    INFTY= 2*gameData.materialValueDictionary['K']
    @staticmethod
    def AI_Move(board):
        best= AI.INFTY
        legalMoves= board.allLegalMove('b')
        depth= max(2,math.floor(6.0/math.log(len(legalMoves))))
        if len(legalMoves) == 0:
            return None
        for move in legalMoves:
            subBoard= board.copy()
            subBoard.makeMove(move)
            value= AI.minimax(subBoard, depth, True, -AI.INFTY, AI.INFTY)
            if value< best:
                best= value
                finalMove= move
        return finalMove


    @staticmethod    
    def minimax(board, depth, maximizing, alpha, beta):
        if depth == 0:
            return Evaluate.value(board)
    
        if maximizing:
            best= -AI.INFTY
            for move in board.allPossibleMove('w'):
                subBoard= board.copy()
                subBoard.makeMove(move)
                value= AI.minimax(subBoard, depth-1, False, alpha, beta)
                best= max(best, value)
                alpha= max(alpha, best)
                if beta<=alpha:
                    break
            return best
        else:
            best= AI.INFTY
            for move in board.allPossibleMove('b'):
                subBoard= board.copy()
                subBoard.makeMove(move)
                value= AI.minimax(subBoard, depth-1, True, alpha, beta)
                best= min(best, value)
                alpha= min(beta, best)
                if beta<=alpha:
                    break
            return best
