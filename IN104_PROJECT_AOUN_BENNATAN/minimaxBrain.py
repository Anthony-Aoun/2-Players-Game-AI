import aiarena
# changer l'import ci-dessous pour changer la version de minimax utilisée
from .minimax.limited_depth import minimax
from .evaluation_functions import connect4, checkers

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
        indice_opti = 0
        score_opti = minimax(possibleMoves[0],false,self.get_children,self.evaluate,self.depth)
        for move,i in enumerate(possibleMoves):
            score = minimax(possibleMoves[i],false,self.get_children,self.evaluate,self.depth)
            if score > score_opti :
                indice_opti=i
                score_opti=score
        return possibleMoves[i]
        


    def __str__(self):
        return "MiniMax_Player"

