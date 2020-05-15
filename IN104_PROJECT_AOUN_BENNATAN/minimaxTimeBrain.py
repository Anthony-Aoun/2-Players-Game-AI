import aiarena
from .minimax.limited_time_negascout_tt import minimax
from .evaluation_functions import connect4, checkers
import subprocess as sp
import time

# definition d'un dictionaire qui associe à chaque jeu une fonction d'évaluation
evaluations_functions = {
    aiarena.checkers: checkers.evaluate,
    aiarena.connect4: connect4.evaluate
}

# le compute fait la moyenne du temps pour findNextStates sur un même gamestate (méthode bête) 
# (une moyenne pour 10 lancers suffit, ça donne les mêmes résultats que pour beaucoup plus)
def compute_research_time(gs,gameclass):
    tic = time.time()
    for i in range(10):
        gameclass.GameState.findNextStates(gs)
    return (time.time() - tic)/10

class MinimaxBrain:

    def __init__(self, gameclass, gameclass_arguments={}):
        self.researchTime = compute_research_time(gameclass.GameState(),gameclass)
        self.get_children = gameclass.GameState.findNextStates
        self.evaluate = evaluations_functions[gameclass]

    def play(self, gameState, timeLimit):
        possibleMoves = gameState.findPossibleMoves()
        sp.check_call('clear')
        gameState.display(showBoard=True)
        indice_opti = 0
        gameState_copy = gameState.copy()
        gameState_copy.doMove(possibleMoves[0])
        movesNumber = len(possibleMoves)
        #+1 ne marchait pas...mais +2 marche
        score_opti = minimax(gameState_copy,True,self.get_children,self.evaluate,timeLimit/(movesNumber+2),self.researchTime)
        for i,move in enumerate(possibleMoves):
            gameState_copy = gameState.copy()
            gameState_copy.doMove(possibleMoves[i])
            score = minimax(gameState_copy,True,self.get_children,self.evaluate,timeLimit/(movesNumber+2),self.researchTime)
            if score > score_opti :
                indice_opti=i
                score_opti=score
        return possibleMoves[i]
        
        


    def __str__(self):
        return "MiniMax_Player"