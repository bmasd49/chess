import gameplay, data, visual, os

def getPlayerMove(board):
    print('\nPlease input your move as: <x from><y from> <x to><y to>')
    print('For example, if you want to move a piece from (4,1) to (4,3), type: "41 43" (without quotation marks) then hit <ENTER>')
    print('Type q or quit to exit.\n')
    moveInput= input('Your move is: ')
    if moveInput.lower() in ['q', 'quit', 'exit']:
        return 0
    try:
        x0= int(moveInput[0])
        y0= int(moveInput[1])
        x1= int(moveInput[3])
        y1= int(moveInput[4])
    except ValueError:
        print('Wrong input format, please type your move again.')
        return getPlayerMove(board)

    if board.pieces[x0][y0] != 0:
        return gameplay.Move(board.pieces[x0][y0].name, x0, y0, x1, y1)
    else:
        print(f'No piece is found at {x0,y0}, please input another square.')
        return getPlayerMove(board)

if __name__ == "__main__":

    gameBoard= data.Board.init()
    while True:
        visual.clearScreen()
        visual.drawBoard(gameBoard)
        visual.drawMove(gameBoard)
        playerMove= getPlayerMove(gameBoard)
        if playerMove == 0:
            break
        gameBoard.makeMove(playerMove)
        


