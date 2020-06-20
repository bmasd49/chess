def drawBoard(board):
    drawboard=[[None for _ in range(8)] for _ in range(8)]
    for i in range(8):
        for j in range(8):
            drawboard[j][i]=board[i][j].side+board[i][j].name

    print('\n    -----------------------------------------')    
    for i in range(7,-1,-1):
        print(f' {i}  |',end='')
        for j in range(8):
            print('',drawboard[i][j],'|',end='')
        print('\n    -----------------------------------------')
    print('       0    1    2    3    4    5    6    7  ')