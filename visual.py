import os
def drawBoard(board):
    drawboard=[['  ' for _ in range(8)] for _ in range(8)]
    for i in range(8):
        for j in range(8):
            if board.pieces[i][j]!=0:
                drawboard[j][i]=board.pieces[i][j].display()

    print('    -----------------------------------------')    
    for i in range(7,-1,-1):
        print(f' {i+1}  |',end='')
        for j in range(8):
            print('',drawboard[i][j],'|',end='')
        print('\n    -----------------------------------------')
    print('       A    B    C    D    E    F    G    H  ')

def drawMove(board):
    i= 1
    for move in board.moves:
        i +=1
        if i%2==0:
            print(f'Move {int(i/2)}: ', move.display(), end='   ') 
        
        else:    
            print(move.display()) 
    if i%2 == 0:
        print()   
    print()      
       

def clearScreen():
    if os.name == 'nt': 
        os.system('cls') 
    else:
        os.system('clear')         
            
        
