def outOfBoard(x, y):
    if x<0 or x>7 or y<0 or y>7:
        return True
    return False


def Rook(friendly,x0,y0,board):
    move=[]

    x=x0
    y=y0
    while True:
        x+=1
        if outOfBoard(x,y):
            break
        elif board[x][y].side=='':
            move.append((x,y))
        elif board[x][y].side==friendly:         
            break
        else:
            move.append((x,y))
            break

    x=x0
    y=y0
    while True:
        x-=1
        if outOfBoard(x,y):
            break
        elif board[x][y].side=='':
            move.append((x,y))
        elif board[x][y].side==friendly:         
            break
        else:
            move.append((x,y))
            break         

    x=x0
    y=y0
    while True:
        y+=1
        if outOfBoard(x,y):
            break
        elif board[x][y].side=='':
            move.append((x,y))
        elif board[x][y].side==friendly:         
            break
        else:
            move.append((x,y))
            break 

    x=x0
    y=y0
    while True:
        y-=1
        if outOfBoard(x,y):
            break
        elif board[x][y].side=='':
            move.append((x,y))
        elif board[x][y].side==friendly:         
            break
        else:
            move.append((x,y))
            break   
    return move            


def Bishop(friendly,x0,y0,board):
    move=[]


    x=x0
    y=y0
    while True:
        x+=1
        y+=1
        if outOfBoard(x,y):
            break
        elif board[x][y].side=='':
            move.append((x,y))
        elif board[x][y].side==friendly:         
            break
        else:
            move.append((x,y))
            break

    x=x0
    y=y0
    while True:
        x+=1
        y-=1
        if outOfBoard(x,y):
            break
        elif board[x][y].side=='':
            move.append((x,y))
        elif board[x][y].side==friendly:         
            break
        else:
            move.append((x,y))
            break         

    x=x0
    y=y0
    while True:
        x-=1
        y+=1
        if outOfBoard(x,y):
            break
        elif board[x][y].side=='':
            move.append((x,y))
        elif board[x][y].side==friendly:         
            break
        else:
            move.append((x,y))
            break

    x=x0
    y=y0
    while True:
        x-=1
        y-=1
        if outOfBoard(x,y):
            break
        elif board[x][y].side=='':
            move.append((x,y))
        elif board[x][y].side==friendly:         
            break
        else:
            move.append((x,y))
            break   
    return move     


def Knight(friendly,x0,y0,board):
    move=[]


    x=x0+1
    y=y0+2
    if outOfBoard(x,y):
        pass
    elif board[x][y].side=='':
        move.append((x,y))
    elif board[x][y].side==friendly:         
        pass
    else:
        move.append((x,y))

    x=x0+2
    y=y0+1
    if outOfBoard(x,y):
        pass
        print('passed')
    elif board[x][y].side=='':
        move.append((x,y))
    elif board[x][y].side==friendly:         
        pass
    else:
        move.append((x,y))

    x=x0+2
    y=y0-1
    if outOfBoard(x,y):
        pass
    elif board[x][y].side=='':
        move.append((x,y))
    elif board[x][y].side==friendly:         
        pass
    else:
        move.append((x,y))

    x=x0+1
    y=y0-2
    if outOfBoard(x,y):
        pass
    elif board[x][y].side=='':
        move.append((x,y))
    elif board[x][y].side==friendly:         
        pass
    else:
        move.append((x,y))

    x=x0-1
    y=y0-2
    if outOfBoard(x,y):
        pass
    elif board[x][y].side=='':
        move.append((x,y))
    elif board[x][y].side==friendly:         
        pass
    else:
        move.append((x,y))

    x=x0-2
    y=y0-1
    if outOfBoard(x,y):
        pass
    elif board[x][y].side=='':
        move.append((x,y))
    elif board[x][y].side==friendly:         
        pass
    else:
        move.append((x,y))

    x=x0-2
    y=y0+1
    if outOfBoard(x,y):
        pass
    elif board[x][y].side=='':
        move.append((x,y))
    elif board[x][y].side==friendly:         
        pass
    else:
        move.append((x,y))

    x=x0-1
    y=y0+2
    if outOfBoard(x,y):
        pass
    elif board[x][y].side=='':
        move.append((x,y))
    elif board[x][y].side==friendly:         
        pass
    else:
        move.append((x,y))

    return move       


def Queen(friendly,x0,y0,board):
    return Rook(friendly,x0,y0,board) + Bishop(friendly,x0,y0,board)


def King(friendly,x0,y0,board):
    move=[]

    x=x0
    y=y0+1
    if outOfBoard(x,y):
        pass
    elif board[x][y].side=='':
        move.append((x,y))
    elif board[x][y].side==friendly:         
        pass
    else:
        move.append((x,y))

    x=x0+1
    y=y0+1
    if outOfBoard(x,y):
        pass
    elif board[x][y].side=='':
        move.append((x,y))
    elif board[x][y].side==friendly:         
        pass
    else:
        move.append((x,y))

    x=x0+1
    y=y0
    if outOfBoard(x,y):
        pass
    elif board[x][y].side=='':
        move.append((x,y))
    elif board[x][y].side==friendly:         
        pass
    else:
        move.append((x,y))

    x=x0+1
    y=y0-1
    if outOfBoard(x,y):
        pass
    elif board[x][y].side=='':
        move.append((x,y))
    elif board[x][y].side==friendly:         
        pass
    else:
        move.append((x,y))    

    x=x0
    y=y0-1
    if outOfBoard(x,y):
        pass
    elif board[x][y].side=='':
        move.append((x,y))
    elif board[x][y].side==friendly:         
        pass
    else:
        move.append((x,y))    

    x=x0-1
    y=y0-1
    if outOfBoard(x,y):
        pass
    elif board[x][y].side=='':
        move.append((x,y))
    elif board[x][y].side==friendly:         
        pass
    else:
        move.append((x,y))    

    x=x0-1
    y=y0
    if outOfBoard(x,y):
        pass
    elif board[x][y].side=='':
        move.append((x,y))
    elif board[x][y].side==friendly:         
        pass
    else:
        move.append((x,y))   

    x=x0-1
    y=y0+1
    if outOfBoard(x,y):
        pass
    elif board[x][y].side=='':
        move.append((x,y))
    elif board[x][y].side==friendly:         
        pass
    else:
        move.append((x,y)) 

    return move                   