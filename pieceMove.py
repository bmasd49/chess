def outOfBoard(x, y):
    if x<0 or x>7 or y<0 or y>7:
        return True
    return False

def Rook(friendly,x0,y0,board):
    move=[]
    take=[]

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
            take.append((x,y))
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
            take.append((x,y))
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
            take.append((x,y))
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
            take.append((x,y))
            break   
    return move, take             


def Bishop(friendly,x0,y0,board):
    move=[]
    take=[]

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
            take.append((x,y))
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
            take.append((x,y))
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
            take.append((x,y))
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
            take.append((x,y))
            break   
    return move, take        

def Knight(friendly,x0,y0,board):
    move=[]
    take=[]

    x=x0+1
    y=y0+2
    if outOfBoard(x,y):
        pass
    elif board[x][y].side=='':
        move.append((x,y))
    elif board[x][y].side==friendly:         
        pass
    else:
        take.append((x,y))

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
        take.append((x,y))

    x=x0+2
    y=y0-1
    if outOfBoard(x,y):
        pass
    elif board[x][y].side=='':
        move.append((x,y))
    elif board[x][y].side==friendly:         
        pass
    else:
        take.append((x,y))

    x=x0+1
    y=y0-2
    if outOfBoard(x,y):
        pass
    elif board[x][y].side=='':
        move.append((x,y))
    elif board[x][y].side==friendly:         
        pass
    else:
        take.append((x,y))

    x=x0-1
    y=y0-2
    if outOfBoard(x,y):
        pass
    elif board[x][y].side=='':
        move.append((x,y))
    elif board[x][y].side==friendly:         
        pass
    else:
        take.append((x,y))

    x=x0-2
    y=y0-1
    if outOfBoard(x,y):
        pass
    elif board[x][y].side=='':
        move.append((x,y))
    elif board[x][y].side==friendly:         
        pass
    else:
        take.append((x,y))

    x=x0-2
    y=y0+1
    if outOfBoard(x,y):
        pass
    elif board[x][y].side=='':
        move.append((x,y))
    elif board[x][y].side==friendly:         
        pass
    else:
        take.append((x,y))

    x=x0-1
    y=y0+2
    if outOfBoard(x,y):
        pass
    elif board[x][y].side=='':
        move.append((x,y))
    elif board[x][y].side==friendly:         
        pass
    else:
        take.append((x,y))

    return move, take        
