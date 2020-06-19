def outOfBoard(x, y):
    if x<0 or x>7 or y<0 or y>7:
        return True
    return False

def Rook(x0,y0,friendly,enemy):
    friendlyPos=[(i.xpos,i.ypos) for i in friendly]
    enemyPos=[(i.xpos,i.ypos) for i in enemy]
    move=[]
    take=[]

    x=x0
    y=y0
    while True:
        x+=1
        if (x,y) in enemyPos:
            take.append((x,y))
            break
        elif outOfBoard(x,y) or (x,y) in friendlyPos:
            break
        else:
            move.append((x,y)) 

    x=x0
    y=y0
    while True:
        x-=1
        if (x,y) in enemyPos:
            take.append((x,y))
            break
        elif outOfBoard(x,y) or (x,y) in friendlyPos:
            break
        else:
            move.append((x,y))          

    x=x0
    y=y0
    while True:
        y+=1
        if (x,y) in enemyPos:
            take.append((x,y))
            break
        elif outOfBoard(x,y) or (x,y) in friendlyPos:
            break
        else:
            move.append((x,y)) 

    x=x0
    y=y0
    while True:
        y-=1
        if (x,y) in enemyPos:
            take.append((x,y))
            break
        elif outOfBoard(x,y) or (x,y) in friendlyPos:
            break
        else:
            move.append((x,y))    
    return move, take             


def Bishop(x0,y0,friendly,enemy):
    friendlyPos=[(i.xpos,i.ypos) for i in friendly]
    enemyPos=[(i.xpos,i.ypos) for i in enemy]
    move=[]
    take=[]

    x=x0
    y=y0
    while True:
        x+=1
        y+=1
        if (x,y) in enemyPos:
            take.append((x,y))
            break
        elif outOfBoard(x,y) or (x,y) in friendlyPos:
            break
        else:
            move.append((x,y)) 

    x=x0
    y=y0
    while True:
        x+=1
        y-=1
        if (x,y) in enemyPos:
            take.append((x,y))
            break
        elif outOfBoard(x,y) or (x,y) in friendlyPos:
            break
        else:
            move.append((x,y))          

    x=x0
    y=y0
    while True:
        x-=1
        y+=1
        if (x,y) in enemyPos:
            take.append((x,y))
            break
        elif outOfBoard(x,y) or (x,y) in friendlyPos:
            break
        else:
            move.append((x,y)) 

    x=x0
    y=y0
    while True:
        x-=1
        y-=1
        if (x,y) in enemyPos:
            take.append((x,y))
            break
        elif outOfBoard(x,y) or (x,y) in friendlyPos:
            break
        else:
            move.append((x,y))    
    return move, take        