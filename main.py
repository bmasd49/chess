import gamePlay, gameBoard, terminalGraphic, os

def getPlayerMove(board, side):
    moveInput= input('Your move is: ')
    if moveInput.lower() in ['q', 'quit', 'exit', ':q']:
        return 0
    moveInput.replace(' ','')    
    try:
        x0= ord(moveInput[0].lower())-97
        y0= int(moveInput[1])-1
        x1= ord(moveInput[2].lower())-97
        y1= int(moveInput[3])-1
    except:
        print('Wrong input format, please type your move again.')
        return getPlayerMove(board, side)

    if not (board.inside(x0, y0) and board.inside(x1, y1)):
        print(f'Your move is out of the board, please try again.')
        return getPlayerMove(board, side)

    if board.pieces[x0][y0] == 0:
        print(f'No piece is found at {chr(x0+97)}{y0+1}, please input another square.')
        return getPlayerMove(board, side)
    move= gamePlay.Move(board.pieces[x0][y0].name, x0, y0, x1, y1, False) 
    if move.isIn(board.allLegalMove(side)) != False:
        return move.isIn(board.allLegalMove(side))
    else:     
        print(f'{gamePlay.Move(board.pieces[x0][y0].name, x0, y0, x1, y1, False).display()} is not a legal move, please input another move.')
        return getPlayerMove(board, side) 

        
if __name__ == "__main__":

    gameBoard= gameBoard.Board.init()
    
    while True:
        terminalGraphic.printGameInfo(gameBoard)
        print(f'Board score:  {gamePlay.Evaluate.value(gameBoard)/10:+.2f}')

        if len(gameBoard.allLegalMove('w')) == 0:
            print('You lose, try again next time!')
        else:    
            playerMove= getPlayerMove(gameBoard, 'w')
        if playerMove == 0:
            break
        gameBoard.makeMove(playerMove)
        terminalGraphic.printGameInfo(gameBoard)
        print('Give me a second to beat you...')
        AIMove=gamePlay.AI.AI_Move(gameBoard)
        if AIMove != None:
            gameBoard.makeMove(AIMove)
        else:
            print('GG I can\', you won!!')
            break
    print('Thanks for playing the game!')        
        


