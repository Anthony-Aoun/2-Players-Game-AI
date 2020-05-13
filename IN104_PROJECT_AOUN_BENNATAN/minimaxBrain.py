import aiarena
from .minimax.limited_depth_negascout import minimax
from .evaluation_functions import connect4, checkers
import subprocess as sp

# definition d'un dictionaire qui associe à chaque jeu une fonction d'évaluation
evaluations_functions = {
    aiarena.checkers: checkers.evaluate,
    aiarena.connect4: connect4.evaluate
}

class MinimaxBrain:

    def __init__(self, gameclass, gameclass_arguments={}):
        self.depth = 5      # Set the exploration depth here
        self.get_children = gameclass.GameState.findNextStates
        self.evaluate = evaluations_functions[gameclass]

    def play(self, gameState, timeLimit):
        possibleMoves = gameState.findPossibleMoves()
        sp.check_call('clear')
        gameState.display(showBoard=True)

        indice_opti = 0
        gameState_copy = gameState.copy()
        gameState_copy.doMove(possibleMoves[0])
        score_opti = minimax(gameState_copy,True,self.get_children,self.evaluate,self.depth)
        for i,move in enumerate(possibleMoves):
            gameState_copy = gameState.copy()
            gameState_copy.doMove(possibleMoves[i])
            score = minimax(gameState_copy,True,self.get_children,self.evaluate,self.depth)
            if score > score_opti :
                indice_opti=i
                score_opti=score
        return possibleMoves[i]
        
        


    def __str__(self):
        return "MiniMax_Player"

  