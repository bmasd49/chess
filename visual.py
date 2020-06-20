def drawBoard(board):
    drawboard=[[None for _ in range(8)] for _ in range(8)]
    for i in range(8):
        for j in range(8):
            drawboard[j][i]=board[i][j].side+board[i][j].name

    for i in range(7,-1,-1):
        print(drawboard[i])