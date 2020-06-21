import gameplay, data, visual, os

def clearScreen():
    if os.name == 'nt': 
        os.system('cls') 
    else:
        os.system('clear')  

if __name__ == "__main__":
    clearScreen()
    gameBoard= data.Board.init()
    gameBoard.makeMove(gameplay.Move('p', 4, 1, 4, 3))
    gameBoard.makeMove(gameplay.Move('p', 4, 6, 4, 4))
    gameBoard.makeMove(gameplay.Move('Q', 3, 0, 6, 3))

    visual.drawBoard(gameBoard)
    visual.drawMove(gameBoard)
    print()
    for move in gameBoard.pieces[4][0].legalMoves(gameBoard):
        print(move.display())