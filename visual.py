def drawBoard(board):
    drawboard=[['  ' for _ in range(8)] for _ in range(8)]
    for i in range(8):
        for j in range(8):
            if board.pieces[i][j]!=0:
                drawboard[j][i]=board.pieces[i][j].display()

    print(f'\n---> Move {board.moveCounter}')
    print('    -----------------------------------------')    
    for i in range(7,-1,-1):
        print(f' {i}  |',end='')
        for j in range(8):
            print('',drawboard[i][j],'|',end='')
        print('\n    -----------------------------------------')
    print('       0    1    2    3    4    5    6    7  ')

  
