import aiarena
from .minimax.limited_time import minimax
from .evaluation_functions import connect4, checkers
import subprocess as sp
import time

# definition d'un dictionaire qui associe à chaque jeu une fonction d'évaluation
evaluations_functions = {
    aiarena.checkers: checkers.evaluate,
    aiarena.connect4: connect4.evaluate
}

def compute_research_time(gs):
    ###########################
    #  CALCUL DE T_RECHERCHE  #
    ###########################
    return 0

class MinimaxBrain:

    def __init__(self, gameclass, gameclass_arguments={}):
        ####################################
        #  APPEL de compute_research_time  #
        ####################################
        self.get_children = gameclass.GameState.findNextStates
        self.evaluate = evaluations_functions[gameclass]

    def play(self, gameState, timeLimit):
        possibleMoves = gameState.findPossibleMoves()
        sp.check_call('clear')
        gameState.display(showBoard=True)

        indice_opti = 0
        gameState_copy = gameState.copy()
        gameState_copy.doMove(possibleMoves[0])
        score_opti = minimax(gameState_copy,True,self.get_children,self.evaluate,#T_RECHERCHE)
        for i,move in enumerate(possibleMoves):
            gameState_copy = gameState.copy()
            gameState_copy.doMove(possibleMoves[i])
            score = minimax(gameState_copy,True,self.get_children,self.evaluate,#T_RECHERCHE)
            if score > score_opti :
                indice_opti=i
                score_opti=score
        return possibleMoves[i]
        
        


    def __str__(self):
        return "MiniMax_Player"