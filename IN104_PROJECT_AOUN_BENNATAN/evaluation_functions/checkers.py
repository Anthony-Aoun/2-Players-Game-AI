import aiarena 

#returns difference of pieces
def evaluate(gameState):
    white = 0
    black = 0
    for c in gameState.cells:
        if (c.isWhite == True) and (c.type != aiarena.checkers.cell.NONE):
            white += 1

        elif c.isWhite == False and (c.type != aiarena.checkers.cell.NONE):
            black += 1

    return (white-black)



    
