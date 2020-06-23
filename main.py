import gamePlay, gameBoard, terminalGraphic, os

def getPlayerMove(board, side):

    moveInput= input('Your move is: ')
    if moveInput.lower() in ['q', 'quit', 'exit']:
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
        print(f'{gamePlay.Move(board.pieces[x0][y0].name, x0, y0, x1, y1, False).display()} is not a legal move, please input another square.')
        return getPlayerMove(board, side) 

        
if __name__ == "__main__":

    gameBoard= gameBoard.Board.init()
    
    while True:
        terminalGraphic.clearScreen()
        print('\nPlease input your move as: <x from><y from> <x to><y to>')
        print('For example, if you want to move a piece from E2 to E4, type: "E2 E4", "E2E4, "e2 e4", or "e2e4" (without quotation marks) then hit <ENTER>')
        print('Type q or quit to exit.\n')
        terminalGraphic.drawBoard(gameBoard)
        terminalGraphic.drawMove(gameBoard)
        print(f'Board score:  {gamePlay.Evaluate.materialValue(gameBoard)/10:+.2f}')
        if gameBoard.moveCounter%2 == 0:
            side= 'w'
            print('WHITE to move.')
            # print('All legal moves for White:')
        else:
            side= 'b'    
            print('BLACK to move.')
            # print('All legal moves for Black:')

        # for move in gameBoard.allLegalMove(side):
        #     print('  ', move.display())

        playerMove= getPlayerMove(gameBoard, side)
        if playerMove == 0:
            break
        
        gameBoard.makeMove(playerMove)

    print('Thanks for playing the game!')        
        


