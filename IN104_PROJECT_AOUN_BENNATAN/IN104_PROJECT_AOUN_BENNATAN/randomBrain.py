import random
import sys
import subprocess as sp
from misc_copy import smart_display

class RandomBrain:
    def __init__(self):
        pass

    def play(self, gameState, timeLimit):
        random.seed()
        possibleMoves = gameState.findPossibleMoves()
        sp.check_call('clear')
        gameState.display(showBoard=True)
        pdn_list = [str(m) for m in possibleMoves]
        smart_display(pdn_list, count=True)
        while True:
            n = len(pdn_list)
            rdm_move = pdn_list[random.randrange(n)]
            return possibleMoves[pdn_list.index(rdm_move)]
        raise NotImplementedError()

    def __str__(self):
        return "Random_Player"
