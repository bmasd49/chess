import gameplay, data, visual, os

def clearScreen():
    if os.name == 'nt': 
        os.system('cls') 
    else:
        os.system('clear')  

if __name__ == "__main__":
    clearScreen()
    gameBoard= data.Board.init()
    visual.drawBoard(gameBoard)

    gameBoard.makeMove(gameplay.Move(4, 7, 2, 7, True))
    visual.drawBoard(gameBoard)



