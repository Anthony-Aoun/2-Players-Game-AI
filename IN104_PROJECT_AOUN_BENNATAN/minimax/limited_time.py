#white is maximizing
#black is minimizing

import numpy as np
import time

def minimax(node, maximize, get_children, evaluate, maxTime, researchTime):
    tic = time.time()
    children = get_children(node)

    if (maxTime < researchTime or (children == [])):
        return evaluate(node)
    
    if (maximize == True):
        best = -(np.Inf)
        elapsed = 0
        childrenNumber = len(children)
        for i,child in enumerate(children):
            elapsed = time.time() - tic
            value = minimax(child, False, get_children, evaluate, (maxTime-elapsed)/(childrenNumber-i), researchTime)
            best = max(best, value)
        return best

    elif (maximize == False):
        best = np.Inf
        elapsed = 0
        childrenNumber = len(children)
        for i,child in enumerate(children):
            elapsed = time.time() - tic
            value = minimax(child, True, get_children, evaluate, (maxTime-elapsed)/(childrenNumber-i), researchTime)
            best = min(best, value)
        return best
    





