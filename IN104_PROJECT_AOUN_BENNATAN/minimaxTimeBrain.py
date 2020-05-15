import aiarena
from .minimax.limited_time_alphabeta import minimax
from .evaluation_functions import connect4, checkers
import subprocess as sp
import numpy as np
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
        tic = time.time()
        possibleMoves = gameState.findPossibleMoves()
        sp.check_call('clear')
        gameState.display(showBoard=True)
        gameState_copy = gameState.copy()
        gameState_copy.doMove(possibleMoves[0])
        movesNumber = len(possibleMoves)
        indice_opti = 0
        elapsed = time.time() - tic
        score_opti = minimax(gameState_copy,True,self.get_children,self.evaluate,(timeLimit-elapsed)/movesNumber,self.researchTime)
        for i,move in enumerate(possibleMoves[1:]):
            gameState_copy = gameState.copy()
            gameState_copy.doMove(move)
            elapsed= time.time() - tic
            score = minimax(gameState_copy,True,self.get_children,self.evaluate,(timeLimit-elapsed)/(movesNumber-(i+1)),self.researchTime)
            if score > score_opti :
                indice_opti=i+1
                score_opti=score
        return possibleMoves[indice_opti]
        
        


    def __str__(self):
        return "MiniMax_Player"