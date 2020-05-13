#white is maximizing
#black is minimizing

import numpy as np
import time

def minimax(node, maximize, get_children, evaluate, maxTime):
    if (maxTime <= 0 or (get_children(node) == [])):
        return evaluate(node)
    
    if (maximize == True):
        best = -(np.Inf)
        elapsed=0
        childNumber = len(get_children(node))
        for i,child in enumerate(get_children(node)):
            tic = time.time()
            value = minimax(child, False, get_children, evaluate, (maxTime-elapsed)/(childNumber-i))
            best = max(best, value)
            elapsed += time.time() - tic
        return best

    elif (maximize == False):
        best = np.Inf
        elapsed=0
        childNumber = len(get_children(node))
        for i,child in enumerate(get_children(node)):
            tic = time.time()
            value = minimax(child, True, get_children, evaluate, (maxTime-elapsed)/(childNumber-i))
            best = min(best, value)
            elapsed+= time.time() - tic
        return best




